# -*- coding: utf-8 -*-
# @Author: Landers
# @Github: Landers1037
# @File: __init__.py
# @Date: 2020-05-16

#用于认证用户的api接口

from flask import Blueprint
from flask_cors import CORS


auth = Blueprint('auth_api', __name__)
CORS(auth)

from . import get_token
from . import db_init