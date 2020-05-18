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
#sqlite
from app.models import Token
from app import db
#mongo
from app import mongo
from app import global_config

def mail_to(address):
    HOST = current_app.config["MAIL_HOST"]
    PORT = current_app.config['MAIL_PORT']
    USER = current_app.config['MAIL_USER']
    PASS = current_app.config['MAIL_PASS']

    sender = USER
    receiver = address

    t = None
    if global_config.engine == 'sqlite':
        t = Token.query.filter_by(mail=address).first()
    else:
        t = mongo.db.token.find_one({"mail":address})    
    if t:
        if global_config.engine == 'sqlite':
            token = t.token
        else:
            token = t["token"]    
        #生成check标志

        link = get_check(address,t)
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


def get_check(address,t):
    #生成临时check标志，针对本身不存在的账户生成空信息
    if global_config.engine == 'sqlite':
        #存在
        check = str(time.time())
        t.check = check
        db.session.commit()
        #请在地址栏填写本站点运行的域名，或者在flask_config里修改server_name参数
        server_name = current_app.config['SERVER_NAME'] if current_app.config['SERVER_NAME'] else 'localhost:{}'.format(
            global_config.port)
        return 'http://{}/api/remove_token?mail={}&check={}'.format(server_name,address,check)
    else:
        check = str(time.time())
        mongo.db.token.update_one({"mail": address},{'$set': {"check": check}})
        server_name = current_app.config['SERVER_NAME'] if current_app.config['SERVER_NAME'] else 'localhost:{}'.format(
            global_config.port)
        return 'http://{}/api/remove_token?mail={}&check={}'.format(server_name, address, check)
          
