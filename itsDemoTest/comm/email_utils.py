#!/usr/bin/env python
# encoding: gbk
# @author: liusir
# @file: email_utils.py
# @time: 2020/10/18 2:38 下午

import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from itsDemoTest.comm.ReadConfig import config
import time
class EmailUtils:
    def __init__(self,smtp_body,smtp_attch_path=None,log_attch_path=None):
        self.smtp_server = 'smtp.qq.com'
        self.smtp_port = 25
        self.smtp_sender = '3048903923@qq.com'
        self.smtp_password = 'qsvgzpwencendgff'
        self.smtp_receiver = config.SMTP_RECEIVER
        self.smtp_cc = '3048903923@qq.com'
        self.smtp_subject = '智能工时2.0接口测试报告'
        self.smtp_body = smtp_body
        self.smtp_attch_path = smtp_attch_path
        self.log_attch_path = log_attch_path

    def email_message_body(self):
        message = MIMEMultipart()
        message['from'] = self.smtp_sender
        message['to'] = self.smtp_receiver
        message['Cc'] = self.smtp_cc
        message['subject'] = self.smtp_subject
        message.attach( MIMEText(self.smtp_body,'html','utf-8') )
        # 附件1
        if self.smtp_attch_path:
            attach_file_obj = MIMEText(open(self.smtp_attch_path, 'rb').read(), 'base64', 'utf-8')
            attach_file_obj['Content-Type'] = 'application/octet-stream'
            attach_file_obj.add_header('Content-Disposition', 'atachment',
                                       filename=('gbk', '', os.path.basename(self.smtp_attch_path)))
            message.attach(attach_file_obj)
        # 附件2
        if self.log_attch_path:
            attach_file_obj = MIMEText(open(self.log_attch_path, 'rb').read(), 'base64', 'utf-8')
            attach_file_obj['Content-Type'] = 'application/octet-stream'
            attach_file_obj.add_header('Content-Disposition', 'atachment',
                                       filename=('gbk', '', os.path.basename(self.log_attch_path)))
            message.attach(attach_file_obj)
        return message

    def send_mail(self):
        smtp = smtplib.SMTP()
        smtp.connect(self.smtp_server,self.smtp_port)
        smtp.login(self.smtp_sender,self.smtp_password)
        smtp.sendmail( self.smtp_sender,self.smtp_receiver.split(',')+self.smtp_cc.split(',')   ,self.email_message_body().as_string() )
