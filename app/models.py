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


    def __init__(self,name,path):
        self.name = name
        self.path = path
    
    def info(self):
        return {
            "name": self.name,
            "path": self.path
        }