import configparser
import os

config_file_path = os.path.join(os.path.dirname(__file__),'..','config','config.ini' )
print(config_file_path)
class ConfigUtils:
    def __init__(self,conf_path = config_file_path):
        self.cfg = configparser.ConfigParser()
        self.cfg.read( config_file_path )
     #获取配置文件的主机地址
    @property   # 类中的一个方法加property这个装饰器 属性方法
    def GET_HOSTS(self):
        hosts_value = self.cfg.get('default','HOSTS')
        return hosts_value

    #获取配置文件的主机的端口号
    @property
    def GET_PORT(self):
        port_value = self.cfg.get('default', 'PORT')
        return port_value

    #获取登录接口用户登录的用户名
    @property
    def GET_UserName(self):
        port_value = self.cfg.get('user_info', 'UserName')
        return port_value

    # 获取配置文件列表分页的页码数
    @property
    def GET_PageNum(self):
        port_value = self.cfg.get('user_info', 'pageNum')
        return port_value

     # 获取配置文件的分页每页条数
    @property
    def GET_PageSize(self):
        port_value = self.cfg.get('user_info', 'pageSize')
        return port_value

    @property
    def LOG_PATH(self):
        log_path_value = self.cfg.get('default', 'LOG_PATH')
        return log_path_value

    @property
    def LOG_LEVEL(self):
        log_level_value = int(self.cfg.get('default', 'LOG_LEVEL'))
        return log_level_value

    @property
    def SMTP_RECEIVER(self):
        smtp_receiver_value = self.cfg.get('default', 'SMTP_RECEIVER')
        return smtp_receiver_value

    @property
    def REPORT_PAHT(self):
        report_paht_value = self.cfg.get('default', 'REPORT_PATH')
        return report_paht_value

config = ConfigUtils()




