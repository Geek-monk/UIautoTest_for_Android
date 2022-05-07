# This test code uses the Appium python client.
# Please input  "pip install Appium-Python-Client" to Terminal
# -*- coding: utf-8 -*-
'''
==============================================
# @Time         : 2021/7/2 5:10 下午
# @Author       : Geekmonk
# @Software     : PyCharm
# @Project name :UT_AutomatedTesting
# Case name     : SendReport_for_Dingding.py
==============================================
'''

import requests
import time
import hmac
import hashlib
import base64
import urllib.parse
import json

# 使用钉钉发送报告
def ReportToDing(content):
    host = 'https://oapi.dingtalk.com/robot/send?'
    timestamp = round(time.time() * 1000)
    #小群的机器人
    secret = 'SEC40f57ecxxxxxxxxxxxxxxxxxxxd093123d6a'
    secret_enc = bytes(secret,encoding = 'utf-8')
    string_to_sign = '{}\n{}'.format(timestamp, secret)
    string_to_sign_enc = bytes(string_to_sign,encoding = 'utf-8')
    hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
    sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))

    #小群的机器人
    url = host + 'access_txxxxxxxxxxxxx3xxxxxxxxxxxxxxd7f06887ef4ab83'+'&timestamp='+str(timestamp)+'&sign='+sign

    dict = {"msgtype":"text",
            "text":
                {"content":content
                 }
            }
    payload = json.dumps(dict)
    headers = {
      'Content-Type': 'application/json'
    }

    response = requests.post(url,headers=headers,data=payload)
    print (response.text)