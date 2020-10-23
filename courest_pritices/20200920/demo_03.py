#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: demo_03.py
# @time: 2020/9/20 10:35 上午

import requests
# get模拟请求头部信息
# https://www.baidu.com/s?wd=newdream

get_param_dict = {
    "wd":"newdream"
}

header_info_dict = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
}

response = requests.get(url='https://www.baidu.com/s',
                        params=get_param_dict,
                        headers=header_info_dict)

print( response.content.decode('utf-8') )