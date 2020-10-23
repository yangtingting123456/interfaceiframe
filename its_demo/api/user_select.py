import requests
from its_demo.comm.url_info import urlinfo
import jsonpath
from its_demo.api.login import Login_info
from its_demo.api.user_list import User_list

u_ids = User_list()
u_id= u_ids.get_user_id()
usertoken=Login_info()

# 用户下拉列表接口
class User_select():

    def get_user_select(self):
        user_info_params ={
            "departmentId":"1",
            "companyId":"1"
        }
        header_params = {
            "token": usertoken.get_token()
        }
        response = requests.get(url='%s/user/select' % urlinfo.url_hostname_info(),
                                headers=header_params,
                                params = user_info_params
                                )
        # 将登录接口返回的数据转换成json
        json_obj = response.json()
        # 提取登录接口返回的数据token
        user_id = jsonpath.jsonpath(json_obj, '$.data.id')
        return json_obj

user_info = User_select()
print(user_info.get_user_select())