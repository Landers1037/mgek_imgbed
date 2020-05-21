# -*- coding: utf-8 -*-
# @Author: Landers
# @Github: Landers1037
# @File: mail.py
# @Date: 2020-05-17

#发送邮件函数
import smtplib,time
from email.mime.text import MIMEText
from email.header import Header
from flask import current_app

from app import global_config
from app.database import database

def mail_to(address):
    HOST = current_app.config["MAIL_HOST"]
    PORT = current_app.config['MAIL_PORT']
    USER = current_app.config['MAIL_USER']
    PASS = current_app.config['MAIL_PASS']

    sender = USER
    receiver = address

    t = database().get_token(global_config.engine,address) 
    if t:
        token = t
        #生成check标志

        link = get_check(address)
        message = MIMEText('请妥善保管你的认证密钥\n{}，如果你的邮箱没有在本站点注册很抱歉打扰您，请点击以下链接删除您的账户,{}'.format(token,link), 'plain', 'utf-8')
        message['From'] = sender
        message['To'] = address

        subject = 'Mgek_ImgBed认证密钥找回服务'
        message['Subject'] = Header(subject, 'utf-8')
        try:
            smtp = smtplib.SMTP_SSL(host=HOST,port=PORT)
            smtp.login(USER,PASS)
            smtp.sendmail(sender,receiver,message.as_string())
            smtp.quit()
            return True

        except Exception as e:
            print(e.args)
            return False
    else:
        return False     


def get_check(address):
    #生成临时check标志，针对本身不存在的账户生成空信息
    #存在
    check = str(time.time())
    database().update_token(global_config.engine,{"address": address,"check": check})
        
    #请在地址栏填写本站点运行的域名，或者在flask_config里修改server_name参数
    server_name = current_app.config['SERVER_NAME'] if current_app.config['SERVER_NAME'] else 'localhost:{}'.format(
            global_config.port)
            
    return 'http://{}/api/remove_token?mail={}&check={}'.format(server_name,address,check)

          
