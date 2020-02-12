# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 14:15:50 2020

@author: sunil shetty
"""
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


fromaddr="xyz@gmail.com"
toaddr="abcd@gmail.com"
msg=MIMEMultipart()
msg['From']=fromaddr
msg['To']=toaddr
msg['Subject']="found"
body="sent from xyz"
msg.attach(MIMEText(body,'plain'))
filename="abc.jpg"
attachment=open("D:/face/faces/abc.jpg","rb")

p=MIMEBase('application','octet-stream')
p.set_payload((attachment).read())

encoders.encode_base64(p)

p.add_header('Content-Disposition',"attachment; filename=%s"%filename)
msg.attach(p)

s=smtplib.SMTP('smtp.gmail.com',587)

s.starttls()

s.login(fromaddr,"sender mail password")

text=msg.as_string()

s.sendmail(fromaddr,toaddr,text)

s.quit()
