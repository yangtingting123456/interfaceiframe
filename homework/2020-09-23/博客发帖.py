import requests
import re

s = requests.session() #开启一个会话Session
#登录接口
heads_params ={
    "Accept":"application/json, text/plain, */*",
    "X-Requested-With":"XMLHttpRequest",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0",
    "Referer":"https://account.cnblogs.com/signin?returnUrl=https:%2F%2Fhome.cnblogs.com%2Fu%2Ftingting-yang"
}
res = s.get(url='https://account.cnblogs.com/api/sign-in',
                   verify=False,
                   headers = heads_params)
cks = res.cookies
XSRFTOKEN = re.findall('XSRF-TOKEN=(.+) for account.cnblogs.com/>]>',str(cks))[0]
print(XSRFTOKEN)
#设置cookies
s.cookies.set('.Cnblogs.AspNetCore.Cookies','CfDJ8AHUmC2ZwXVKl7whpe9_laur97Xhaf0nvjmKr7zD1Uk0pm2kx5Rk1h5gM9anuqwcxSo_4QdmmBMrsf1a4kjk0sksQN4gYAyL4_z7Z0JZd--TZsYp7SbLXjXFjVSGjl91AS7B-2xCipX3EEPNWyo7xtfmcY9lTIysQ8vRongWmrs_Ei_3poWpwYOWvQFo3B8EXNkYMHT21fNiRJ32yVaQ1BXVOGJpcUC2_kF0DvGOT7dw7lIIxtRSS6TdPnmrwKd61XkK6u05t_Ar_X_6VK8vmMwQd_UUAKqUWve3PT_-4o4ZOG8MRfq6KoBEOd1tIpQaYY5Dkwimaki85ZuE8zK9QFoU-Amc8eyoWC2VpgT4w8iE35WFLthB-3qZoy-2_UunuAVaMhywprq6hiPrHdyBWu1mW3v6NGb8vwvnf7C9vaTNkKu2ybkJOqYs9tPiqSw39lJOootLsksdwnObL8RW0QUZa-tV5yjRLCJoqCPvUVfgrx7pLCoIf0yrjdRs8-TdtW7MTq6R5WIxoouG1e_gCxAjwuhTSmjVIbp3kcYkK833Nc2rq0rTMqsh8zxb2Z9krQ',path='/',domain='.cnblogs.com')
s.cookies.set('.CNBlogsCookie','06E3EE2B4F9EBCF302D0F4982D9DC3D4BDDAF908FC87925C39353E7C4D2FBB9CAD1C34651DD5D460C91DEAE38888535820932F2AFED1CC82F60F892F8CF25F6959E4F36106FCAB8954E72EFDE46D8863F24BB916E0CFB208FE35DDB8DA2C12AF84AEFBB1',path='/',domain='.cnblogs.com')
s.cookies.set('__gads','ID=9f6cc12696f6f9ac-227709569ac3007f:T=1600670516:S=ALNI_MYRNQsBjICBAdw1QyScXRQ-_ja3jg',path='/',domain='.cnblogs.com')
s.cookies.set('UM_distinctid','17511c9c5afa-06bbeaba1e4cc2-4c3f247a-1fa400-17511c9c5b16f',path='/',domain='.cnblogs.com')

heads_infos ={
    "Accept":"application/json, text/plain, */*",
    "X-Requested-With":"XMLHttpRequest",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0",
    "Referer":"https://account.cnblogs.com/signin?returnUrl=https:%2F%2Fhome.cnblogs.com%2Fu%2Ftingting-yang",
    "Content-Type":"application/x-msgpack"

}
res = s.post(
    url='https://account.cnblogs.com/api/sign-in?returnUrl=https:%2F%2Fhome.cnblogs.com%2Fu%2Ftingting-yang',
    verify=False,
    headers = heads_infos,
    cookies=cks


                   )
print(res.content.decode('utf-8'))