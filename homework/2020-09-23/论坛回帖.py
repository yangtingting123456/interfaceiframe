# 1、用 charles+requests 完成论坛的登录、发帖实战
import requests
import re
from collections import OrderedDict

# 获取csrf_token
host = "http://47.107.178.45"
ses = requests.session()
response = ses.get(url='%s/phpwind/'%host)
body = response.content.decode('utf-8')
csrf_token = re.findall('name="csrf_token" value="(.+?)"/>',body)[0]

#登录
login_params={
    "username":"test01",
    "password":"123456",
    "csrf_token":csrf_token,
    "csrf_token":csrf_token
}
header_info = {
    "Accept":"application/json, text/javascript, */*; q=0.01",
    "X-Requested-With":"XMLHttpRequest",
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
    "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"
}
response_login = ses.post(
    url = '%s/phpwind/index.php?m=u&c=login&a=dologin'%host,
    data = login_params,
    headers =header_info
)
body =response_login.content.decode('utf-8')
statu_id = re.findall('&_statu=(.+?)",',body)[0]

#欢迎登录
get_data_dict={
    "m":"u",
    "c":"login",
    "a":"welcome",
    "_statu":statu_id
}
response = ses.get(url='%s/phpwind/index.php'%host,
                   params=get_data_dict)
import random
def random_str(digits=True, lowercase=True, uppercase=True, symbol=True, slen=10):
    seed = ''
    seed = seed + '1234567890' if digits else seed+''
    seed = seed + 'abcdefghijklmnopqrstuvwxyz' if lowercase else seed + ''
    seed = seed + 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' if uppercase else seed + ''
    seed = seed + '!@#$%^&*()_+=-' if symbol else seed + ''
    if len(seed)==0:
        return None
    sa = []
    for i in range(slen):
      sa.append(random.choice(seed))
    return ''.join(sa)
str=random_str()
#发帖
form_data = OrderedDict(
    [
        ("atc_title",(None,str)),
       ("atc_content",(None,str)),
        ("pid",(None,'')),
        ("tid",(None,'92506')),
        ("special",(None,'')),
        ("reply_notice",(None,'1')),
        ("csrf_token",(None,csrf_token))
    ]
)

response_ft = ses.post(
    url = '%s/phpwind/index.php?c=post&a=doreply&_json=1&fid=81'%host,
    files = form_data
                       )
print( response.content.decode('utf-8') )

