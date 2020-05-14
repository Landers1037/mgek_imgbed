# -*- coding: utf-8 -*-
# @Author: Landers
# @Github: Landers1037
# @File: image_info.py
# @Date: 2020-05-14

from app.api import api
from app import db
from app.models import Image
from app.utils import format_response
from flask import request

@api.route('/api/image_info')
def image_info():
    # 根据图片的id获取图片信息
    try:
        name = request.json["name"]
        img = Image.query.filter_by(name=name).first()
        if img:
            return format_response('ok',img.info())
        else:
            return format_response('error','图片信息获取失败')
    except:
        return format_response('error', '图片信息获取失败')
