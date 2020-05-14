# -*- coding: utf-8 -*-
# @Author: Landers
# @Github: Landers1037
# @File: format_response.py
# @Date: 2020-05-14

#用于格式化需要返回的数据JSON

from flask import jsonify

def format_response(type: str,msg):
    """
    type: 返回数据的类型，应该分为error，forbidden，ok
    """
    return jsonify({
        "type": type,
        "data": msg
    })