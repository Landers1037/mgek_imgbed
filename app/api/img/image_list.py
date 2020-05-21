<<<<<<< HEAD
# -*- coding: utf-8 -*-
# @Author: Landers
# @Github: Landers1037
# @File: image_list.py
# @Date: 2020-05-14


from app.api.img import img
from app.utils import format_response
from flask import request
from flask import g
from app import global_config

from app.utils import count_page
from app.database import database


@img.route('/api/image_list')
def image_list():
    #支持按需获取图片列表 用于前端的懒加载
    try:
        token = request.args.get('token')
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
            mail = database().get(global_config.engine, 'token', token)
            if mail:
                #仅获取当前用户下的图片列表
                if global_config.engine == 'sqlite':
                    img_list = database().get_image_list(global_config.engine,mail)
                    for i in img_list:
                        g.data.append(i.info())

                elif global_config.engine == 'mongo':
                    img_list = database().get_image_list(global_config.engine, mail)
                    for i in img_list:
                        g.data.append({"name": i["name"], "path": i["path"], "url": i["url"]})

                else:
                    pass         
            else:
                pass
            return format_response('ok',g.data)  

    except Exception as e:
        print((e.args))
        return format_response('error','图片列表加载失败')    
=======
# -*- coding: utf-8 -*-
# @Author: Landers
# @Github: Landers1037
# @File: image_list.py
# @Date: 2020-05-14


from app.api.img import img
from app.utils import format_response
from flask import request
from flask import g
from app import global_config

from app.utils import count_page
from app.database import database


@img.route('/api/image_list')
def image_list():
    #支持按需获取图片列表 用于前端的懒加载
    token = request.args.get('token')
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
        mail = database().get(global_config.engine, 'token', token)
        if mail:
            #仅获取当前用户下的图片列表
            if global_config.engine == 'sqlite':
                img_list = database().get_image_list(global_config.engine,mail)
                for i in img_list:
                    g.data.append(i.info())

            elif global_config.engine == 'mongo':
                img_list = database().get_image_list(global_config.engine, mail)
                for i in img_list:
                    g.data.append({"name": i["name"], "path": i["path"], "url": i["url"]})

            else:
                pass         
        else:
            pass
        return format_response('ok',g.data)  
   
>>>>>>> 82249f551dc1b0b7f3404782bc29efd70c88a15a
