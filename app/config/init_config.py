# @Author: Landers1037
# @Github: github.com/landers1037
# @File: init_config.py
# @Date: 2020-05-12

import json
import os


def init_config():
    path = os.path.join(os.getcwd(), 'config.json')
    data = {
        "port": 5000,
        "debug": True,
        "server_name": None,  # 比较特殊的配置，默认应用绑定的域名，本地测试时应当忽略
        "multiroutine": False,
        "server": {
            "image_path": '',
            "image_size": 10*1024*1024,
            "image_url": '',
            "image_rule": 'base64',
            "image_zip": False,
            "image_zip_path": ''
        },
        "database": {
            "engine": 'sqlite',
            "sqlite": 'sqlite:///test.db',
            "mongo": ''
        }
    }
    with open(path, 'w', encoding='utf-8')as f:
        try:
            json.dump(data, f, ensure_ascii=False, indent=2)
        finally:
            f.close()
