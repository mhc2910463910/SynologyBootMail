import base64
import smtplib
import schedule
import time
from email.mime.text import MIMEText
from email.header import Header

sender_email = '发件人邮箱'
password = '发件人授权码'
receiver_email = '收件人邮箱'
sender_name = '发件人名称 <发件人邮箱>'

def send_email():
    global account, password, receiver
    mailhost = 'smtp.qq.com'
    qqmail = smtplib.SMTP_SSL(mailhost, 465)
    qqmail.login(account, password)
    content = '邮件内容'
    message = MIMEText(content, 'plain', 'utf-8')
    subject = '邮件标题'
    message['From'] = Header(sender_email)
    message['Subject'] = Header(subject, 'utf-8')
    try:
        qqmail.sendmail(account, receiver, message.as_string())
        print('邮件发送成功')
    except Exception as e:
        print(f'邮件发送失败:{e}')
    qqmail.quit()

if __name__ == '__main__':
    send_email()