import hashlib
# 密码md5加密
def get_md5_password():
    md5 = hashlib.md5()
    md5.update('abc123456'.encode('utf-8'))
    return (md5.hexdigest())

md5_password = get_md5_password()
