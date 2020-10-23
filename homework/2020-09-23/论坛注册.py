# 2、用 charles+requests 完成论坛的注册
import requests
import re
from collections import OrderedDict

# 获取csrf_token
host = "http://47.107.178.45"
ses = requests.session()
response = ses.get(url='%s/phpwind/'%host)
body = response.content.decode('utf-8')
csrf_token = re.findall('name="csrf_token" value="(.+?)"/>',body)[0]

#定义生成随机字符串函数
import random
def random_str(digits=True, lowercase=True, uppercase=True, symbol=True, slen=10):
    seed = ''
    seed = seed + '1234567890' if digits else seed+''
    seed = seed + 'abcdefghijklmnopqrstuvwxyz' if lowercase else seed + ''
    seed = seed + 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' if uppercase else seed + ''
    if len(seed)==0:
        return None
    sa = []
    for i in range(slen):
      sa.append(random.choice(seed))
    return ''.join(sa)
str=random_str()
print(str)

# 进行注册
post_params ={
    "username":str,
    "password":"user01122",
    "repassword":"user01122",
    "email":str+"@qq.com",
    "csrf_token":csrf_token
}

response = ses.post(
    url='%s/phpwind/index.php?m=u&c=register&a=dorun'%host,
    data = post_params

                    )
print(response.content.decode('utf-8'))

