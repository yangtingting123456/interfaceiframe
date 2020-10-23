
import os
import logging
from logging import handlers
from itsDemoTest.comm.ReadConfig import config
import time

log_path = os.path.join( os.path.dirname(__file__),'..', config.LOG_PATH )

class LogUtils:
    def __init__(self,log_path = log_path,rq=time.strftime('%Y%m%d%H%M_', time.localtime(time.time())) ):
        self.log_file_name = rq+'API_TEST_LOG.log'
        self.logger = logging.getLogger('API_TEST_LOG')
        self.logger.setLevel( config.LOG_LEVEL )

        formatter = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        console_handler.setLevel( config.LOG_LEVEL )

        file_handler = handlers.TimedRotatingFileHandler(os.path.join(log_path,self.log_file_name),when='D',interval=1,backupCount=1,
                                                         encoding='utf-8')
        file_handler.setLevel( config.LOG_LEVEL )
        file_handler.setFormatter( formatter )

        self.logger.addHandler(console_handler)
        self.logger.addHandler(file_handler)

        console_handler.close()  # 防止打印日志重复
        file_handler.close()  # 防止打印日志重复

    def get_logger(self):
        return self.logger

logger = LogUtils().get_logger()

if __name__=='__main__':
    logger.info('this is a logging info message')
    logger.debug('this is a logging debug message')
    logger.warning('this is a logging warning message')
    logger.error('this is a logging error message')
    logger.critical('this is a logging critical message')