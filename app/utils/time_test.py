# -*- coding: utf-8 -*-
# @Author: Landers
# @Github: Landers1037
# @File: time_test.py
# @Date: 2020-05-16

import time
import datetime

t = int(time.time())
local = time.localtime(t)
now = time.strftime('%H-%M-%S',local)
tmp = now.split('-')
res = int(tmp[0])*60*60 + int(tmp[1])*60 + int(tmp[2])
print(t,res)