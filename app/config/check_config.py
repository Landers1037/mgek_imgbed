# @Author: Landers1037
# @Github: github.com/landers1037
# @File: check_config.py
# @Date: 2020-05-12

import os
from .init_config import init_config

def check_config():
    """
    用于生成默认的配置文件
    :return:
    """
    if not os.path.exists(os.path.join(os.getcwd(), 'config.json')):
        init_config()
    else:
        pass