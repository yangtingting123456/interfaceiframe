#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: re_demo_18.py
# @time: 2020/9/20 5:23 下午

import re
import requests

response = requests.get(url='http://www.hnxmxit.com/')
body = response.content.decode('utf-8')
print(body)
con = re.findall('property="qc:admins" content="(.+?)"',body)
print( con )

# for c in con:
#     print(c)


