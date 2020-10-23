#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: run_all_cases.py
# @time: 2020/10/11 5:14 下午

import unittest
import os
from  itsDemoTest.comm import HTMLTestReportCN
from itsDemoTest.comm.email_utils import EmailUtils
import time
from itsDemoTest.comm.ReadConfig import config
from itsDemoTest.comm.log_utils import logger

case_path = os.path.join( os.path.dirname(__file__),'testcases' )
print(case_path)
discover = unittest.defaultTestLoader.discover(start_dir=case_path,
                                               pattern='test_*.py',
                                               top_level_dir=case_path)
all_case_suite = unittest.TestSuite()
all_case_suite.addTest( discover )

report_path = os.path.join(os.path.dirname(__file__),'reports/')
report_dir = HTMLTestReportCN.ReportDirectory(report_path) #创建一个测试报告路径对象
report_dir.create_dir('API_TEST_') #调用创建目录的方法
report_html_path = HTMLTestReportCN.GlobalMsg.get_value('report_path') #获取测试报告文件的路径
report_html_file = open( report_html_path,'wb' )
html_runner = HTMLTestReportCN.HTMLTestRunner(stream=report_html_file,
                                              title='工时2.0接口测试报告',
                                              description='接口框架测试实战使用',
                                              tester='P3P4')
html_runner.run(all_case_suite)

log_path = os.path.join(os.path.dirname(__file__),
                        config.LOG_PATH + '/'+time.strftime('%Y%m%d%H%M_', time.localtime(time.time())) + 'API_TEST_LOG.log')

email_u = EmailUtils('智能工时2.0接口测试报告',report_html_file.name,log_path)
print(report_html_file)
email_u.send_mail()



