# -*- coding: utf-8 -*-
# @Author: Landers
# @Github: Landers1037
# @File: models.py
# @Date: 2020-05-14

# 数据库的配置文件 slqite适用

from app import db

class Image(db.Model):
    __tablename__ = 'image'
    name = db.Column(db.String(100),primary_key=True) #图片唯一id
    mail = db.Column(db.String(50),nullable=False) #图片所属的账户
    path = db.Column(db.String(100),nullable=False) #图片地址
    url = db.Column(db.String(100),nullable=False) #图片在服务器上的地址
    time = db.Column(db.Integer) #图片更新时间

    def __init__(self,name,mail,path,url,time):
        self.name = name
        self.mail = mail
        self.path = path
        self.url = url
        self.time = time
    
    def info(self):
        return {
            "name": self.name,
            "path": self.path,
            "url": self.url,
            "time": self.time
            #为保证图片信息安全不返回所属账户
        }

class Token(db.Model):
    __tablename__ = 'token'
    mail = db.Column(db.String(50),primary_key=True)
    token = db.Column(db.String(100))
    check = db.Column(db.String(100),nullable=True)

    def __init__(self,mail,token,check):
        self.mail = mail
        self.token = token
        self.check = check

    def info():
        return {
            "token": self.token
        }
