<<<<<<< HEAD
# -*- coding: utf-8 -*-
# @Author: Landers
# @Github: Landers1037
# @File: image_delete.py
# @Date: 2020-05-14

from app.api.img import img
from app.utils import format_response
from flask import request
from app.database import database
from app import global_config

@img.route('/api/image_delete',methods=['POST'])
def image_delete():
    #根据图片的唯一ID删除对应的文件
    try:
        data = request.json
        if "namaelist" in data.keys():
            try:
                database().delete_many(global_config.engine,'image',data["namelist"])
                return format_response('ok', '文件删除成功')

            except:
                return format_response('error', '文件删除失败')

        elif "name" in data.keys():
            try:
                database().delete(global_config.engine,'image',data["name"])
                return format_response('ok','文件删除成功')
            except:
                return format_response('error','文件删除失败')
                
    except Exception as e:
        print(e.args)
        return format_response('error', '文件删除失败')
=======
# -*- coding: utf-8 -*-
# @Author: Landers
# @Github: Landers1037
# @File: image_delete.py
# @Date: 2020-05-14

from app.api.img import img
from app.utils import format_response
from flask import request
from app.database import database
from app import global_config

@img.route('/api/image_delete',methods=['POST'])
def image_delete():
    #根据图片的唯一ID删除对应的文件
    data = request.json
    if "namaelist" in data.keys():
        database().delete_many(global_config.engine,'image',data["namelist"])
        return format_response('ok', '文件删除成功')

    elif "name" in data.keys():
        database().delete(global_config.engine,'image',data["name"])
        return format_response('ok','文件删除成功')
>>>>>>> 82249f551dc1b0b7f3404782bc29efd70c88a15a
