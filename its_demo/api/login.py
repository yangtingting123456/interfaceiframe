import requests
from its_demo.comm.url_info import urlinfo
import jsonpath
from its_demo.comm.md5_password import get_md5_password
import unittest
import re

# 登录接口，获取用户登录的token
md5_password = get_md5_password()

class Login_info():

    def test_gettoken(self):
        post_params = {
            "name": "admin",
            "password": md5_password
        }
        header_param = {
            "Content-Type": "application/json"
        }

        response = requests.post(url='%s/user/login' % urlinfo.url_hostname_info(),
                                 json=post_params,
                                 headers=header_param
                                 )
        body = response.json()
        code = body['code']
        user_token=body['data']['token']

        return user_token

LoginInfo=Login_info()












