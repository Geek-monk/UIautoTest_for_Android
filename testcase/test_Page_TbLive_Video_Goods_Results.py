# This test code uses the Appium python client.
# Please input  "pip install Appium-Python-Client" to Terminal
# -*- coding: utf-8 -*-
'''
=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=
# @Time         : 2021/7/23 7:46 下午
# @Author       : Geekmonk
# @Software     : PyCharm
# @Project name :UT_AutomatedTesting
# Case name     :test_Page_TbLive_Video_Goods_Results.py
=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=
'''

import unittest,os, logging
from time import sleep
from modules import SetUp, main_UIcontrol
from modules.swipescreen import BaseOpera
from selenium.common.exceptions import NoSuchElementException


class Page_TbLive_Video_Goods_Results( unittest.TestCase ):

    def test_11_Goods_Results_I_Want(self):
        self.driver = SetUp.android_driver()
        os.system( main_UIcontrol.Restart )
        logging.info( "case_11" )
        self.driver.implicitly_wait( 5 )
        self.driver.find_element_by_xpath( main_UIcontrol.btn_APPname ).click()
        os.system( main_UIcontrol.btn_Mine )
        self.driver.find_element_by_xpath(main_UIcontrol.Personalpage_Like).click()
        self.driver.find_element_by_xpath(main_UIcontrol.Personalpage_FirstCard).click()

        # 循环查找带有挂品的视频
        i=0
        a = BaseOpera( self.driver )
        while i < 30:
            try: # 如果有就点击，点击后退出
                self.driver.find_element_by_xpath("xpath=//*[@text='上榜好物']")
                self.driver.find_element_by_xpath(main_UIcontrol.shortvideo_iteminfo).click()
                break
            except NoSuchElementException as e: # 如果在当前视频没有找到就继续滑动查找
                a.swipe_to_top()
                i += 1
        # 点击收藏按钮
        self.driver.find_element_by_xpath(main_UIcontrol.shortvideo_Favorite).click()
        self.driver.find_element_by_xpath( main_UIcontrol.shortvideo_unFavorite ).click()
        # 点击返回
        i = 0
        for i in range(3):
            self.driver.press_keycode( 4 )  # back

    def test_12_Goods_Results_Buy(self):
        self.driver = SetUp.android_driver()
        os.system( main_UIcontrol.Restart )
        logging.info( "case_12" )
        self.driver.implicitly_wait( 5 )
        self.driver.find_element_by_xpath( main_UIcontrol.btn_APPname ).click()
        os.system( main_UIcontrol.btn_Mine )
        self.driver.find_element_by_xpath( main_UIcontrol.Personalpage_Like ).click()
        self.driver.find_element_by_xpath( main_UIcontrol.Personalpage_FirstCard ).click()

        # 循环查找带有挂品的视频
        i = 0
        a = BaseOpera( self.driver )
        while i < 30:
            try:  # 如果有就点击，点击后退出
                self.driver.find_element_by_xpath( "xpath=//*[@text='上榜好物']" )
                self.driver.find_element_by_xpath( main_UIcontrol.shortvideo_iteminfo ).click()
                break
            except NoSuchElementException as e:  # 如果在当前视频没有找到就继续滑动查找
                a.swipe_to_top()
                i += 1
        # 点击收藏按钮
        self.driver.find_element_by_xpath(main_UIcontrol.shortvideo_Buying).click()
        # 点击返回
        i = 0
        for i in range( 3 ):
            self.driver.press_keycode( 4 )  # back

    def test_13_Goods_Results_Click_Avatar_Goods(self):
        self.driver = SetUp.android_driver()
        os.system( main_UIcontrol.Restart )
        logging.info( "case_13" )
        self.driver.implicitly_wait( 5 )
        self.driver.find_element_by_xpath( main_UIcontrol.btn_APPname ).click()
        os.system( main_UIcontrol.btn_Mine )
        self.driver.find_element_by_xpath( main_UIcontrol.Personalpage_Like ).click()
        self.driver.find_element_by_xpath( main_UIcontrol.Personalpage_FirstCard ).click()

        # 循环查找带有挂品的视频
        i = 0
        a = BaseOpera( self.driver )
        while i < 30:
            try:  # 如果有就点击，点击后退出
                self.driver.find_element_by_xpath( "xpath=//*[@text='上榜好物']" )
                self.driver.find_element_by_xpath( main_UIcontrol.shortvideo_iteminfo ).click()
                break
            except NoSuchElementException as e:  # 如果在当前视频没有找到就继续滑动查找
                a.swipe_to_top()
                i += 1
        # 点击收藏按钮
        self.driver.find_element_by_xpath(main_UIcontrol.shortvideo_Gotodetail).click()
        sleep(3)
        # 点击返回
        i = 0
        for i in range( 3 ):
            self.driver.press_keycode( 4 )  # back


    def test_14_Click_Recommend_Goods(self):
        self.driver = SetUp.android_driver()
        os.system( main_UIcontrol.Restart )
        logging.info( "case_14" )
        self.driver.implicitly_wait( 5 )
        self.driver.find_element_by_xpath( main_UIcontrol.btn_APPname ).click()
        os.system(main_UIcontrol.btn_Mine)
        self.driver.find_element_by_xpath(main_UIcontrol.Personalpage_Like).click()
        self.driver.find_element_by_xpath(main_UIcontrol.Personalpage_FirstCard).click()

        # 查找专门的视频
        i = 0
        a = BaseOpera( self.driver )
        while i < 20:
            try:  # 如果有就点击，点击后退出
                self.driver.find_element_by_xpath( "xpath=//*[@text='婆媳关系缩影']")
                self.driver.find_element_by_xpath( main_UIcontrol.shortvideo_iteminfo ).click()
                break
            except NoSuchElementException as e:  # 如果在当前视频没有找到就继续滑动查
                a.swipe_to_top()
                i += 1

        a.swipe_to_top()

        self.driver.find_element_by_xpath( "xpath=//*[@text='买家发布']" ).click()
        i = 0
        for i in range(4):
            self.driver.press_keycode( 4 )  # back

    def test_15_Show_Recommend_Goods(self):
        self.driver = SetUp.android_driver()
        os.system( main_UIcontrol.Restart )
        logging.info( "case_15" )
        self.driver.implicitly_wait( 5 )
        self.driver.find_element_by_xpath( main_UIcontrol.btn_APPname ).click()
        os.system( main_UIcontrol.btn_Mine )
        self.driver.find_element_by_xpath( main_UIcontrol.Personalpage_Like ).click()
        self.driver.find_element_by_xpath( main_UIcontrol.Personalpage_FirstCard ).click()

        # 查找专门的视频
        i = 0
        a = BaseOpera( self.driver )
        while i < 20:
            try:  # 如果有就点击，点击后退出
                self.driver.find_element_by_xpath( "xpath=//*[@text='婆媳关系缩影']" )
                self.driver.find_element_by_xpath( main_UIcontrol.shortvideo_iteminfo ).click()
                break
            except NoSuchElementException as e:  # 如果在当前视频没有找到就继续滑动查
                a.swipe_to_top()
                i += 1

        a.swipe_to_top()

        self.driver.find_element_by_xpath( "xpath=//*[@text='买家发布']" ).click()
        i = 0
        for i in range( 4 ):
            self.driver.press_keycode( 4 )  # back

    def test_59_Show_Avatar_Goods(self):
        self.driver = SetUp.android_driver()
        self.driver.implicitly_wait( 5 )
        os.system( main_UIcontrol.Restart )
        logging.info( "case_59" )
        self.driver.find_element_by_xpath( main_UIcontrol.btn_APPname ).click()
        self.driver.find_element_by_xpath( main_UIcontrol.btn_shortvideo ).click()
        i = 0
        a = BaseOpera( self.driver )
        while i < 50:
            try:  # 如果有就点击，点击后退出
                self.driver.find_element_by_xpath( main_UIcontrol.shortvideo_iteminfo ).click()
                sleep( 2 )
                break
            except NoSuchElementException as e:  # 如果在当前视频没有找到就继续滑动查找
                a.swipe_to_top()
                i += 1
        for i in range( 3 ):
            self.driver.press_keycode( 4 )

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()