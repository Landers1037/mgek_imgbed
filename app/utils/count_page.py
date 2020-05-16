# -*- coding: utf-8 -*-
# @Author: Landers
# @Github: Landers1037
# @File: count_page.py
# @Date: 2020-05-15

#图片列表的分页数计算

def count_page(all: int,page: int):
    if all <= page:
        return 1
    else:
        p = all // page
        t = all - p
        if t > 0:
            return p + 1
        else:
            return p         