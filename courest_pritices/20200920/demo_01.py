#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: demo_01.py
# @time: 2020/9/20 9:32 上午

import requests


# response 响应对象 （响应行、响应头、响应正文）
response = requests.get(url='http://www.hnxmxit.com/')  # get()方法模拟发送get请求
print( response.url )

# 获取响应正文有两种方式
# 方式一
# print( response.content.decode('utf-8') )  # decode 解码

# 方式二
response.encoding = 'utf-8'
print( response.text )