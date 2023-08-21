import smtplib

smtp = smtplib.SMTP_SSL('smtp.naver.com', 465)

smtp.ehlo()

my_password = open('secret.txt', 'r').read()
smtp.login('mail@naver.com', my_password)

from email.message import EmailMessage
msg = EmailMessage()


msg['Subject'] = '메일 제목'
msg['FROM'] = 'mail@naver.com'
msg['TO'] = 'mail@gmail.com'
msg.set_content('메일 본문')

smtp.send_message(msg)

smtp.quit()