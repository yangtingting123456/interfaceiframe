#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: exception_demo_14.py
# @time: 2020/9/20 4:05 下午

import requests
from requests.exceptions import MissingSchema, RequestException

try:
    response = requests.get(url='www.baidu.com')
except MissingSchema as e:
    print('https/http前缀没加')
except ConnectionError as e:
    print('链接超时')
except RequestException as e:
    print( '请求异常' )