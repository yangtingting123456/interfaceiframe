import  logging
import os.path
import time
from itsDemoTest.comm.ReadConfig import config

#第一步，创建一个logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)  #Log等级总开关
#第二步，创建一个handler，用户写入日志文件；
rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
log_path = os.path.join( os.path.dirname(__file__),'..', config.LOG_PATH+'/'+rq+'.log' )
fh = logging.FileHandler(log_path,'a',encoding='utf-8')
fh.setLevel(logging.DEBUG)   #输入到file的log等级的开关
#第三步，定义handle的输入格式
formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
fh.setFormatter(formatter)
#第四步，将logger添加到handle里面
logger.addHandler(fh)
#日志
logging.info('this is a logging info message')
logging.debug('this is a logging debug message')
logging.warning('this is a logging warning message')
logging.error('this is a logging error message')
logging.critical('this is a logging critical message')





