# @Author: Landers1037
# @Github: github.com/landers1037
# @File: __init__.py.py
# @Date: 2020-05-12

from flask import Flask
from app.config import *
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
global_config = None


def create_app(mode=None):
    application = Flask(__name__)

    check_config()
    global global_config
    global_config = read_config()

    if mode == 'dev' or global_config.debug:
        application.debug = True
    application.config.from_object(flask_config())


    db.init_app(application)
    from .api import api
    application.register_blueprint(api)


    return application
