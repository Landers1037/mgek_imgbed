# @Author: Landers1037
# @Github: github.com/landers1037
# @File: read_config.py
# @Date: 2020-05-12

import json
import os

# 避免每次调用的时候都有io操作，把数据存储在全局变量里
# 映射为类


class Config:
    def __init__(self, port, debug, server_name, multiroutine, server, database):
        self.port = port  # 通用配置
        self.debug = debug
        self.server_name = server_name
        self.multiroutine = multiroutine
        self.get_server(server)  # 服务器配置
        self.get_database(database)  # 数据库配置

    def get_server(self, server):
        self.image_path = set_default_config(
            server, 'image_path', '')  # 图片保存位置
        self.image_size = set_default_config(
            server,'image_size',10*1024*1024
        )    
        self.image_url = set_default_config(
            server, 'image_url', '')  # 图片的服务器地址
        self.image_rule = set_default_config(
            server, 'image_rule', 'base64')  # 图片hash的命名方式
        self.image_zip = set_default_config(
            server, 'image_zip', False)  # 是否使用图片压缩，即生成缩略图
        self.image_zip_path = set_default_config(
            server, 'image_zip_path', '')  # 图片缩略图的存储位置
            
    def get_database(self, database):
        self.engine = set_default_config(
            database, 'engine', 'sqlite')  # 使用sqlite或mongodb
        self.sqlite = set_default_config(database, 'sqlite', 'sqlite:///test.db')  # sqlite的地址
        self.mongo = set_default_config(database, 'mongo', '')  # MongoDB地址

    def __repr__(self):
        return 'mgekimg_bed config Object'

    def __call__(self, *args, **kwargs):
        return {
            "port": self.port,
            "debug": self.debug,
            "multiroutine": self.multiroutine,
            "server": {
                "image_path": self.image_path,
                "image_url": self.image_url,
                "image_rule": self.image_rule,
                "image_zip": self.image_zip,
                "image_zip_path": self.image_zip_path
            },
            "database": {
                "engine": self.engine,
                "sqlite": self.sqlite,
                "momgo": self.mongo
            }
        }


def read_config(conf=None):
    if conf:
        # 按照键获取值
        with open(conf, 'r', encoding='utf-8')as f:
            config = json.load(f)
            pass
    else:
        try:
            path = os.path.join(os.getcwd(), 'config.json')
            with open(path, 'r', encoding='utf-8')as f:
                config = json.load(f)
                c = Config(
                    port=config["port"],
                    debug=config["debug"],
                    server_name=set_default_config(
                        config, 'server_name', None),
                    multiroutine=config["multiroutine"],
                    server=config["server"],
                    database=config["database"]
                )
                return c
        except:
            return None

# 为防止配置文件的读取缺失 添加默认的配置项


def set_default_config(config, name, value):
    try:
        return config[name]
    except:
        return value
