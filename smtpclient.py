from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import smtplib

class SMTPClient:
    def __init__(self,host, email,password,port=465):
        self.s = smtplib.SMTP_SSL(host, port)
        self.email = email
        self.password = password
        self.s.login(self.email, self.password)

    def sendMail(self, subject, to, message):
        msg = MIMEText(message)
        msg['From'] = self.email
        msg['To'] = ', '.join(to)
        msg['Subject'] = subject
        self.s.send_message(msg)
        del msg



