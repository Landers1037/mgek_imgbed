# -*- coding: utf-8 -*-
# @Author: Landers
# @Github: Landers1037
# @File: image_format.py
# @Date: 2020-05-15

#输出适用多种格式的图片信息

from app.api.img import img
from app.database import database
from flask import request
from app.utils import format_response
from app import global_config

@img.route('/api/image_format')
def image_format():
    name = request.json["name"]
    try:
        img = database().get(global_config.engine,'image',name)
        print(global_config.image_url)
        res = {
            "raw": img["name"],
            "link": "{}{}".format(global_config.image_url,img["name"]),
            "html": "<img src={}{} alt=image>".format(global_config.image_url,img["name"]),
            "markdown": "![image]({}{})".format(global_config.image_url,img["name"])
        }
        return format_response('ok',res)

    except Exception as e:
        print(e.args)
        return format_response('error','获取格式化信息失败')
