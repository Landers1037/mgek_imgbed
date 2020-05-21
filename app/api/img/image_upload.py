# @Author: Landers1037
# @Github: github.com/landers1037
# @File: image_upload.py
# @Date: 2020-05-12

# 普通的图片处理api
from app.api.img import img
from app import global_config
from flask import redirect, request, abort
from app.utils import rename,format_response,generate_time
import os
from app.database import database


#定义允许的文件类型
#保存文件时的名称是做小写处理的，不必考虑名称问题
ALLOW_SET = ['jpg','jpeg','png','webp','gif'] 

@img.route('/api/image_upload',methods=['POST'])
def image_upload():
    #保持一个上下文的命名变量
    #默认的文件列表是file，这应该与前端保持同步
    #没有使用安全命名的方式，因为所有文件名会经过hash计算后重命名
    #默认需要登录认证
    token = request.args.get("token")
    files = request.files.getlist('file')
    path = global_config.image_path if global_config.image_path != '' else os.path.join(os.getcwd(),"images")

    if token and database().get(global_config.engine,'token',token):
        #账户存在
        if not os.path.exists(path):
            os.mkdir(path)
            #保证目录的创建
            #判断是否有上传文件
        if 'file' not in request.files:
            return format_response('error', '空的上传文件')
        else:
            res = database().get(global_config.engine, 'token', token)
            for f in files:
                if f.filename:
                    name = rename.rename(f.filename)
                    f.save(os.path.join(path, name))

                    #数据库操作
                    res = database().set(global_config.engine, 'image',
                                        {"name": name, "mail": res, "path": os.path.join(path, name),
                                        "url": "{}{}".format(global_config.image_url, name),
                                        "time": generate_time()[0]
                                    })
                    if res:
                        pass
                    else:
                        return format_response('error', '文件上传失败')

            return format_response('ok', '文件上传成功')

    else:
        return format_response('error', '无文件上传权限')
