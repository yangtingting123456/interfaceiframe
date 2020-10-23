#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: timeout_demo_10.py
# @time: 2020/9/20 2:41 下午

import requests
import time

print( time.time() )  # 格林威治时间 20200920 - 19700101 秒数、毫秒数
response = requests.get( url = 'https://www.baidu.com', timeout=60 )  # 1s = 1000ms  259-83=176ms
print( time.time() )
# 特殊需求 ： 公司 系统之间 有心跳包 A -- B
# 3625 == 363ms  536 = 537  537-363 = 166ms
# 数值： folat  接收数据的时间设定
#  (0.1,0.2)  tuple  0.1代表连接超时，0.2代表接收数据的超时时间