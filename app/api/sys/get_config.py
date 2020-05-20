# -*- coding: utf-8 -*-
# @Author: Landers
# @Github: Landers1037
# @File: get_config.py
# @Date: 2020-05-19

#获取配置文件的路径
import os
from app.api.sys import sys

@sys.route('/api/get_config')
def get_config():
    path = os.path.join(os.getcwd(), 'config.json')
    
    return path
