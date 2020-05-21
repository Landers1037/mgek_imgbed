<<<<<<< HEAD
# -*- coding: utf-8 -*-
# @Author: Landers
# @Github: Landers1037
# @File: db_init.py
# @Date: 2020-05-14

from app import db
from app.api.auth import auth
from app.utils import format_response

@auth.route('/api/init_db',methods=['POST'])
def init_db():
    try:
        db.create_all()
        return format_response('ok','database init success')
    except:
        return format_response('error','database init failed')
=======
# -*- coding: utf-8 -*-
# @Author: Landers
# @Github: Landers1037
# @File: db_init.py
# @Date: 2020-05-14

from app import db
from app.api.auth import auth
from app.utils import format_response

@auth.route('/api/init_db',methods=['POST'])
def init_db():
    db.create_all()
    return format_response('ok','database init success')

        
>>>>>>> 82249f551dc1b0b7f3404782bc29efd70c88a15a
