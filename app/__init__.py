# @Author: Landers1037
# @Github: github.com/landers1037
# @File: __init__.py.py
# @Date: 2020-05-12

from flask import Flask
from app.config import *
from flask_sqlalchemy import SQLAlchemy
from flask_pymongo import PyMongo

#初始时会默认初始化数据库连接，根据engine的配置选择配置的数据库
db = SQLAlchemy()
mongo = PyMongo()
global_config = None


def create_app(mode=None):
    application = Flask(__name__, static_url_path='/images', static_folder='../images')

    check_config()
    global global_config
    global_config = read_config()

    if mode == 'dev' or global_config.debug:
        application.debug = True
    application.config.from_object(flask_config())

    #对数据库连接添加错误判断
    if global_config.engine == 'sqlite':
        db.init_app(application)

    elif global_config.engine == 'mongo':    
        mongo.init_app(application)
    else:
        db.init_app(application)

        
    from .api.img import img
    from .api.auth import auth
    from .api.sys import sys
    application.register_blueprint(img)
    application.register_blueprint(auth)
    application.register_blueprint(sys)


    return application
