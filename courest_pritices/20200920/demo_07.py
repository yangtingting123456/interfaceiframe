#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: demo_07.py
# @time: 2020/9/20 11:47 上午

import requests
import json

response = requests.get(url='http://www.hnxmxit.com/')

#响应行  响应状态码  响应信息  协议版本
print( response.status_code )  # 200
print( response.reason ) # OK

# 响应头
print( response.headers )  #所有的响应头  { ... }
print( response.headers['Server'] )
print( response.headers['Content-Encoding'] )

# 响应正文
# 方式一：
# response.encoding = response.apparent_encoding # 'utf-8'
# print( response.text )

# 方式二：二进制响应内容
# print( response.content.decode('utf-8') )

# 方式三：json方式

get_param_dict={
    "grant_type":"client_credential",
    "appid":"wx55614004f367f8ca",
    "secret":"65515b46dd758dfdb09420bb7db2c67f"
}

response = requests.get( url='https://api.weixin.qq.com/cgi-bin/token',
                         params=get_param_dict)
# r = response.content.decode('utf-8')
# print( type(r) )
# str_json = json.loads(r)
# print( type(str_json) )

print( response.json() )

# 方式四：  r.raw 查看原始响应
r = requests.get('https://www.baidu.com',stream=True)
print(r.raw.read(10))









