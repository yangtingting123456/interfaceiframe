import requests
from its_demo.comm.url_info import urlinfo
import jsonpath
from its_demo.api.login import Login_info

usertoken=Login_info()

# 通过用户列表接口获取某个用户的id
class User_list():
    def get_user_id(self):
        header_params = {
            "token": usertoken.test_gettoken()
        }
        response = requests.get(url='%s/user/info' % urlinfo.url_hostname_info(),
                                headers=header_params
                                )
        # 将登录接口返回的数据转换成json
        json_obj = response.json()
        # 提取登录接口返回的数据token
        user_id = jsonpath.jsonpath(json_obj, '$.data.id')
        return user_id[0]

user_id = User_list()


