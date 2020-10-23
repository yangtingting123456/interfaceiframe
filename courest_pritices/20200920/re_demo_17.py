#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: re_demo_17.py
# @time: 2020/9/20 5:01 下午

import re

# 正则表达式模块  1、字符模版的含义  2、方法太杂

# 写法一：利用re模块的函数去匹配
source_str = 'python3classggfdgfdgfderewrwe'
value = re.search( 'python\d',source_str ).group()
print( value )

#写法二：利用正则表达式对象处理
reg_obj = re.compile('python\d')
value1 = reg_obj.search(source_str).group()
print( value1 )

title_str = '<title>新梦想_软件测试培训_Java培训_Python培训_长沙新梦想IT教育</title>'
reg_obj_01 = re.compile('t+')
result = reg_obj_01.findall(title_str)
print( result )

result1 = re.findall('<title>(.+?)</title>',title_str)[0]
print( result1 )







