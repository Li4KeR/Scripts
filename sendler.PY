import fdb
import pandas as pd
import os
from datetime import date
import ftplib

import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


#perem
df = pd.DataFrame()
days_in_year = 365.2425
now = date.today().strftime('%d.%m.%Y')
filename = 'logging.txt'

#ftp_acc
USER = 'FTP_USER'
PASS = 'FTP_PASS'
SERVER = 'FTP_IP'

#mail_inf
subject = "Логи за " + now
body = "Отчет отправки за " + now + "во вложении"
sender_email = 'FROM'
receiver_email = 'TO'
password = 'PASS_FROM'

#BD
name_BD = 'SERV:BD'
user_BD = 'USER_BD'
pass_BD = 'PASS_BD'


#parse_bd
try:
    con = fdb.connect(dsn='name_DB', user='user_BD', password='pass_BD')
    cur = con.cursor()
    cur.execute("""
                    select CLIENTS.LASTNAME as lname, CLIENTS.FIRSTNAME as fname, CLIENTS.MIDNAME as mname,
                    CLIENTS.PHONE as number, TREAT.PCODE as code, CLIENTS.FILIAL as filial, TREAT.TREATDATE as fdate, CLIENTS.BDATE as BDate
                    from treat, clients
                    where treat.pcode=clients.pcode and treatdate=CURRENT_DATE-1 and depnum not like 10013511 and primtreat=1
                    and CLIENTS.REFUSESMS not like 1
                    """
                    )
except:
    with open('logging.txt', "a") as logfile:
        print('Error parse_bd ' + now, file=logfile)
else:
    with open('logging.txt', "a") as logfile:
        print('All fine parse_bd ' + now, file=logfile)


#parse_to_csv
try:
    for row in cur.itermap():
        if int((date.today() - row['BDATE'].date()).days / days_in_year)>= 18:
            new_row = {
                        'SURNAME':row['lname'],
                        'NAME':row['fname']+' '+row['mname'],
                        'PHONE':row['number'],
                        'PATIENT_ID':row['code'],
                        'BRANCH_ID':row['filial'],
                        'VISIT_DATE':row['fdate'].date().strftime("%d.%m.%Y"),
                        }
            df = df.append(new_row, ignore_index=True)
    df[['PATIENT_ID', 'BRANCH_ID']] = df[['PATIENT_ID', 'BRANCH_ID']].astype(int)
    df.to_csv('MK-' + now + '.csv', index=False, encoding="windows-1251", sep=';')
except:
    with open('logging.txt', "a") as logfile:
        print('Error creat csv ' + now, file=logfile)
else:
    with open('logging.txt', "a") as logfile:
        print('All fine creat csv ' + now, file=logfile)


#send_ftp
try:
    ftp = ftplib.FTP(SERVER)
    ftp.login(USER, PASS)
    with open('MK-' + now + '.csv', 'rb') as upload_file:
        ftp.storbinary('STOR ' + 'MK-' + now + '.csv', upload_file)
    ftp.close
except:
    with open("logging.txt", "a") as logfile:
        print('Error send ftp ' + now, file=logfile)
else:
    with open("logging.txt", "a") as logfile:
        print('All fine send ftp ' + now, file=logfile)


#send_mail
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message["Bcc"] = receiver_email

message.attach(MIMEText(body, "plain"))

with open(filename, "rb") as attachment:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

encoders.encode_base64(part)

part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)

message.attach(part)
text = message.as_string()

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.yandex.ru", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, text)
