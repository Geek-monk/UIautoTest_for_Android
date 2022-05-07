# This test code uses the Appium python client.
# Please input  "pip install Appium-Python-Client" to Terminal
# -*- coding: utf-8 -*-
'''
=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=
# @Time         : 2021/7/7 6:04 下午
# @Author       : Geekmonk
# @Software     : PyCharm
# @Project name :UT_AutomatedTesting
# Case name     :main_UIcontrol.py
=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=
'''
使用以下命令获取当前界面的 Activity
adb shell dumpsys activity top | grep ACTIVITY
此页内容主要是封装控件，用抓取控件的工具对页面元素进行封装
'''