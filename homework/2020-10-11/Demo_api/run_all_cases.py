#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: run_all_cases.py
# @time: 2020/10/11 5:14 下午

import unittest
import os
import HTMLTestReportCN

case_path = os.path.join( os.path.dirname(__file__),'testcases' )
print(case_path)
discover = unittest.defaultTestLoader.discover(start_dir=case_path,
                                               pattern='test_*.py',
                                               top_level_dir=case_path)
all_case_suite = unittest.TestSuite()
all_case_suite.addTest( discover )

report_path = os.path.join(os.path.dirname(__file__),'report/')
print(report_path)
report_dir = HTMLTestReportCN.ReportDirectory(report_path) #创建一个测试报告路径对象
report_dir.create_dir('API_TEST_') #调用创建目录的方法
report_html_path = HTMLTestReportCN.GlobalMsg.get_value('report_path') #获取测试报告文件的路径
report_html_file = open( report_html_path,'wb' )
html_runner = HTMLTestReportCN.HTMLTestRunner(stream=report_html_file,
                                              title='2020-10-11号作业接口测试报告',
                                              description='接口框架测试实战使用',
                                              tester='P3P4')
html_runner.run(all_case_suite)




