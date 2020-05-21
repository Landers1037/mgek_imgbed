# @Author: Landers1037
# @Github: github.com/landers1037
# @File: __init__.py.py
# @Date: 2020-05-12


from flask import Blueprint
from flask_cors import CORS


img = Blueprint('img_api', __name__)
CORS(img)


from . import image_upload
from . import image_info
from . import image_list
from . import image_delete
from . import image_format

#add jwt
from app.middleware import jwt_middleware