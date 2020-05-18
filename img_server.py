# @Author: Landers1037
# @Github: github.com/landers1037
# @File: img_server.py
# @Date: 2020-05-12

#基于rest的图床api测试版
#基于纯Flask实现

from app import create_app
from gevent.pywsgi import WSGIServer

application = create_app(mode='dev')

if __name__ == '__main__':
    #基于运行模式提供基于gevent的异步支持
    from app import global_config
    run_mode = global_config.multiroutine
    if run_mode:
        #using gevent
        http_server = WSGIServer(('',global_config.port),application)
        http_server.serve_forever()

    else:
        #usually using in dev    
        application.run(port=global_config.port)