#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: vx_demo_16.py
# @time: 2020/9/20 4:35 下午

import requests
import jsonpath

hosts = 'https://api.weixin.qq.com'

get_param_dict = {
    "grant_type":"client_credential",
    "appid":"wx55614004f367f8ca",
    "secret":"65515b46dd758dfdb09420bb7db2c67f"
}

response = requests.get(url = '%s/cgi-bin/token'%hosts,
                        params = get_param_dict)
json_obj = response.json()
token_id = jsonpath.jsonpath(json_obj,'$.access_token')[0]  # 接口依赖、接口关联

get_param_dict1 = {
    "access_token":token_id
}
post_data = {   "tag" : {     "name" : "guangzhoup3p4"   } }
response1 = requests.post(url='%s/cgi-bin/tags/create'%hosts,
                          params=get_param_dict1,
                          json=post_data)
json_obj_1 = response1.json()
create_tag_id = jsonpath.jsonpath( json_obj_1,'$.tag.id' )[0]
# print( type(create_tag_id),create_tag_id )

post_data1 = {   "tag" : {     "id" : create_tag_id,     "name" : "guangzhouren"   } }

response2 = requests.post(url="%s/cgi-bin/tags/update"%hosts,
                          params=get_param_dict1,
                          json=post_data1)
print( response2.json() )

