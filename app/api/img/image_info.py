# -*- coding: utf-8 -*-
# @Author: Landers
# @Github: Landers1037
# @File: image_info.py
# @Date: 2020-05-14

from app.api.img import img
from app.utils import format_response
from flask import request
from app.database import database
from app import global_config

@img.route('/api/image_info')
def image_info():
    # 根据图片的id获取图片信息
    try:
        name = request.json["name"]
        img = database().get(global_config.engine,'image',name)
        if img:
            return format_response('ok',img)
        else:
            return format_response('error','图片信息获取失败')
            
    except Exception as e:
        
        return format_response('error', '图片信息获取失败')
