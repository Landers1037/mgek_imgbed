# -*- coding: utf-8 -*-
# @Author: Landers
# @Github: Landers1037
# @File: generate_time.py
# @Date: 2020-05-16

#图片添加日期的处理函数

import time


def generate_time():
    local = int(time.time())
    local_format = time.strftime('%Y-%m-%d', time.localtime(local))

    return [local,local_format]

