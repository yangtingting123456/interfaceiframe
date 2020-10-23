import requests
from its_demo.comm.url_info import urlinfo
from its_demo.api.login import LoginInfo
from its_demo.api.user_list import User_list
from its_demo.comm.md5_password import get_md5_password

u_ids = User_list()
u_id= u_ids.get_user_id()

md5_password = get_md5_password()
 # 修改密码
post_params = {"id":"1","name":"admin","mobile":"15173661874","wechat":"aaaa","email":"tingting.yang@juneyaokc.com","status":"1","jobNumber":"12as323","address":"a2aaa","jobTypeId":"2","jobId":"1","realName":"aaaAAA",
               "companyId":"1","departmentId":"1","company":"上海均瑶集团有限公司","department":"市场部","jobType":"sxx","job":"aaasa"}

header_param = {
     "Content-Type": "application/json",
      "token": LoginInfo.test_gettoken()
        }

response = requests.post(url='%s/user/update' % urlinfo.url_hostname_info(),
                         json=post_params,
                          headers=header_param
                                 )
print(response.text)
