#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: demo_05.py
# @time: 2020/9/20 11:16 上午


import json
import requests

# requests 模拟发送post请求
url_param_dict = {
    "access_token":'37_Ek4AQ3pIzrUYfXzoUD3bpPBm5mXo4eyncOcgDvk2KJ3gnia4hr_iwUDhpbPFb09Jjuzh5J4XgCXfgzy_nWxyT3wBoENIinh-X6l26hmnvur-s7BXqhi5Jsu5oclaGzi9XQpnZZz340ODbGbRAUMgAIAMGY'
}
post_param_data = { "tag" : { "name" : "hunanP3P4"   } }

response = requests.post(url='https://api.weixin.qq.com/cgi-bin/tags/create',
                         params=url_param_dict,
                         # json=post_param_data
                         data = json.dumps( post_param_data )
                         )
print( response.content.decode('utf-8') )