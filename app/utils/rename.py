# -*- coding: utf-8 -*-
# @Author: Landers
# @Github: Landers1037
# @File: rename.py
# @Date: 2020-05-14

# 核心的防止重复命名函数，使用两种方式为文件命名
# 使用base64编码图片的方式和md5hash方式

# 通过配置文件选择重命名方式，默认为b64

from app import global_config
from flask import jsonify
from base64 import b64encode
from hashlib import md5
import time


def rename(file_name: str):
    rule = global_config.image_rule
    time_now = str(time.time())
    file_name = file_name.lower() #小写处理
    if rule == 'base64':
        ext = access_ext(file_name)
        return b64encode((file_name + time_now).encode('utf-8')).decode('utf-8') + ext

    elif rule == 'md5':
        ext = access_ext(file_name)
        new = md5()
        new.update((file_name + time_now).encode('utf-8'))
        return new.hexdigest() + ext

    else:
        # using default base64
        ext = access_ext(file_name)
        return b64encode((file_name + time_now).encode('utf-8')).decode('utf-8') + ext

def access_ext(name):
    #用于扩展名称的获取
    ALLOW_SET = ['jpg', 'jpeg', 'png', 'webp', 'gif']
    li = name.split('.')
    if  len(li) > 1 and li[-1] in ALLOW_SET:
        return "." + li[-1] #返回扩展名

    else:
        #不合法的文件默认保存为无扩展的文件
        #还需要在前端做文件类型的判断
        return ''
