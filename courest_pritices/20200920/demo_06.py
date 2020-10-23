#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: demo_06.py
# @time: 2020/9/20 11:35 上午

import os
import requests
import httpx

# post 上传文件

current_path = os.path.dirname(__file__)
excel_path = os.path.join( current_path ,'..','data','testdata.xlsx' )
# excel_path = current_path + '/../data/testdata.xlsx'

excel_file = {'file': open(excel_path,'rb') }
response = requests.post(
    url='http://httpbin.org/post',
    files=excel_file
)
print( response.content.decode('utf-8') )

