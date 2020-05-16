# -*- coding: utf-8 -*-
# @Author: Landers
# @Github: Landers1037
# @File: image_list.py
# @Date: 2020-05-14


from app.api import api
from app.models import Image
from app.utils import format_response
from flask import request
from flask import g
from app import global_config
from app import mongo
from app.utils import count_page

@api.route('/api/image_list')
def image_list():
    #支持按需获取图片列表 用于前端的懒加载
    try:
        if request.args.get('page'):
            #分页情况
            #默认从第一页开始
            if global_config.engine == 'sqlite':
                try:
                    # pages = count_page(all,global_config.image_page)
                    p = Image.query.paginate(1,10)
                    #暂未实现
                    return format_response('ok',10)

                except:
                    return format_response('error','获取图片列表错误')    
            else:
                pass    

        else:
            #默认返回全部图片列表
            #包含图片总数，计算得到的图片分页数
            g.data = []
            if global_config.engine == 'sqlite':
                img_list = Image.query.all()
                for i in img_list:
                    g.data.append(i.info())
            else:
                img_list = mongo.db.images.find()
                for i in img_list:
                    g.data.append({"name": i["name"], "path": i["path"], "url": i["url"]})

            return format_response('ok',g.data)  

    except Exception as e:
        print((e.args))
        return format_response('error','图片列表加载失败')    
