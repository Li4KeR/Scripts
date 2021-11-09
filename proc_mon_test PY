import time
import psutil
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

addr_from = "FROM"
addr_to = "TO"
password = "PASS_FROM"

msg = MIMEMultipart()
msg['From'] = addr_from
msg['To'] = addr_to
msg['Subject'] = 'Proc more than 65%'
body = "Danger Server!"
msg.attach(MIMEText(body, 'plain'))

while True:
    x = psutil.cpu_percent()
    if x > 50.0 :
        server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
        server.login(addr_from, password)
        server.send_message(msg)
        server.quit()
        time.sleep(60)
    else:
        print(x)
        time.sleep(300)
