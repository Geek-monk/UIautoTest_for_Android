# This test code uses the Appium python client.
# Please input  "pip install Appium-Python-Client" to Terminal
# -*- coding: utf-8 -*-
'''
=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=
# @Time         : 2021/7/22 7:45 下午
# @Author       : Geekmonk
# @Software     : PyCharm
# @Project name :UT_AutomatedTesting
# Case name     :test_Page_xxxxxxFollow.py
=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=
'''

import unittest,os, logging
from time import sleep
from modules import SetUp, main_UIcontrol,Login
from modules.swipescreen import BaseOpera
from selenium.common.exceptions import NoSuchElementException


class Page_xxxxxxFollow( unittest.TestCase ):

    def test_3_Specialfollow(self):
        self.driver = SetUp.android_driver()
        os.system( main_UIcontrol.Restart )
        logging.info( "case_3" )
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath( main_UIcontrol.btn_xxx ).click()
        self.driver.find_element_by_xpath( main_UIcontrol.btn_Favoritebotton).click()
        self.driver.press_keycode( 4 )  # back

    def test_4_Click_Specialfollow(self):
        self.driver = SetUp.android_driver()
        os.system( main_UIcontrol.Restart )
        logging.info( "case_4" )
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath( main_UIcontrol.btn_xxx ).click()
        self.driver.find_element_by_xpath( main_UIcontrol.btn_Favoritebotton ).click()

        try:
            fristFavorite_card = self.driver.find_element_by_xpath(main_UIcontrol.btn_firstFavoriteCard)
        except NoSuchElementException:
            print("检查是否有想要点击的东西")
        else:
            fristFavorite_card.click()

        sleep(3)
        self.driver.press_keycode( 4 )  # back
        self.driver.press_keycode( 4 )  # back

    def test_5_More_xxx(self):
        self.driver = SetUp.android_driver()
        os.system( main_UIcontrol.Restart )
        logging.info( "case_5" )
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath( main_UIcontrol.btn_xxx ).click()
        self.driver.find_element_by_xpath( main_UIcontrol.btn_Favoritebotton ).click()

        item = self.driver.find_element_by_xpath(main_UIcontrol.btn_watchxxx)
        # 循环查找
        a = BaseOpera( self.driver )
        i = 0
        for i in range( 0, 3 ):
            a.swipe_to_top()
        item.click()

        self.driver.find_element_by_xpath(main_UIcontrol.xxxroom_Closebtn).click()
        self.driver.press_keycode( 4 )  # back

        replay = self.driver.find_element_by_xpath( main_UIcontrol.btn_replayxxx )
        # 循环查找回放卡片
        b = BaseOpera( self.driver )
        s = 0
        for s in range( 0, 7 ):
            b.swipe_to_top()

        replay.click()

        self.driver.find_element_by_xpath(main_UIcontrol.xxxroom_Closebtn).click()
        self.driver.press_keycode( 4 )  # back

    def test_6_Page_xxxxxxFollow_More_xxx(self):
        self.driver = SetUp.android_driver()
        os.system( main_UIcontrol.Restart )
        logging.info( "case_6" )
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath( main_UIcontrol.btn_xxx ).click()
        self.driver.find_element_by_xpath( main_UIcontrol.btn_Favoritebotton ).click()

        item = self.driver.find_element_by_xpath(main_UIcontrol.btn_watchxxx)
        # 循环查找
        a = BaseOpera( self.driver )
        i = 0
        for i in range( 0, 3 ):
            a.swipe_to_top()
        item.click()

        self.driver.find_element_by_xpath(main_UIcontrol.xxxroom_Closebtn).click()
        self.driver.press_keycode( 4 )  # back

        replay = self.driver.find_element_by_xpath( main_UIcontrol.btn_replayxxx )
        # 循环查找回放卡片
        b = BaseOpera( self.driver )
        s = 0
        for s in range( 0, 7 ):
            b.swipe_to_top()

        replay.click()

        self.driver.find_element_by_xpath(main_UIcontrol.xxxroom_Closebtn).click()
        self.driver.press_keycode( 4 )  # back

    def test_7_Click_Recommend_xxx(self):
        self.driver = SetUp.android_driver()
        os.system( main_UIcontrol.Restart )
        logging.info( "case_7" )
        self.driver.implicitly_wait( 5 )

        Login.Login_ChangeAccount_NoFollowing( self )
        self.driver.find_element_by_xpath(main_UIcontrol.btn_Favoritebotton).click()

        i = 0
        a = BaseOpera( self.driver )
        while i < 30:
            try:  # 如果有就点击，点击后退出
                self.driver.find_element_by_xpath( main_UIcontrol.btn_watchxxx ).click()
                break
            except NoSuchElementException as e:  # 如果在当前视频没有找到就继续滑动查找
                a.swipe_to_top()
                i += 1

        self.driver.press_keycode( 4 )  # back
        # 更换账号---换回测试之前的账号
        Login.Login_ChangeAccount_Recovery(self)

    def test_42_Show_More_Video(self):
        self.driver = SetUp.android_driver()
        os.system( main_UIcontrol.Restart )
        logging.info( "case_42" )
        self.driver.implicitly_wait( 5 )
        self.driver.find_element_by_xpath( main_UIcontrol.btn_xxx ).click()
        self.driver.find_element_by_xpath(main_UIcontrol.btn_Favoritebotton ).click()

        item = self.driver.find_element_by_xpath( main_UIcontrol.btn_Shortvideo_undermainpage)
        a = BaseOpera( self.driver )
        i = 0
        for i in range( 0, 20):
            a.swipe_to_top()
        item.click()
        sleep(4)

        self.driver.press_keycode( 4 )  # back

    def test_43_Click_More_Video(self):
        self.driver = SetUp.android_driver()
        os.system( main_UIcontrol.Restart )
        logging.info( "case_43" )
        self.driver.implicitly_wait( 5 )
        self.driver.find_element_by_xpath( main_UIcontrol.btn_xxx ).click()
        self.driver.find_element_by_xpath(main_UIcontrol.btn_Favoritebotton ).click()

        item = self.driver.find_element_by_xpath( main_UIcontrol.btn_Shortvideo_undermainpage)
        a = BaseOpera( self.driver )
        for i in range( 10 ):
            a.swipe_to_top()
        item.click()
        sleep(4)

        self.driver.press_keycode( 4 )  # back



    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

