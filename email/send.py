import smtplib
import email
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

def send(name,user,passwd,qqnum):
    HOST = 'smtp.qq.com'
    SUBJECT = "有人申请注册账号"
    FROM = "2647936408@qq.com"
    TO = "1091057545@qq.com"

    message = MIMEMultipart('related')
    meru = "姓名:%s\n用户名:%s\n密码:%s\nQQ号:%s"%(name,user,passwd,qqnum)

    text = MIMEText(meru,'plain','utf-8') 
    message.attach(text)


    message['From'] = FROM
    message['To'] = TO
    message['Subject'] = SUBJECT

    email_client = smtplib.SMTP_SSL(host=HOST)
    email_client.connect(HOST,'465')


    ans = email_client.login(FROM,'cntbcmqvhynpebja')
    #print('kekka : ',ans)
    email_client.sendmail(from_addr=FROM,to_addrs=TO,msg=message.as_string())

    email_client.close()



if __name__ == '__main__':
    send("张三","admin","123456","123123")







