# -*- coding: utf-8 -*-
# @Author: Landers
# @Github: Landers1037
# @File: jwt_middleware.py
# @Date: 2020-05-16

#jwt装饰器
from flask import request,abort
from app.api import api
from itsdangerous import JSONWebSignatureSerializer
import time
from app.utils import format_response
from app.models import Token
from app import global_config
from flask import current_app

#仅支持sqlite数据库，你也可以自定义可信token
test_token = {"id": 1, "token": 'just_for_test'}


@api.before_request
def jwt_auth():
    if current_app.config["JWT"]:
        token = request.args.get('token')
        if token:
            if global_config.engine == 'sqlite':
                ts = Token.query.all()
                for t in ts:
                    if token == t.token:
                        pass
                    elif token == test_token["token"]:
                        pass
                    else:
                        return abort(401)
            else:
                # mongo not support
                pass
        else:
            #你可以使用常规的401权限码也可以使用统一响应码
            return format_response('forbidden','401 No Authority')
            #return abort(401)
    else:
        #不使用jwt时跳过认证
        pass                  

def genernate(mail):
    #生成token应该保存到数据库内部以做比较
    #根据时间生成token
    time_now = str(time.time())
    s = JSONWebSignatureSerializer('Please-input-your-secret-key')

    return s.dumps({"id": mail+time_now}).decode('utf-8')

