# -*- coding: utf-8 -*-
# @Author: Landers
# @Github: Landers1037
# @File: __init__.py
# @Date: 2020-05-18

#日志记录器

#在这里导入封装的库

#函数例如
def logg(request,e,path):
    """
    request是请求对象，使用方式为request.url记录当前请求的地址
    e是catch的错误，调用为e.args
    path是日志保存的绝对路径，直接使用即可
    默认记录当前的时间，调用time.time()即可
    """
    #return 无需return
    #保存格式
    data = {
        "url": ,
        "error": ,
        "time": ,
    }
    save data