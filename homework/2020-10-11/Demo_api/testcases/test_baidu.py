# 1、利用requests模拟打开百度首页，并能通过正则随机取 左上角 新闻、hao123、地图、视频、贴吧、学术中的一个字符串进行输出
import requests
import re
import unittest

class TestBaiDu(unittest.TestCase):
    def setUp(self) -> None:
        self.session = requests.session()

    def tearDown(self) -> None:
        self.session.close()
    def testbaidu(self):
        s = requests.session()  # 开启一个会话Session
        headres_params = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0",
            "Upgrade-Insecure-Requests": "1",
            "Accept-Encoding": "gzip, deflate, br"
        }

        response = s.get(
            url='https://www.baidu.com/?',
            verify=False,
            headers=headres_params
        )

        body = response.content.decode('utf-8')
        # print(body)
        links = re.findall('class="mnav c-font-normal c-color-t">(.+?)</a>', body)
        for i in links:
            print(i)


