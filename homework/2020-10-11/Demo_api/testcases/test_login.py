# 2、利用requests中的session以及cookie的设置功能，完成 免登录进行回帖操作

import requests
import re
from collections import OrderedDict
import unittest
class TestLogin(unittest.TestCase):
    def setUp(self) -> None:
        self.session = requests.session()
    def tearDown(self) -> None:
        self.session.close()

    def test_login(self):
        # 获取csrf_token
        host = "http://47.107.178.45"
        ses = requests.session()
        response = ses.get(url='%s/phpwind/' % host)
        body = response.content.decode('utf-8')
        csrf_token = re.findall('name="csrf_token" value="(.+?)"/>', body)[0]
        ses.cookies.set('zFb_winduser', 'Pvi55R1gVKSwAM%2FUXo1SpBZQkwqudcGMYbl67RRG5nPLi%2B2Fdic%2FGX5Xaqw%3D',
                        path='/', domain='47.107.178.45')
        ses.cookies.set('zFb_lastvisit', '1167%091602494044%09%2Fphpwind%2Findex.php%3Fc%3Dthread%26fid%3D81', path='/',
                        domain='47.107.178.45')

        import random
        def random_str(digits=True, lowercase=True, uppercase=True, symbol=True, slen=10):
            seed = ''
            seed = seed + '1234567890' if digits else seed + ''
            seed = seed + 'abcdefghijklmnopqrstuvwxyz' if lowercase else seed + ''
            seed = seed + 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' if uppercase else seed + ''
            seed = seed + '!@#$%^&*()_+=-' if symbol else seed + ''
            if len(seed) == 0:
                return None
            sa = []
            for i in range(slen):
                sa.append(random.choice(seed))
            return ''.join(sa)

        str = random_str()
        # 发帖
        form_data = OrderedDict(
            [
                ("atc_title", (None, str)),
                ("atc_content", (None, str)),
                ("pid", (None, '')),
                ("tid", (None, '92506')),
                ("special", (None, '')),
                ("reply_notice", (None, '1')),
                ("csrf_token", (None, csrf_token))
            ]
        )

        response_ft = ses.post(
            url='%s/phpwind/index.php?c=post&a=doreply&_json=1&fid=81' % host,
            files=form_data
        )

