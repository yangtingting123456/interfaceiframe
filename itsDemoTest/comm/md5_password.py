import hashlib
# 密码md5加密
class Md5Password:
    def get_md5_password(self):
        md5 = hashlib.md5()
        md5.update('abc123456'.encode('utf-8'))
        return (md5.hexdigest())

psd = Md5Password()
