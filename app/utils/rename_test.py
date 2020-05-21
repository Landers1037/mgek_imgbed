# -*- coding: utf-8 -*-
# @Author: Landers
# @Github: Landers1037
# @File: rename_test.py
# @Date: 2020-05-14

# rename test

from base64 import b64encode
from hashlib import md5
import time


def access_ext_test(name):
    #用于扩展名称的获取
    ALLOW_SET = ['jpg', 'jpeg', 'png', 'webp', 'gif']
    li = name.split('.')
    if len(li) > 1 and li[-1] in ALLOW_SET:
        return "." + li[-1]  # 返回扩展名

    else:
        #不合法的文件默认保存为无扩展的文件
        #还需要在前端做文件类型的判断
        return ''

if __name__ == "__main__":
    # time test
    time = str(time.time())
    print("time", time)

    # base64 test
    old = "test_base64_name"
    new = b64encode((old + time).encode('utf-8'))
    print(new.decode('utf-8'))

    # md5 test
    old = "test_md5_name"
    new = md5()
    new.update(((old + time).encode('utf-8')))
    print(new.hexdigest())

    #lower test
    print("test")
    print("teSt".lower())
    print('测试用例Test'.lower())
    
    print(access_ext_test('hello.jpg'))
