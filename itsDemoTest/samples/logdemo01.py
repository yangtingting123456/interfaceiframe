import logging
#将信息打印在控制台上
# logging.debug('debug 级别日志')
# logging.info('info 级别日志')
# logging.warning('warn 级别日志')
# logging.error('error 级别日志')
# logging.critical('critical 严重级别日志')
# 级别排序:CRITICAL > ERROR > WARNING > INFO > DEBUG
# logging.basicConfig(level=logging.NOTSET)
# logging.debug('如果设置了日志级别为NOTSET,那么这里可以采取debug、info的级别的内容也可以显示在控制台上了')
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
#由于日志基本配置中基本设置为DEBUG,所以一下打印信息将会全部显示在控制台上
logging.info('this is a logging info message')
logging.debug('this is a logging debug message')
logging.warning('this is a logging warning message')
logging.error('this is a logging error message')
logging.critical('this is a logging critical message')




