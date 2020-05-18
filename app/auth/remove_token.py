# -*- coding: utf-8 -*-
# @Author: Landers
# @Github: Landers1037
# @File: remove_token.py
# @Date: 2020-05-17

#用户注销账户的接口

from app.auth import auth
from flask import request
from app import db
from app.models import Token
from app import mongo
from app.utils import format_response
from app import global_config

@auth.route('/api/remove_token')
def remove_token():
    #支持两种判断方式 输入邮箱token后验证
    #通过邮件里的check标志验证
    mail =request.args.get('mail')
    token = request.args.get('token')
    check = request.args.get('check')

    if global_config.engine == 'sqlite':
        if mail and token:
            t = Token.query.filter_by(mail=mail).first()
            try:
                if t.token == token:
                    #验证成功
                    db.session.delete(t)
                    db.session.commit()
                    return format_response('ok','密钥删除成功')
                else:
                    return format_response('error', '密钥删除失败')
            except:
                db.session.rollback()
                return format_response('error', '密钥删除失败')

        elif mail and check:
            t = Token.query.filter_by(mail=mail).first()
            try:
                if t.check == check:
                    #验证成功
                    db.session.delete(t)
                    db.session.commit()
                    return format_response('ok','密钥删除成功')
                else:
                    return format_response('error', '密钥删除失败')
            except:
                db.session.rollback()
                return format_response('error', '密钥删除失败')
                
        else:
            return format_response('error', '密钥删除失败,信息不全')

    else:
        #mongo
        if mail and token:
            t = mongo.db.token.find_one({"mail":mail})
            try:
                if t["token"] == token:
                    #验证成功
                    mongo.db.token.delete_one({"mail": mail})
                    return format_response('ok','密钥删除成功')
                else:
                    return format_response('error', '密钥删除失败')
            except:
                return format_response('error', '密钥删除失败')

        elif mail and check:
            t = mongo.db.token.find_one({"mail": mail})
            try:
                if t["check"] == check:

                    #验证成功
                    mongo.db.token.delete_one({"mail": mail})
                    return format_response('ok','密钥删除成功')
                else:
                    return format_response('error', '密钥删除失败')
                    
            except:
                return format_response('error', '密钥删除失败')
                
        else:
            return format_response('error', '密钥删除失败,信息不全')        


