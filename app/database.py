# -*- coding: utf-8 -*-
# @Author: Landers
# @Github: Landers1037
# @File: database.py
# @Date: 2020-05-15

#数据库的封装调用
#当前就支持图片信息的添加和获取的封装
#其他操作使用逻辑判断

from app import db
from app.models import *
from app import mongo

class database:
    sql_map = {
        "image": Image,
        "token": Token
    }
    def set(self,engine,table,data):
        if engine == 'sqlite':
            #判断操作的表
            if table == 'image':
                try:
                    d = self.sql_map[table](name=data["name"], mail=data["mail"], path=data["path"], url=data["url"], time=data["time"])
                    db.session.add(d)
                    db.session.commit()
                    return True
                except:
                    db.session.rollback()
                    return False

            elif table == 'token':
                try:
                    t = self.sql_map[table](mail=data["mail"], token=data["token"],check='')
                    db.session.add(t)
                    db.session.commit()
                    return True
                except:
                    db.session.rollback()
                    return False

        else:
            #mongo
            if table == 'image':
                try:
                    mongo.db.images.insert_one({"name": data["name"],"mail": data["mail"], "path": data["path"],"url": data["url"],"time": data["time"]})
                    return True
                except Exception as e:
                    print(e.args)
                    return False

            elif table == 'token':
                try:
                    mongo.db.token.insert_one({"mail": data["mail"],"token": data["token"],"check": ''})
                    return True
                except:
                    return False    

    def get(self,engine,table,data):
        if engine == 'sqlite':
            if table == 'image':
                try:
                    d = self.sql_map[table].query.filter_by(name=data).first()
                    return d.info()
                except:
                    return {}

            elif table == 'token':
                #没有获取token的函数，这个查询的作用是判断当前传入token是否存在，存在则返回对应的mail
                try:
                    t = self.sql_map[table].query.filter_by(token=data).first()
                    if t:
                        return t.mail
                    else:
                        return None    
                except:
                    return None 
        else:
            #mongo
            if table == 'image':
                try:
                    i =  mongo.db.images.find_one({"name": data})
                    return {"name": i["name"], "path": i["path"], "url": i["url"], "time": i["time"]}

                except Exception as e:
                    print(e.args)
                    return {}

            elif table == 'token':
                try:
                    t =  mongo.db.token.find_one({"token": data})
                    if t:
                        return t["mail"]
                    else:
                        return None    

                except:
                    return None     

    def get_token(self,engine,data):
        #单独的通过mail获取token的函数
        if engine == 'sqlite':
            try:
                t = Token.query.filter_by(mail=data).first()
                return t.token
            except:
                return None    
        else:
            try:
                t = mongo.db.token.find_one({"mail": data})
                return t["token"]
            except:
                return None

    def get_image_list(self,engine,data):
        if engine == 'sqlite':
            try:
                img_list = Image.query.filter_by(mail=data).all()
                return img_list
            except:
                return False
        else:
            try:
                img_list = mongo.db.images.find({"mail": data})
                return img_list
            except:
                return False    


    def update_token(self,engine,data):
        if engine == 'sqlite':
            try:
                t = Token.query.filter_by(mail=data["address"]).first()
                t.check = data["check"]
            except:
                pass
        else:
            try:
                t = mongo.db.token.update_one({"address": data["address"]}, {'$set': {"check": data["check"]}})
            except:
                pass    

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

    def remove_token(self,engine,data):

        if engine == 'sqlite':
            try:
                mail = data["mail"]
                if data["token"]:
                    #通过token删除
                    t = Token.query.filter_by(mail=mail).first()
                    if t.token == data["token"]:
                        try:
                            db.session.delete(t)
                            db.session.commit()
                            return True
                        except:
                            db.session.rollback()
                            return False    
                    else:
                        return False
                elif data["check"]:
                    t = Token.query.filter_by(mail=mail).first()
                    if t.check == data["check"]:
                        try:
                            db.session.delete(t)
                            db.session.commit()
                            return True
                        except:
                            db.session.rollback()
                            return False
                    else:
                        return False
            except:
                return False                                  
        else:
            mail = data["mail"]
            if data["token"]:
                t = mongo.db.token.find_one({"mail": mail})
                if t["token"] == data["token"]:
                    try:
                        mongo.db.token.delete_one({"mail": mail})
                        return True
                    except:
                        return False  
                else:
                    return False
            elif data["check"]:
                t = mongo.db.token.find_one({"mail": mail})
                if t["check"] == data["check"]:
                    try:
                        mongo.db.token.delete_one({"mail": mail})
                        return True
                    except:
                        return False  
                else:
                    return False        
