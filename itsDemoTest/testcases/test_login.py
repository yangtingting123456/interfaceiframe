import requests
from itsDemoTest.comm.ReadConfig import config
from itsDemoTest.comm.md5_password import psd
import unittest
from itsDemoTest.comm.apiutils import API_Info
from itsDemoTest.comm.log_utils import logger

class Login_InfoCase(unittest.TestCase):
    def setUp(self) -> None:
        self.session = requests.session()
        self.HOST = config.GET_HOSTS
        self.PORT = config.GET_PORT
        self.pwd = psd.get_md5_password()
        self.UserName = config.GET_UserName
        self.usernameisnot='111'
        self.passwordisnot = 'abc123'

    def tearDown(self):
        self.session.close()

    def test_Login_Success(self):
        ses = API_Info.Login_Api_Info(self.session,self.HOST,self.PORT,self.UserName,self.pwd)
        body = ses.json()
        code = body['code']
        self.assertEqual(code,200,'登录失败')
    #登录接口用户名不存在
    def test_Login_Fail01(self):
        ses = API_Info.Login_Api_Info(self.session, self.HOST, self.PORT,self.usernameisnot, self.pwd)
        body = ses.json()
        code = body['code']
        self.assertEqual(code, 2114, '登录接口用户名不存在，返回code2114')
        # 登录接口用户名不存在
    #登录接口密码错误
    def test_Login_Fail02(self):
        ses = API_Info.Login_Api_Info(self.session,self.HOST, self.PORT,self.UserName, self.passwordisnot)
        body = ses.json()
        code = body['code']
        self.assertEqual(code, 2114, '登录接口密码错误，返回code2114')

if __name__ == '__main__':
    unittest.main(verbosity=2)











