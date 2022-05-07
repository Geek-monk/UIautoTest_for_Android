# This test code uses the Appium python client.
# Please input  "pip install Appium-Python-Client" to Terminal
# -*- coding: utf-8 -*-
'''
==============================================
# @Time         : 2021/7/2 5:10 下午
# @Author       : Geekmonk
# @Software     : PyCharm
# @Project name :UT_AutomatedTesting
# Case name     : SetUp.py
==============================================
'''

import yaml, os
from appium import webdriver
import requests
import uiautomator2 as u2
import time
import json
import datetime

# 项目根目录路径
BASE_PATH = os.path.dirname( os.path.dirname( os.path.abspath( __file__ ) ) )
# capabilities配置文件desired_caps.py路径
DESIRED_CAPS_YAML_PATH = BASE_PATH + '/config/desired_caps.yaml'

def android_driver():
    # 从desired_caps.yaml读取driver配置数据
    stream = open( DESIRED_CAPS_YAML_PATH, 'r' )
    data = yaml.load( stream, Loader=yaml.FullLoader )

    desired_caps = {}
    desired_caps[ "platformName"] = data[ "platformName"]
    desired_caps[ "platformVersion" ] = data[ "platformVersion" ]
    desired_caps[ "deviceName" ] = data[ "deviceName" ]
    desired_caps[ "newCommandTimeout" ] = data[ "newCommandTimeout" ]
    desired_caps[ "allowTestPackages" ] = data[ "allowTestPackages" ]
    desired_caps[ "autoGrantPermissions" ] = data[ "autoGrantPermissions" ]
    desired_caps[ "ensureWebviewsHavePages" ] = data[ "ensureWebviewsHavePages" ]
    desired_caps[ "unicodeKeyboard" ] = data[ "unicodeKeyboard" ]
    desired_caps[ "resetKeyboard" ] = data[ "resetKeyboard" ]
    desired_caps[ "noReset" ] = data[ "noReset" ]
    desired_caps[ "appPackage" ] = data[ "appPackage" ]
    desired_caps[ "appActivity" ] = data[ "appActivity" ]
    desired_caps[ "automationName" ] = data[ "automationName" ]
    # desired_caps[ "autoLaunch" ] = data[ "autoLaunch" ]
    # desired_caps[ "newCommandTimeout" ] = data[ "newCommandTimeout" ]
#驱动程序
    driver = webdriver.Remote( 'http://' + str( data[ 'url' ] ) + ':' + str( data[ 'port' ] ) + '/wd/hub', desired_caps )
    driver.implicitly_wait( 2 )

    return driver


def begin_pingbacktest( driver, url):

    pass


def get_XXOobject():
    url = 'xxx'
    payload = '{"appInfoId":xxx,"appToken":"exxxxxxxxxxxU","workId":"2xxx0"}'
    headers = {'Content-Type': 'application/json'}
    response = requests.request( "POST", url, headers=headers, data=payload )
    jsonxxOobject = json.loads( response.text )
    responsedata = jsonxxOobject[ 'data' ]
    authQueryxxx = {"xxxxxxxx": responsedata}
    return authQueryxxxx


def begin_verify(authQueryxxx):
    url = 'https://utcxxxxxxxt/verify'
    data = {"verifyxxx": {"appInfoId": xxx, "planId": 20000005, "verifyType": "APP"}}
    dict = data.copy()
    dict.update( authQueryxxx )
    data = json.dumps( dict )
    print( '数据', data )
    headers = {'Content-Type': 'application/json'}
    response = requests.request( "POST", url, headers=headers, data=data )
    data = json.loads( response.text )

    return data


def finish_verify(authQueryxxx, verifyInstanceId, trackDebugId):
    time = datetime.date.today()
    # url = 'https://pre-utcheck.livex.xxxx.com/proxy/finish/verify'
    url = 'https://utcheck.livex.xxxx.com/proxy/finish/verify'
    data = {"verifyxxx": {"verifyInstanceId": verifyInstanceId, "trackDebugId": trackDebugId,
                          "reportName": "%s,XXXXXXUSERID" % time}}
    dict = data.copy()
    dict.update( authQueryxxx )
    data = json.dumps( dict )
    headers = {'Content-Type': 'application/json'}
    response = requests.request( "POST", url, headers=headers, data=data )
    return response.text


def get_ReportInfo(authQueryXXX, verifyInstanceId):
    # url = 'https://pre-utcheck.livex.xxxx.com/proxy/get/verifyReportInfo'
    url = 'https://utcheck.livex.xxxx.com/proxy/get/verifyReportInfo'
    data = {"verifyxxx": {"verifyInstanceId": verifyInstanceId, "reportName": "namexxxxxx"}}
    dict = data.copy()
    dict.update( authQueryXXX )
    data = json.dumps( dict )
    headers = {'Content-Type': 'application/json'}
    response = requests.request( "POST", url, headers=headers, data=data )
    return response.text


def get_ReportDetail(authQueryxxx, verifyInstanceId):
    # url = 'https://pre-utcheck.livex.xxxx.com/proxy/get/verifyReportDetail'
    url = 'https://utcheck.livex.xxxx.com/proxy/get/verifyReportDetail'
    data = {"verifyxxx": {"verifyInstanceId": verifyInstanceId, "reportName": "直播测试校验"}}
    dict = data.copy()
    dict.update( authQueryxxx )
    data = json.dumps( dict )
    headers = {'Content-Type': 'application/json'}
    response = requests.request( "POST", url, headers=headers, data=data )
    print( '测试结果是', response.text )
    return response.text


def get_ReportLogUrl(reportId, trackDebugId, verifyInstanceId):

    url = 'https://xxxxxxxxxxxxxxxxx/track/check/details?reportId=%d&trackDebugId=%s&verifyInstanceId=%d' % (
    reportId, trackDebugId, verifyInstanceId)
    return url


def Analyse_ReportInfo(data):
    datajson = json.loads( data )
    Detaildata = datajson[ 'data' ][ 'items' ]
    for item in Detaildata:
        list = {
            "规则名称": item[ 'ruleName' ],
            "规则ID": item[ 'ruleId' ],
            "规则是否通过（1代表通过，0代表不通过）": item[ 'ruleStatus' ]
        }
        Detaildata.append( list )

    return Detaildata