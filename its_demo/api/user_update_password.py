import requests
from its_demo.comm.url_info import urlinfo
from its_demo.api.login import Login_info
from its_demo.api.user_list import User_list
from its_demo.comm.md5_password import get_md5_password

u_ids = User_list()
u_id= u_ids.get_user_id()
usertoken=Login_info()
md5_password = get_md5_password()
 # 修改密码
post_params = {
     "newPassword": md5_password,
     "password": md5_password
        }
header_param = {
     "Content-Type": "application/json",
      "token": usertoken.get_token()
        }

response = requests.post(url='%s/user/update-password' % urlinfo.url_hostname_info(),
                         json=post_params,
                          headers=header_param
                                 )
print(response.text)
