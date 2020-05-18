# -*- coding: utf-8 -*-
# @Author: Landers
# @Github: Landers1037
# @File: get_token.py
# @Date: 2020-05-16

from app.middleware.jwt_middleware import genernate
from app.auth import auth
from flask import jsonify,g,request
from app import global_config
from app import db
from app.models import Token
from app import mongo

@auth.route('/api/get_token',methods=['POST'])
def get_token():
    try:
        mail = request.json["mail"]
        g.token = genernate(mail)
        """
        在这里添加保存至数据库的函数
        """
        if global_config.engine == 'sqlite':
            try:
                t = Token(mail=mail,token=g.token)
                db.session.add(t)
                db.session.commit()
                return jsonify({"token": g.token})
                
            except:
                db.session.rollback()
                return jsonify({"token": ''})
        else:
            #mongo
            try:
                mongo.db.token.insert_one({"mail": mail,"token": g.token,"check": ""})
                return jsonify({"token": g.token})
                
            except:
                return jsonify({"token": ''})
    except:
        return jsonify({"token": ''})    
