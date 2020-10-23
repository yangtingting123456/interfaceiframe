#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: proxy_demo_09.py
# @time: 2020/9/20 2:31 下午

import requests

proxy_server = {'http':'http://127.0.0.1:8888',
                'https':'http://127.0.0.1:8888'}

proxy_user_pasword = {
    'https':'http://username:password@127.0.0.1:8888'
}

response = requests.get(url='http://www.hnxmxit.com/',
                        proxies=proxy_server)  # 代理配置

print( response.status_code )

