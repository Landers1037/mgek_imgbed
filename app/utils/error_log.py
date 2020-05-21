# @Author: xk-wang
# @Github: github.com/xk-wang
# @File: error_log.py
# @Date: 2020-05-21

import logging
from app.utils import format_response
from flask import current_app
from flask import request
from functools import wraps
from datetime import datetime
import os

def log(f):
    @wraps(f)
    def wrapper(*args,**kwargs):
        try:
            response=f(*args,**kwargs)
            return response
        except Exception as e:
            log_dir=os.path.join(os.getcwd(),current_app.config['ERROR_LOG_DIR'])
            if not os.path.exists(log_dir):
                os.makedirs(log_dir)
            timestamp=datetime.now().strftime('%Y.%m.%d')
            logging.basicConfig(level=logging.ERROR,filename=os.path.join(log_dir,timestamp+".log"))
            logging.getLogger("werkzeug").setLevel(logging.WARNING)
            message='[{}] {} {} {}\n{}'.format(datetime.now().strftime('%Y/%m/%d %H:%M:%S'),
                                              request.method,request.url,f.__name__,e)
            logging.error(message)
            return format_response('error','发生了错误')
            
    return wrapper