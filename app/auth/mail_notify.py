# -*- coding: utf-8 -*-
# @Author: Landers
# @Github: Landers1037
# @File: mail_notify.py
# @Date: 2020-05-17

#用于找回信息的邮件通知服务
from app.auth import auth
from app.utils import format_response,mail_to
from flask import request

@auth.route('/api/mail_for_reset',methods=['POST'])
def mail_for_reset():
    #获取用户的mail地址 给目标用户发送找回邮件
    try:
        address = request.json["mail"]
        if mail_to(address):
            return format_response('ok', '找回邮件已发送')
        else:
            return format_response('error', '请求找回错误')

    except Exception as e:
        print(e.args)
        return format_response('error','请求找回错误')
