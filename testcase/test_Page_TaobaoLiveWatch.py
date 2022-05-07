# This test code uses the Appium python client.
# Please input  "pip install Appium-Python-Client" to Terminal
# -*- coding: utf-8 -*-
'''
=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=
# @Time         : 2021/7/21 7:13 下午
# @Author       : Geekmonk
# @Software     : PyCharm
# @Project name :UT_AutomatedTesting
# Case name     :test_Page_LiveWatch.py
=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=
'''

import unittest, os, logging
from time import sleep
from modules import SetUp, main_UIcontrol
from modules.swipescreen import BaseOpera
from selenium.common.exceptions import NoSuchElementException


class Page_xxxLiveWatch( unittest.TestCase ):

    def test_2_Leaving_The_Liveroom(self):
        self.driver = SetUp.android_driver()
        os.system( main_UIcontrol.Restart )
        logging.info( "case_2" )
        self.driver.implicitly_wait( 5 )
        self.driver.find_element_by_xpath( main_UIcontrol.btn_xxx ).click()
        self.driver.find_element_by_xpath( main_UIcontrol.btn_Live ).click()
        self.driver.find_element_by_xpath(main_UIcontrol.btn_firstcard_Live ).click()

        #滑动直播间10次
        a = BaseOpera( self.driver )
        i = 0
        for i in range(0,10):
            a.swipe_to_top()

        self.driver.find_element_by_xpath(main_UIcontrol.Liveroom_Closebtn ).click() # 点击直播间内的关闭按钮
        self.driver.press_keycode( 4 )  # back

        self.driver.find_element_by_xpath( main_UIcontrol.btn_xxx ).click()
        self.driver.find_element_by_xpath( main_UIcontrol.btn_Live ).click()
        self.driver.find_element_by_xpath( main_UIcontrol.btn_firstcard_Live ).click()
        self.driver.press_keycode(3)
        self.driver.find_element_by_xpath( "xpath=(//*[contains(@text, 'appname')])" ).click()
        self.driver.press_keycode( 4 )  # back

    def test_8_Button_AccountFollow(self):
        self.driver = SetUp.android_driver()
        os.system( main_UIcontrol.Restart )
        logging.info( "case_8" )
        self.driver.implicitly_wait( 5 )
        self.driver.find_element_by_xpath( main_UIcontrol.btn_xxx ).click()
        self.driver.find_element_by_xpath( main_UIcontrol.btn_Live ).click()
        self.driver.find_element_by_xpath(main_UIcontrol.btn_firstcard_Live).click()

        # 循环查找是否有 关注按钮
        while True:
            a = BaseOpera( self.driver )
            a.swipe_to_top()
            try:
                self.driver.find_element_by_xpath(main_UIcontrol.Liveroom_Followbtn).click()
                sleep(2)
                break
            except:
                print("未找到关注按钮")

        self.driver.find_element_by_xpath(main_UIcontrol.Liveroom_Avatar).click()
        self.driver.find_element_by_xpath(main_UIcontrol.Liveroom_Followed).click()
        self.driver.find_element_by_xpath("xpath=//*[@text='不再关注']").click()

        i = 0
        for i in range( 2 ):
            self.driver.press_keycode( 4 )  # back

    def test_9_Share_The_Liveroom(self):
        self.driver = SetUp.android_driver()
        os.system( main_UIcontrol.Restart )
        logging.info( "case_9" )
        self.driver.implicitly_wait( 5 )
        self.driver.find_element_by_xpath( main_UIcontrol.btn_xxx ).click()
        self.driver.find_element_by_xpath( main_UIcontrol.btn_firstcard_Live ).click()
        self.driver.find_element_by_xpath( main_UIcontrol.Liveroom_Sharebtn ).click()
        sleep( 2 )
        i = 0
        for i in range( 2 ):
            self.driver.press_keycode( 4 )  # back

    def test_16_Button_GoodsBuy(self):
        self.driver = SetUp.android_driver()
        os.system( main_UIcontrol.Restart )
        logging.info( "case_16" )
        self.driver.implicitly_wait( 5 )
        self.driver.find_element_by_xpath( main_UIcontrol.btn_xxx ).click()
        self.driver.find_element_by_xpath( main_UIcontrol.btn_Live).click()
        self.driver.find_element_by_xpath( main_UIcontrol.btn_firstcard_Live).click()
        self.driver.find_element_by_xpath(main_UIcontrol.Liveroom_packageshopping).click()
        self.driver.find_element_by_xpath("xpath=//*[@content-desc='马上抢']").click()
        self.driver.press_keycode( 4 )  # back
        self.driver.press_keycode( 4 )  # back
        a = BaseOpera( self.driver )
        a.swipe_to_top()
        i = 0
        for i in range( 2 ):
            self.driver.press_keycode( 4 )  # back

    def test_17_Click_Button_detail(self):
        self.driver = SetUp.android_driver()
        os.system(main_UIcontrol.Restart)
        logging.info( "case_17" )
        self.driver.implicitly_wait( 5 )
        self.driver.find_element_by_xpath( main_UIcontrol.btn_xxx ).click()
        self.driver.find_element_by_xpath( main_UIcontrol.btn_Live ).click()
        self.driver.find_element_by_xpath( main_UIcontrol.btn_firstcard_Live ).click()
        self.driver.find_element_by_xpath(main_UIcontrol.Liveroom_packageshopping).click()
        self.driver.find_element_by_xpath( main_UIcontrol.Liveroom_SecondCard_in_packageshopping ).click()
        i = 0
        for i in range( 3 ):
            self.driver.press_keycode( 4 )  # back

    def test_18_Button_itemwindow(self):
        self.driver = SetUp.android_driver()
        os.system( main_UIcontrol.Restart )
        logging.info( "case_18" )
        self.driver.implicitly_wait( 5 )
        self.driver.find_element_by_xpath( main_UIcontrol.btn_xxx ).click()
        self.driver.find_element_by_xpath(main_UIcontrol.btn_Live).click()
        self.driver.find_element_by_xpath(main_UIcontrol.btn_firstcard_Live).click()
        i = 0
        a = BaseOpera( self.driver )
        while i < 30:
            try:  # 如果有就点击，点击后退出
                self.driver.find_element_by_xpath( main_UIcontrol.Liveroom_itemCard ).click()
                break
            except NoSuchElementException as e:  # 如果在当前直播间没有找到就继续滑动查找
                self.driver.press_keycode( 4 )
                a.swipe_to_top()
                i += 1
        i = 0
        for i in range( 2 ):
            self.driver.press_keycode( 4 )  # back

    def test_39_Button_CommentSend(self):
        self.driver = SetUp.android_driver()
        os.system( main_UIcontrol.Restart )
        logging.info( "case_39" )
        self.driver.implicitly_wait( 5 )
        self.driver.find_element_by_xpath( main_UIcontrol.btn_xxx ).click()
        self.driver.find_element_by_xpath(main_UIcontrol.btn_Live).click()
        self.driver.find_element_by_xpath(main_UIcontrol.btn_firstcard_Live).click()
        self.driver.find_element_by_xpath(main_UIcontrol.Liveroom_input).click()
        os.system( "adb shell ime set com.sohu.inputmethod.sogou/.SogouIME" )
        sleep( 5 )
        os.system("adb shell input text 'hahahahaha'")
        self.driver.press_keycode( 66 )
        self.driver.find_element_by_xpath(main_UIcontrol.Liveroom_inputSend).click()
        os.system( "adb shell ime set com.android.adbkeyboard/.AdbIME" )
        self.driver.press_keycode( 4 )  # back

    def test_40_Button_Like(self):
        self.driver = SetUp.android_driver()
        os.system( main_UIcontrol.Restart )
        logging.info( "case_40" )
        self.driver.implicitly_wait( 5 )
        self.driver.find_element_by_xpath( main_UIcontrol.btn_xxx ).click()
        self.driver.find_element_by_xpath(main_UIcontrol.btn_Live).click()
        self.driver.find_element_by_xpath(main_UIcontrol.btn_firstcard_Live).click()
        i = 0
        for i in range (0,10):
            self.driver.find_element_by_xpath(main_UIcontrol.Liveroom_Like).click()

        self.driver.press_keycode( 4 )  # back

    def test_41_Button_StartSearch(self):
        self.driver = SetUp.android_driver()
        os.system( main_UIcontrol.Restart )
        logging.info( "case_41" )
        self.driver.implicitly_wait( 5 )
        self.driver.find_element_by_xpath( main_UIcontrol.btn_xxx ).click()
        self.driver.find_element_by_xpath(main_UIcontrol.btn_search).click()
        self.driver.find_element_by_xpath(  main_UIcontrol.btn_SearchInput ).click()
        os.system("adb shell am broadcast -a ADB_INPUT_TEXT --es msg '李佳琦'")
        os.system("adb shell input keyevent KEYCODE_ENTER")
        self.driver.find_element_by_xpath("xpath=//*[@text='直播']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='视频']").click()
        i = 0
        for i in range (3):
            self.driver.press_keycode( 4 )  # back

    def test_45_Show_TopAnchor(self):
        self.driver = SetUp.android_driver()
        os.system( main_UIcontrol.Restart )
        logging.info( "case_45" )
        self.driver.implicitly_wait( 5 )
        self.driver.find_element_by_xpath( main_UIcontrol.btn_xxx ).click()
        self.driver.find_element_by_xpath(main_UIcontrol.btn_search).click()
        self.driver.find_element_by_xpath(  main_UIcontrol.btn_SearchInput ).click()
        os.system("adb shell am broadcast -a ADB_INPUT_TEXT --es msg '李佳琦'")
        os.system("adb shell input keyevent KEYCODE_ENTER")
        self.driver.find_element_by_xpath("xpath=//*[@text='直播']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='视频']").click()
        i = 0
        for i in range (3):
            self.driver.press_keycode( 4 )  # back

    def test_46_Click_TopAnchor(self):
        self.driver = SetUp.android_driver()
        os.system( main_UIcontrol.Restart )
        logging.info( "case_46" )
        self.driver.implicitly_wait( 5 )
        self.driver.find_element_by_xpath( main_UIcontrol.btn_xxx ).click()
        self.driver.find_element_by_xpath(main_UIcontrol.btn_search).click()
        self.driver.find_element_by_xpath(  main_UIcontrol.btn_SearchInput ).click()
        os.system("adb shell am broadcast -a ADB_INPUT_TEXT --es msg '李佳琦'")
        os.system("adb shell input keyevent KEYCODE_ENTER")
        self.driver.find_element_by_xpath(main_UIcontrol.btn_Search_BigCard).click()

        i = 0
        for i in range (4):
            self.driver.press_keycode( 4 )  # back

    def test_48_Show_LiveFeed(self):
        self.driver = SetUp.android_driver()
        os.system( main_UIcontrol.Restart )
        logging.info( "case_48" )
        self.driver.implicitly_wait( 5 )
        self.driver.find_element_by_xpath( main_UIcontrol.btn_xxx ).click()
        self.driver.find_element_by_xpath(main_UIcontrol.btn_search).click()
        self.driver.find_element_by_xpath(  main_UIcontrol.btn_SearchInput ).click()
        os.system( "adb shell am broadcast -a ADB_INPUT_TEXT --es msg 'XXX'" )
        os.system( "adb shell input keyevent KEYCODE_ENTER" )
        # 循环查找短视频
        i = 0
        a = BaseOpera( self.driver )
        while i < 10:
            try:  # 找它
                self.driver.find_element_by_xpath( main_UIcontrol.btn_Search_Liveicon ).click()
                sleep(3)
                break
            except NoSuchElementException as e:  # 如果在当前视频没有找到就继续滑动查找
                a.swipe_to_top()
                i += 1
        i = 0
        for i in range (3):
            self.driver.press_keycode( 4 )  # back

    def test_49_Click_LiveFeed(self):
        self.driver = SetUp.android_driver()
        os.system( main_UIcontrol.Restart )
        logging.info( "case_49" )
        self.driver.implicitly_wait( 5 )
        self.driver.find_element_by_xpath( main_UIcontrol.btn_xxx ).click()
        self.driver.find_element_by_xpath(main_UIcontrol.btn_search).click()
        self.driver.find_element_by_xpath(  main_UIcontrol.btn_SearchInput ).click()
        os.system( "adb shell am broadcast -a ADB_INPUT_TEXT --es msg 'xxx'" )
        os.system( "adb shell input keyevent KEYCODE_ENTER" )
        # 循环查找短视频
        i = 0
        a = BaseOpera( self.driver )
        while i < 10:
            try:  # 找它
                self.driver.find_element_by_xpath( main_UIcontrol.btn_Search_Liveicon ).click()
                sleep(3)
                break
            except NoSuchElementException as e:  # 如果在当前视频没有找到就继续滑动查找
                a.swipe_to_top()
                i += 1
        i = 0
        for i in range (3):
            self.driver.press_keycode( 4 )  # back

    def test_50_Show_Video(self):
        self.driver = SetUp.android_driver()
        os.system( main_UIcontrol.Restart )
        logging.info( "case_50" )
        self.driver.implicitly_wait( 5 )
        self.driver.find_element_by_xpath( main_UIcontrol.btn_xxx ).click()
        self.driver.find_element_by_xpath(main_UIcontrol.btn_search).click()
        self.driver.find_element_by_xpath(  main_UIcontrol.btn_SearchInput ).click()
        os.system("adb shell am broadcast -a ADB_INPUT_TEXT --es msg '李佳琦'")
        os.system("adb shell input keyevent KEYCODE_ENTER")
        # 循环查找短视频
        i = 0
        a = BaseOpera( self.driver )
        while i < 10:
            try:  # 找它
                self.driver.find_element_by_xpath( "xpath=//*[@text='相关视频']" )
                break
            except NoSuchElementException as e:
                a.swipe_to_top()
                i += 1
        self.driver.find_element_by_xpath(main_UIcontrol.btn_Search_video).click()
        sleep(2)
        i = 0
        for i in range (4):
            self.driver.press_keycode( 4 )  # back


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
