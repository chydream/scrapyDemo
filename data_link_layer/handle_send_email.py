import smtplib
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.text import MIMEText


class Handle_Send_Email(object):
    def __init__(self):
        self.client = smtplib.SMTP("smtp.qq.com")
        self.client.starttls()
        self.client.login('710962261@qq.com', "zrfjiakcaexfbbfj")

    def send_email(self, address):
        msg = MIMEMultipart()
        msg['Subject'] = Header('测试邮件', 'utf-8')
        msg['From'] = Header("710962261@qq.com")
        content = MIMEText("PYTHON课程", 'plain', 'utf-8')
        msg.attach(content)
        self.client.sendmail('710962261@qq.com', address, msg.as_string())
        self.client.close()

client = Handle_Send_Email()
client.send_email("710962261@qq.com")