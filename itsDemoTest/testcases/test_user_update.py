import requests
from itsDemoTest.comm.ReadConfig import config
from itsDemoTest.comm.md5_password import psd
import unittest
from itsDemoTest.comm.apiutils import API_Info
from itsDemoTest.comm.log_utils import logger

class UserUpateCase(unittest.TestCase):
    def setUp(self):
        self.session = requests.session()
        self.HOST = config.GET_HOSTS
        self.PORT = config.GET_PORT
        self.pwd = psd.get_md5_password()
        self.UserName = config.GET_UserName
        self.PageNum = config.GET_PageNum
        self.PageSize = config.GET_PageSize

    def tearDown(self):
        self.session.close()
    #更新用户信息
    def test_user_update(self):
        ses_login = API_Info.Login_Api_Info(self.session, self.HOST, self.PORT, self.UserName, self.pwd)
        json_login_data = ses_login.json()
        token = json_login_data['data']['token']
        res = API_Info.update_userinfo_api(self.session, self.HOST, self.PORT,token)
        updateInfo_json = res.json()
        code = updateInfo_json['code']
        self.assertEqual(code,200,'更新用户信息失败')

    # 更新用户信息失败，返回code1003
    def test_user_update_fail(self):
        ses_login = API_Info.Login_Api_Info(self.session, self.HOST, self.PORT, self.UserName, self.pwd)
        json_login_data = ses_login.json()
        token = json_login_data['data']['token']
        res = API_Info.update_userinfo_api(self.session, self.HOST, self.PORT, 'token')
        updateInfo_json = res.json()
        code = updateInfo_json['code']
        self.assertEqual(code, 1003, 'token错误，返回code1003')
if __name__ == '__main__':
    unittest.main()