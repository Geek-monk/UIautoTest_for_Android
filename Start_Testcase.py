# This test code uses the Appium python client.
# Please input  "pip install Appium-Python-Client" to Terminal
# -*- coding: utf-8 -*-
'''
=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=
# @Time         : 2021/8/4 2:24 下午
# @Author       : Geekmonk
# @Software     : PyCharm
# @Project name :UT_AutomatedTesting
# Case name     :Start_Testcase.py
=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=
'''

import unittestreport
import json
import unittest
import time
from modules import SetUp,SendReport_for_Dingding


# 加载测试用例
testcase = unittest.defaultTestLoader.discover( "/Users/xxxx/PycharmProjects/testcase" )

now = time.time()
# 当前测试结束时间
now_time = time.strftime( "%Y%m%d_%H%M%S", time.localtime( now ) )
# 测试报告名称
report_name = "UIAutoTestResult_" + now_time + ".html"
# 测试报告名称
resultname = "AndroidUTautoTest_"+now_time+".html"
# 测试人员名称
tester_name = "Geekmonk"
# 测试报告标题
resulttitle = "Android UI自动化测试报告" + now_time

# 创建测试运行程序
runner = unittestreport.TestRunner( testcase, tester=tester_name, filename=resultname, report_dir="/Users/xxxx/PycharmProjects/UT_AutomatedTesting/report",
                                    title=resulttitle, desc="androidUI自动化测试报告", templates=1 )
# 运行测试用例
runner.run( count=3, interval=2 )  # count为重试次数，interval 为重试的时间间隔

time.sleep( 4 )
# 获取正确或者错误的报告信息
SetUp.finish_verify( DTOobject, verifyInstanceId, trackDebugId )
ReportInfo = SetUp.get_ReportInfo( DTOobject, verifyInstanceId )
ReportInfodata = json.loads( ReportInfo )
reportId = ReportInfodata[ 'data' ][ 'reportId' ]
errorCount = ReportInfodata[ 'data' ][ 'errorCount' ]
successCount = ReportInfodata[ 'data' ][ 'successCount' ]
url = SetUp.get_ReportLogUrl( reportId, trackDebugId, verifyInstanceId )
content = '通过情况：\n 成功次数：%s' % successCount + '\n'  + ' 错误次数： %s' % errorCount + '\n' + '报告地址：' + '\n' + url

# 获取报告细节
ReportDetail = SetUp.get_ReportDetail(DTOobject,verifyInstanceId)
ReportDetaildata = json.loads(ReportDetail)
ruleName = ReportDetaildata['data']['ruleName']
rulePreCondtion = ReportDetaildata['data']['rulePreCondition']
ruleStatus = ReportDetaildata['data']['ruleStatus']
# 发送钉钉
SendReport_for_Dingding.ReportToDing(content)