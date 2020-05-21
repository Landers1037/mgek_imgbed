# -*- coding: utf-8 -*-
# @Author: Landers
# @Github: Landers1037
# @File: remove_token.py
# @Date: 2020-05-17

#用户注销账户的接口

from app.api.auth import auth
from flask import request
from app.utils import format_response
from app import global_config
from app.database import database

@auth.route('/api/remove_token')
def remove_token():
    #支持两种判断方式 输入邮箱token后验证
    #通过邮件里的check标志验证
    mail =request.args.get('mail')
    token = request.args.get('token')
    check = request.args.get('check')

    if mail and token:
        
        res = database().remove_token(global_config.engine,{"mail":mail,"token":token})
        if res:
            return format_response('ok', '密钥删除成功')
        else:
           return format_response('error', '密钥删除失败')

    elif mail and check:
        res = database().remove_token(global_config.engine,
                               {"mail": mail, "check": check})
        if res:
            return format_response('ok', '密钥删除成功')
        else:
           return format_response('error', '密钥删除失败')
     
    else:
        return format_response('error', '密钥删除失败,信息不全')


