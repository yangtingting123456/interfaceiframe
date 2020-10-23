import mimetypes
import smtplib
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
import  datetime
import os
filepath = 'D:\\Program Files\\JetBrains\\interfac_request\\itsDemoTest\\reports\\API_TEST_V1.0\\API_TEST_V1.0.html'

smtp_server = "smtp.qq.com"
username = "3048903923@qq.com"
password = "qsvgzpwencendgff"
sender = '3048903923@qq.com'
receivers = '3048903923@qq.com'

time = datetime.datetime.today().strftime("%Y-%m-%d_%H:%M")
msg = MIMEMultipart()
# 邮件正文
msg.attach(MIMEText("{}的测试报告见附件".format(time),'plain','utf-8'))
msg['From'] = "3048903923@qq.com"
msg['To'] = "3048903923@qq.com"
subject = "{}的测试报告".format(time)
msg['Subject'] = subject

data = open(filepath,'rb+')
ctype, encoding = mimetypes.guess_type(filepath)
if ctype is None or encoding is not None:
    ctype = 'application/octet-stream'
maintype, subtype = ctype.split('/', 1)
file_msg = MIMEBase(maintype, subtype)
file_msg.set_payload(data.read())
data.close()
encoders.encode_base64(file_msg)  # 把附件编码
file_msg.add_header('Content-Disposition', 'attachment', filename="测试报告.zip")  # 修改邮件头
msg.attach(file_msg)
try:
    server = smtplib.SMTP(smtp_server,25)
    server.login(username,password)
    server.sendmail(sender,receivers,msg.as_string())
    server.quit()
    print("发送成功")
except Exception as err:
    print("发送失败")
    print(err)
