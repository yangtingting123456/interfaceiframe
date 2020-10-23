#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: cookie_demo_12.py
# @time: 2020/9/20 3:16 下午

import requests

# 在请求中添加cookie
# 方式一：
# cookie_dict = {"company_name":"newdream"}
# requests.get(url='http://www.hnxmxit.com/',
#              cookies = cookie_dict)

# 方式二：
header_info_dict = {
    'cookie':'company_name=newdream'
}
requests.get(url='http://www.hnxmxit.com/',
             headers = header_info_dict)