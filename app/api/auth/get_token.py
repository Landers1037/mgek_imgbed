# -*- coding: utf-8 -*-
# @Author: Landers
# @Github: Landers1037
# @File: get_token.py
# @Date: 2020-05-16

from app.middleware.jwt_middleware import genernate
from app.api.auth import auth
from flask import jsonify,g,request
from app import global_config

from app.database import database

@auth.route('/api/get_token',methods=['POST'])
def get_token():
    try:
        mail = request.json["mail"]
        g.token = genernate(mail)
        """
        在这里添加保存至数据库的函数
        #注意如果原本账户存在 不能更新只能找回
        """
        ifexist = database().get_token(global_config.engine,mail)
        if not ifexist:
            res = database().set(global_config.engine,'token',{"mail": mail,"token": g.token})
            if res:
                return jsonify({"token": g.token})
            else:
                return jsonify({"token": ''})

        else:
            return jsonify({"token": 'already exist'})
    except:
        return jsonify({"token": ''})    
