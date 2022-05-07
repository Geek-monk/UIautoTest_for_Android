# This test code uses the Appium python client.
# Please input  "pip install Appium-Python-Client" to Terminal
# -*- coding: utf-8 -*-
'''
==============================================
# @Time         : 2021/7/2 5:10 下午
# @Author       : Geekmonk
# @Software     : PyCharm
# @Project name :UT_AutomatedTesting
# Case name     :Login.py
==============================================
'''

import os
from modules import SetUp
from modules import main_UIcontrol

def Login_ChangeAccount_NoFollowing(self):
    self.driver = SetUp.android_driver()
    self.driver.implicitly_wait( 5 )
    self.driver.find_element_by_xpath(
        "xpath=(//*[@class='android.widget.LinearLayout' and ./parent::*[@id='hp3_bottom_tab']]/*/*/*/*[@id='hp3_tab_img'])[1]" ).click()
    os.system( main_UIcontrol.btn_Mine )
    self.driver.find_element_by_xpath( "xpath=//*[@id='personal_menu']" ).click()
    self.driver.find_element_by_xpath( "xpath=//*[@text='设置']" ).click()
    self.driver.find_element_by_xpath( "xpath=//*[@resource-id='com.xxxx.xxxx:id/personal_exit_btn']" ).click()
    self.driver.find_element_by_xpath( "xpath=//*[@resource-id='com.xxxx.xxxx:id/homepage2_login_text']" ).click()
    self.driver.find_element_by_xpath( "xpath=//*[@resource-id='com.xxxx.xxxx:id/ali_user_guide_account_login_btn']" ).click()
    self.driver.find_element_by_xpath( "xpath=//*[@text='更多']" ).click()
    self.driver.find_element_by_xpath( "xpath=//*[@text='换个账户登录']" ).click()
    self.driver.find_element_by_xpath("xpath=//*[@resource-id='com.xxxx.xxxx:id/aliuser_recommend_login_account_et']").click()

    login_inputbox = self.driver.find_element_by_xpath("xpath=//*[@resource-id='com.xxxx.xxxx:id/aliuser_recommend_login_account_et']")
    login_inputbox.click()
    os.system("adb shell am broadcast -a ADB_INPUT_TEXT --es msg 'test user id'")

    self.driver.find_element_by_xpath( "xpath=//*[@resource-id='com.xxxx.xxxx:id/tl_login_chb_protocol']" ).click()
    self.driver.find_element_by_xpath("xpath=//*[@text='确认']").click()
    passwd_inputbox = self.driver.find_element_by_xpath("xpath=//*[@resource-id='com.xxxx.xxxx:id/aliuser_recommend_login_password_et']")
    passwd_inputbox.send_keys('your id |gongxifacai327,')
    self.driver.find_element_by_xpath( "xpath=//*[@text='登录']" ).click()

    return


def Login_ChangeAccount_Recovery(self):
    self.driver = SetUp.android_driver()
    self.driver.implicitly_wait( 5 )
    self.driver.find_element_by_xpath(
        "xpath=(//*[@class='android.widget.LinearLayout' and ./parent::*[@id='hp3_bottom_tab']]/*/*/*/*[@id='hp3_tab_img'])[1]" ).click()
    os.system( main_UIcontrol.btn_Mine )
    self.driver.find_element_by_xpath( "xpath=//*[@id='personal_menu']" ).click()
    self.driver.find_element_by_xpath( "xpath=//*[@text='设置']" ).click()
    self.driver.find_element_by_xpath( "xpath=//*[@resource-id='com.xxxx.xxxx:id/personal_exit_btn']" ).click()
    self.driver.find_element_by_xpath( "xpath=//*[@resource-id='com.xxxx.xxxx:id/homepage2_login_text']" ).click()
    self.driver.find_element_by_xpath( "xpath=//*[@resource-id='com.xxxx.xxxx:id/ali_user_guide_account_login_btn']" ).click()
    self.driver.find_element_by_xpath( "xpath=//*[@text='更多']" ).click()
    self.driver.find_element_by_xpath( "xpath=//*[@text='换个账户登录']" ).click()
    self.driver.find_element_by_xpath("xpath=//*[@resource-id='com.xxxx.xxxx:id/aliuser_recommend_login_account_et']").click()

    login_inputbox = self.driver.find_element_by_xpath("xpath=//*[@resource-id='com.xxxx.xxxx:id/aliuser_recommend_login_account_et']")
    login_inputbox.click()
    os.system( "adb shell am broadcast -a ADB_INPUT_TEXT --es msg 'userid00015'" )
    self.driver.find_element_by_xpath( "xpath=//*[@resource-id='com.xxxx.xxxx:id/tl_login_chb_protocol']" ).click()
    self.driver.find_element_by_xpath("xpath=//*[@text='确认']").click()

    passwd_inputbox = self.driver.find_element_by_xpath("xpath=//*[@resource-id='com.xxxx.xxxx:id/aliuser_recommend_login_password_et']")
    passwd_inputbox.send_keys("your id |gongxifacai327,")
    self.driver.find_element_by_xpath( "xpath=//*[@text='登录']" ).click()

    return

def Login_ChangeAccount_Liveroom(self):
    self.driver = SetUp.android_driver()
    self.driver.implicitly_wait( 5 )
    self.driver.find_element_by_xpath(
        "xpath=(//*[@class='android.widget.LinearLayout' and ./parent::*[@id='hp3_bottom_tab']]/*/*/*/*[@id='hp3_tab_img'])[1]" ).click()
    os.system( main_UIcontrol.btn_Mine )
    self.driver.find_element_by_xpath( "xpath=//*[@id='personal_menu']" ).click()
    self.driver.find_element_by_xpath( "xpath=//*[@text='设置']" ).click()
    self.driver.find_element_by_xpath( "xpath=//*[@resource-id='com.xxxx.xxxx:id/personal_exit_btn']" ).click()
    self.driver.find_element_by_xpath( "xpath=//*[@resource-id='com.xxxx.xxxx:id/homepage2_login_text']" ).click()
    self.driver.find_element_by_xpath( "xpath=//*[@resource-id='com.xxxx.xxxx:id/ali_user_guide_account_login_btn']" ).click()
    self.driver.find_element_by_xpath( "xpath=//*[@text='更多']" ).click()
    self.driver.find_element_by_xpath( "xpath=//*[@text='换个账户登录']" ).click()
    self.driver.find_element_by_xpath("xpath=//*[@resource-id='com.xxxx.xxxx:id/aliuser_recommend_login_account_et']").click()

    login_inputbox = self.driver.find_element_by_xpath("xpath=//*[@resource-id='com.xxxx.xxxx:id/aliuser_recommend_login_account_et']")
    login_inputbox.click()
    os.system( "adb shell am broadcast -a ADB_INPUT_TEXT --es msg 'test user id '" )
    self.driver.find_element_by_xpath( "xpath=//*[@resource-id='com.xxxx.xxxx:id/tl_login_chb_protocol']" ).click()
    self.driver.find_element_by_xpath("xpath=//*[@text='确认']").click()

    passwd_inputbox = self.driver.find_element_by_xpath("xpath=//*[@resource-id='com.xxxx.xxxx:id/aliuser_recommend_login_password_et']")
    passwd_inputbox.send_keys("test user id |gongxifacai327,")
    self.driver.find_element_by_xpath( "xpath=//*[@text='登录']" ).click()

    return


