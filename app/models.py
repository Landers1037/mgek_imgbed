# -*- coding: utf-8 -*-
# @Author: Landers
# @Github: Landers1037
# @File: models.py
# @Date: 2020-05-14

# 数据库的配置文件 slqite适用

from app import db

class Image(db.Model):
    __tablename__ = 'image'
    name = db.Column(db.String(100),primary_key=True)
    path = db.Column(db.String(100),nullable=False)
    url = db.Column(db.String(100),nullable=False)
    time = db.Column(db.Integer)

    def __init__(self,name,path,url,time):
        self.name = name
        self.path = path
        self.url = url
        self.time = time
    
    def info(self):
        return {
            "name": self.name,
            "path": self.path,
            "url": self.url,
            "time": self.time
        }

class Token(db.Model):
    __tablename__ = 'token'
    mail = db.Column(db.String(50),primary_key=True)
    token = db.Column(db.String(100))

    def info():
        return {
            "token": self.token
        }