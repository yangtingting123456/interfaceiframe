#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: redir_demo_11.py
# @time: 2020/9/20 3:01 下午

# 重定向 请求和响应的时候 响应状态码为 3**

import requests

respnse = requests.get('http://www.360buy.com')
print( respnse.history ) # 显示请求的重定向信息
print( respnse.url )  # 显示请求的链接
print( respnse.content.decode('utf-8') )
# requests 在发送请求的时候，会进行自动重定向处理  不需要你干预
print('**********************************')

respnse1 = requests.get('http://www.360buy.com',allow_redirects=False)
print( respnse1.history ) # 显示请求的重定向信息
print( respnse1.url )  # 显示请求的链接
print( respnse1.content.decode('utf-8') )