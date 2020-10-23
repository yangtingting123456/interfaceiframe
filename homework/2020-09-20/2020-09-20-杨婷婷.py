# 1、charles 的 三种过滤方式操作截图做成文档
#见charles四种过滤数据文档

# 2、charles 抓取 论坛 注册 、发帖数据，截图抓到了请求即可

# 3、requests 编写脚本 实现获取access_token、增加标签接口、实现查询标签接口、实现删除标签接口
# 用的公司项目做的，登录（获取token，密码md5加密）-获取用户列表-用户更新，详情，-退出等；

# 4、requests 模拟 https://www.qq.com的请求，用re模块截取出
# <meta name="description" content="(.+?)" />中的content内容
# import requests
# import re
#
# response = requests.get(url='https://www.qq.com' )
# body = response.content.decode('gbk')
# # print(body)
# content = re.findall(' <meta name="description" content="(.+?)" /> ',body)
# print(content)
import re
import requests

response = requests.get(url='https://www.qq.com')
body = response.content.decode('gbk')
# print(body)
con = re.findall(' name="description" content="(.+?)"',body)
print( con )