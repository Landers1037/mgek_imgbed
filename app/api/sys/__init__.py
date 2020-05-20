# -*- coding: utf-8 -*-
# @Author: Landers
# @Github: Landers1037
# @File: __init__.py
# @Date: 2020-05-19

from flask import Blueprint
from flask_cors import CORS


sys = Blueprint('img_sys', __name__)
CORS(sys)

from . import get_config