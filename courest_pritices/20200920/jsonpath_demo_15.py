#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: jsonpath_demo_15.py
# @time: 2020/9/20 4:22 下午

# pip install jsonpath

import json
import jsonpath   # json数据解析 从一个json体中取出你需要的字段数据过程

str1 = '{"name":"xiaoming","age":18,"sex":"男"}'
jsondata = json.loads(str1)
name = jsonpath.jsonpath(jsondata,'$.name')
print( name[0] )

str2 = '{"name":"xiaoming","age":18,"sex":"男","books":[{"bname":"朝花夕拾","price":45.5,"date":"2020-01-1"},{"bname":"呐喊","price":36.5,"date":"2020-01-03"}]}'
jsondata1 = json.loads( str2 )
price = jsonpath.jsonpath(jsondata1,'$.books[1].price')
print( price )



