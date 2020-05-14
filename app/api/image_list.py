# -*- coding: utf-8 -*-
# @Author: Landers
# @Github: Landers1037
# @File: image_list.py
# @Date: 2020-05-14


from app.api import api
from app import db
from app.models import Image
from app.utils import format_response
from flask import request
from flask import g

@api.route('/api/image_list')
def image_list():
    #支持按需获取图片列表 用于前端的懒加载
    try:
        if request.args.get('page'):
            #分页情况
            pass
        else:
            #默认返回全部图片列表
            img_list = Image.query.all()
            g.data = []
            for i in img_list:
                g.data.append(i.info())

            return format_response('ok',g.data)    
    except:
        return format_response('error','图片列表加载失败')    