<<<<<<< HEAD
# -*- coding: utf-8 -*-
# @Author: Landers
# @Github: Landers1037
# @File: flask_config.py
# @Date: 2020-05-14

# flask的配置对象格式
from .read_config import read_config
from .check_config import check_config

# 一个可以实例化解析为配置对象的类
# 这里有一个顺序问题，flask优先加载这里的配置文件，那么init配置步骤就在这里进行


class flask_config:
    check_config()
    raw_config = read_config()
    DEBUG = raw_config.debug
    SQLALCHEMY_DATABASE_URI = raw_config.sqlite
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = 'This is a Secret Key'
    SERVER_NAME = raw_config.server_name
    MAX_CONTENT_LENGTH = raw_config.image_size
    MONGO_DBNAME = 'mongo_mgekimghost'
    MONGO_URI = 'mongodb://localhost:27017/mgek_imghost'
    MONGO_HOST = 'localhost'
    MONGO_PORT = 27017
    MONGO_USERNAME = None
    MONGO_PASSWORD = None
    ERROR_LOG_DIR = "error_log"
    JWT = True
    MAIL_HOST = 'smtp.163.com'
    MAIL_PORT = 465
    MAIL_USER = 'yourmail@163.com'
    MAIL_PASS = 'mail_password'

=======
# -*- coding: utf-8 -*-
# @Author: Landers
# @Github: Landers1037
# @File: flask_config.py
# @Date: 2020-05-14

# flask的配置对象格式
from .read_config import read_config
from .check_config import check_config

# 一个可以实例化解析为配置对象的类
# 这里有一个顺序问题，flask优先加载这里的配置文件，那么init配置步骤就在这里进行


class flask_config:
    check_config()
    raw_config = read_config()
    DEBUG = raw_config.debug
    SQLALCHEMY_DATABASE_URI = raw_config.sqlite
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = 'This is a Secret Key'
    SERVER_NAME = raw_config.server_name
    MAX_CONTENT_LENGTH = raw_config.image_size
    MONGO_DBNAME = 'mongo_mgekimghost'
    MONGO_URI = 'mongodb://localhost:27017/mgek_imghost'
    MONGO_HOST = 'localhost'
    MONGO_PORT = 27017
    MONGO_USERNAME = None
    MONGO_PASSWORD = None
    JWT = True
    IP_FILTER = True
    RULE = '10/60'
    MAIL_HOST = 'smtp.163.com'
    MAIL_PORT = 465
    MAIL_USER = 'user@163.com'
    MAIL_PASS = 'pass'

>>>>>>> 82249f551dc1b0b7f3404782bc29efd70c88a15a
