#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: demo_04.py
# @time: 2020/9/20 11:05 上午

# 模拟post请求

import json

str_dict = {"name":"xiaoming","age":18,"sex":"男"}
print( type(str_dict) )

str1 = json.dumps( str_dict )  # 把字典、json对象转化为 字符串
print( type(str1) )
print( str(str1) )  # repr() 转化为字符串 方便程序阅读的显示  str() 方便用户阅读的显示

str2 = '{"name":"xiaoming","age":18,"sex":"男"}'
str_json = json.loads(str2)
print( type(str_json) )
print( str_json.get('sex') )   # str_json['sex']

