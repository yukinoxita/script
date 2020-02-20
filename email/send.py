import smtplib
import email
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

def send():
    HOST = 'smtp.qq.com'
    SUBJECT = ""
    FROM = ""
    TO = ""

    message = MIMEMultipart('related')
    meru = ""

    text = MIMEText(meru,'plain','utf-8') 
    message.attach(text)


    message['From'] = FROM
    message['To'] = TO
    message['Subject'] = SUBJECT

    email_client = smtplib.SMTP_SSL(host=HOST)
    email_client.connect(HOST,'465')


    ans = email_client.login(FROM,'授权码')
    email_client.sendmail(from_addr=FROM,to_addrs=TO,msg=message.as_string())

    email_client.close()



if __name__ == '__main__':
    send()






