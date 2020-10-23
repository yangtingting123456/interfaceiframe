#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: demo_02.py
# @time: 2020/9/20 9:54 上午

import requests
# get请求携带参数
# https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=APPID&secret=APPSECRET
# https:   协议类型  api.weixin.qq.com：主机地址   /cgi-bin/token 请求地址
# grant_type=client_credential&appid=APPID&secret=APPSECRET  参数  参数之间用&分割的

# 方式一：
# response = requests.get(url='https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=wx55614004f367f8ca&secret=65515b46dd758dfdb09420bb7db2c67f')
# print( response.content.decode('utf-8') )

# 方式二：
get_param_dict={
    "grant_type":"client_credential",
    "appid":"wx55614004f367f8ca",
    "secret":"65515b46dd758dfdb09420bb7db2c67f"
}

response = requests.get( url='https://api.weixin.qq.com/cgi-bin/token',
                         params=get_param_dict,verify=False)
print( response.content.decode('utf-8') )


