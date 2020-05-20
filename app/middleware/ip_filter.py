# -*- coding: utf-8 -*-
# @Author: Landers
# @Github: Landers1037
# @File: ip_filter.py
# @Date: 2020-05-19

#ip地址过滤器
#运行原理 获取传来的IP地址在全局的hash表里找到对应ip，根据ip地址计数器和时间判断是否禁止访问
import time
from flask import abort
from app import global_ip

global_ip = {
    "127.0.0.1": {
        "last_time": 0，#这应该是一个时间变量默认time.time() 
        "count": 0 ,#一个IP计数器，记录当前IP地址的访问次数
        "next_time": 0 #time.time()类型，下一次允许访问的时间
    }
}

def abort():
    #用于禁止访问的函数，你直接调用此函数禁止访问即可 无需实现
    #调用方式
    #return abort()
    pass

def ip_filter(ip_address,rule):
    #ip_address地址 在global_ip里获取其值
    #rule 用于过滤的规则，形如10/60代表10次每60秒
    #使用split方式获取rule的两个值，前一个代表次数，后一个代表间隔时间单位秒
    if ip_address not in global_ip:
        global_ip[ip_address]['last_time'] = 0
        global_ip[ip_address]['count'] = 0
        global_ip[ip_address]['next_time'] = 0
 
    global_ip[ip_address]['count'] += 1       
    last_time = global_ip[ip_address]['last_time'] 
    count = global_ip[ip_address]['count']
    next_time = global_ip[ip_address]['next_time']
    
    try:
        max_times, interval = rule.split('/')    
    except Exception as e:
        print(e)
            
        
    #对ip地址进行判断，获取当前的系统时间，与字典里ip对应的时间比较，
    #比较count的值 lasttime的值 如果当前时间-last_time < rule规定时间，并且count >= rule规定则abort
    #如果IP地址被禁止以后，更新一个next_time变量为下一次可以访问的时间，当前时间+5分钟
    time1 = time.time()
    if time1 < next_time:
        return abort()
    if time1-last_time<int(interval) and count>=int(max_times):
        global_ip[ip_address]['last_time'] = 0
        global_ip[ip_address]['count'] = 0
        global_ip[ip_address]['next_time'] = time1 + 300
        return abort()