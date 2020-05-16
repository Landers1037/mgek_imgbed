# -*- coding: utf-8 -*-
# @Author: Landers
# @Github: Landers1037
# @File: database.py
# @Date: 2020-05-15

#数据库的封装调用
#当前就支持图片信息的添加和获取的封装
#其他操作使用逻辑判断

from flask_pymongo import MongoClient
from app import db
from app.models import *
from app import mongo

class database:
    sql_map = {
        "image": Image
    }
    def set(self,engine,table,data):
        if engine == 'sqlite':
            try:
                d = self.sql_map[table](name=data["name"], path=data["path"], url=data["url"], time=data["time"])
                db.session.add(d)
                db.session.commit()
            except:
                db.session.rollback()
        else:
            #mongo
            try:
                mongo.db.images.insert_one({"name": data["name"],"path": data["path"],"url": data["url"],"time": data["time"]})
            except Exception as e:
                print(e.args)
                pass     

    def get(self,engine,table,data):
        if engine == 'sqlite':
            try:
                d = self.sql_map[table].query.filter_by(name=data).first()
                return d.info()
            except:
                return {}    
        else:
            try:
                data =  mongo.db.images.find_one({"name": data})
                return {"name": data["name"], "path": data["path"], "url": data["url"], "time": data["time"]}

            except Exception as e:
                print(e.args)
                return {}   

    def delete(self,engine,table,data):
        if engine == 'sqlite':
            try:
                d = self.sql_map[table].query.filter_by(name=data).first()
                db.session.delete(d)
                db.session.commit()
            except:
                db.session.rollback()                 

        else:
            try:
                data = mongo.db.images.delete_one({"name": data})
            except:
                pass  

    def delete_many(self, engine, table, data):
        if engine == 'sqlite':
            try:
                for d in data:
                    d = self.sql_map[table].query.filter_by(name=d).first()
                    db.session.delete(d)
                db.session.commit()
            except:
                db.session.rollback()

        else:
            try:
                for d in data:
                    data = mongo.db.images.delete_one({"name": d})
            except:
                pass
