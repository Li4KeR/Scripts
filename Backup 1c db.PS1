[Console]::OutputEncoding = [System.Text.Encoding]::GetEncoding("cp866")

#perem
$name = get-date -f 'dd.MM'
$BackupFrom = 'X:\1cBase\BUH'
$BackupFrom2 = 'X:\1cBase\ZUP'
$BackupWhere = 'Y:\1c_backup\$name.zip'

#smtp
$serverSmtp = "smtp.yandex.ru"
$port = 587
$From = from
$To = to
$subject = "Backup 1C"
$user = login_mail
$pass = pass_mail
$file = "Y:\logs\log_mail.txt"

#backup base 7z
&"C:\Program Files\7-Zip\7z.exe" a -r $BackupWhere $BackupFrom, $GBackupFrom2 | out-file $file -Encoding utf8
$backup = Get-Content -Path $file

#send mail
$att = New-object Net.Mail.Attachment($file)
$mes = New-Object System.Net.Mail.MailMessage
$mes.From = $from
$mes.To.Add($to)
$mes.Subject = $subject
$mes.IsBodyHTML = $true
$mes.Body = "$backup>"
$mes.Attachments.Add($att)
$smtp = New-Object Net.Mail.SmtpClient($serverSmtp, $port)
$smtp.EnableSSL = $true
$smtp.Credentials = New-Object System.Net.NetworkCredential($user, $pass);
$smtp.Send($mes)
$att.Dispose()
