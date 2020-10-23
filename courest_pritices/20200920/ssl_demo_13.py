#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: ssl_demo_13.py
# @time: 2020/9/20 3:25 下午

import requests
import warnings
import urllib3


# response = requests.get('https://www.12306.cn')
# print( response.content.decode('utf-8') )

# https 必须带证书操作 处理方式一： 不验证证书,报警告,返回200
#解决方案一：（废弃）
# from requests.packages import urllib3   # 老版本 request 2.6.0
# urllib3.disable_warnings()

# 解决方案二： 新版本
# requests.packages.urllib3.disable_warnings()
# warnings.filterwarnings("ignore")
# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# response = requests.get('https://www.12306.cn',verify=False)
# print( response.content.decode('utf-8') )

# 方式二：安装pyopenssl模块 安装之后就不会报错
# pip install -U requests[security]
# response = requests.get('https://www.12306.cn')

# 方式三：加上证书  公司内部 开发同事要  ****.crt
respone=requests.get('https://www.12306.cn', cert=('/path/server.crt', '/path/key'))

