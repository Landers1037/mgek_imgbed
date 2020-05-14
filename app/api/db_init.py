from app import db
from app.api import api
from app.utils import format_response

@api.route('/api/init_db',methods=['POST'])
def init_db():
    try:
        db.create_all()
        return format_response('ok','database init success')
    except:
        return format_response('error','database init failed')