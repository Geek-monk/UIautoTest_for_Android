# This test code uses the Appium python client.
# Please input  "pip install Appium-Python-Client" to Terminal
# -*- coding: utf-8 -*-
'''
=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=
# @Time         : 2021/8/5 5:46 下午
# @Author       : Geekmonk
# @Software     : PyCharm
# @Project name :UT_AutomatedTesting
# Case name     :test_Jump_SPMurl_value.py
=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=
'''
import logging
import unittest, os
from time import sleep
from modules import SetUp
from modules.swipescreen import BaseOpera
from modules import main_UIcontrol
from selenium.common.exceptions import NoSuchElementException


class Jump_SPMurl_value( unittest.TestCase ):

    def test_61_From_xxx_Follow_into(self):
        self.driver = SetUp.android_driver()
        os.system( main_UIcontrol.Restart )
        logging.info( "case_61" )
        self.driver.implicitly_wait( 5 )
        self.driver.find_element_by_xpath( main_UIcontrol.btn_xxx ).click()
        self.driver.find_element_by_xpath( main_UIcontrol.btn_shortvideo ).click()
        self.driver.find_element_by_xpath( main_UIcontrol.btn_xxx ).click()
        self.driver.find_element_by_xpath( main_UIcontrol.btn_Favoritebotton ).click()
        self.driver.find_element_by_xpath( main_UIcontrol.btn_shortvideo ).click()
        os.system( main_UIcontrol.Restart )

    def test_62_killprocess_enter(self):
        self.driver = SetUp.android_driver()
        os.system( main_UIcontrol.Restart )
        logging.info( "case_62" )
        self.driver.implicitly_wait( 5 )
        self.driver.find_element_by_xpath( main_UIcontrol.btn_shortvideo ).click()
        os.system( "adb shell am force-stop com.xxxxx.xxx" )
        os.system( "adb shell am start com.xxxxx.xxx/.SplashActivity" )
        self.driver.implicitly_wait( 5 )

        try:
            self.driver.find_element_by_xpath( "xpath=//*[@resource-id='com.xxxxx.xxx:id/tv_teenager_ok']" ).click()
        except NoSuchElementException as e:
            os.system( main_UIcontrol.Restart )

    def test_63_underfollow_shortvideo(self):
        self.driver = SetUp.android_driver()
        os.system( main_UIcontrol.Restart )
        logging.info( "case_63" )
        self.driver.implicitly_wait( 5 )
        self.driver.find_element_by_xpath( main_UIcontrol.btn_Favoritebotton ).click()
        i = 0
        while i < 10:
            try:
                self.driver.find_element_by_xpath( main_UIcontrol.btn_Shortvideo_undermainpage ).click()
                break
            except NoSuchElementException as e:
                os.system( main_UIcontrol.Restart )
                i += 1
        self.driver.press_keycode( 4 )

    def test_64_Search_into(self):
        self.driver = SetUp.android_driver()
        os.system( main_UIcontrol.Restart )
        logging.info( "case_64" )
        self.driver.implicitly_wait( 5 )
        self.driver.find_element_by_xpath( main_UIcontrol.btn_xxx ).click()
        self.driver.find_element_by_xpath( main_UIcontrol.btn_search ).click()
        self.driver.find_element_by_xpath( main_UIcontrol.btn_SearchInput ).click()
        os.system( "adb shell am broadcast -a ADB_INPUT_TEXT --es msg '李佳琦'" )
        os.system( "adb shell input keyevent KEYCODE_ENTER" )
        self.driver.find_element_by_xpath( "xpath=//*[@text='视频']" ).click()
        self.driver.find_element_by_xpath( main_UIcontrol.btn_search_Videocard ).click()
        for i in range( 3 ):
            self.driver.press_keycode( 4 )  # back

    def test_65_Discovery_Shortvideo(self):
        self.driver = SetUp.android_driver()
        os.system( main_UIcontrol.Restart )
        logging.info( "case_65" )
        self.driver.implicitly_wait( 5 )
        self.driver.find_element_by_xpath( main_UIcontrol.btn_discover ).click()
        self.driver.find_element_by_xpath( main_UIcontrol.Discovery_Month ).click()
        self.driver.find_element_by_xpath( main_UIcontrol.Discovery_First_Card ).click()
        i = 0
        a = BaseOpera( self.driver )
        while i < 10:
            try:
                self.driver.find_element_by_xpath( "xpath=//*[@text='买家发布']" ).click()
                break
            except NoSuchElementException as e:
                a.swipe_to_top()
                i += 1
        self.driver.press_keycode( 4 )

    def test_66_goods_video(self):
        self.driver = SetUp.android_driver()
        os.system( main_UIcontrol.Restart )
        logging.info( "case_66" )
        self.driver.implicitly_wait( 5 )
        self.driver.find_element_by_xpath( main_UIcontrol.btn_xxx ).click()
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

    def test_67_shake(self):
        self.driver = SetUp.android_driver()
        os.system( main_UIcontrol.Restart )
        logging.info( "case_67" )
        self.driver.implicitly_wait( 5 )
        os.system( main_UIcontrol.YuanbaoCenter )
        try:
            self.driver.find_element_by_xpath( main_UIcontrol.Personalpage_DollarCentre_close1 ).click()
        except NoSuchElementException as e:
            print( "尝试点击第一个关闭按钮" )
        try:
            self.driver.find_element_by_xpath( main_UIcontrol.Personalpage_DollarCentre_close2 ).click()
        except NoSuchElementException as e:
            print( "尝试点击第二个关闭按钮" )
        try:
            self.driver.find_element_by_xpath( main_UIcontrol.Personalpage_DollarCentre_close3 ).click()
        except NoSuchElementException as e:
            print( "尝试点击第三个关闭按钮" )
        self.driver.find_element_by_xpath( "xpath=//*[@text='摇一摇']" ).click()

        try:
            self.driver.find_element_by_xpath( "xpath=//*[@text='仅使用期间允许']" ).click()
        except NoSuchElementException as e:
            pass
        try:
            self.driver.find_element_by_xpath( "xpath=//*[@text='TB1TJ.yhhvbeK8jSZPfXXariXXa-80-80']" ).click()
        except NoSuchElementException as e:
            self.driver.find_element_by_xpath(
                "xpath=((((//*[@id='page']/*[@class='android.view.View'])[2]/*[@class='android.view.View'])[2]/*[@class='android.view.View'])[1]/*[@class='android.view.View'])[2]" ).click()
        self.driver.find_element_by_xpath( "xpath=//*[contains(@text, '看视频')]" ).click()

        i = 0
        for i in range( 7 ):
            sleep( 5 )
            a = BaseOpera( self.driver )
            a.swipe_to_top()
        i += 1

        for i in range( 3 ):
            self.driver.press_keycode( 4 )

    def test_68_Personalpage_Video(self):
        self.driver = SetUp.android_driver()
        os.system( main_UIcontrol.Restart )
        logging.info( "case_68" )
        self.driver.implicitly_wait( 5 )
        os.system( main_UIcontrol.Mine )
        self.driver.find_element_by_xpath( main_UIcontrol.Personalpage_Video ).click()
        self.driver.find_element_by_xpath( main_UIcontrol.Personalpage_FirstCard ).click()
        self.driver.press_keycode( 4 )

    def test_69_Personalpage_into_collection(self):
        self.driver = SetUp.android_driver()
        os.system( main_UIcontrol.Restart )
        logging.info( "case_69" )
        self.driver.implicitly_wait( 5 )
        os.system( main_UIcontrol.Mine )
        self.driver.find_element_by_xpath( main_UIcontrol.Personalpage_collection ).click()
        self.driver.find_element_by_xpath( "xpath=//*[@text='看视频']" ).click()
        sleep( 2 )
        self.driver.press_keycode( 4 )

    def test_70_collection_into_video(self):
        self.driver = SetUp.android_driver()
        os.system( main_UIcontrol.Restart )
        logging.info( "case_70" )
        self.driver.implicitly_wait( 5 )
        os.system( main_UIcontrol.Mine )
        self.driver.find_element_by_xpath( main_UIcontrol.Personalpage_collection ).click()
        # 查找专门的视频
        i = 0
        a = BaseOpera( self.driver )
        while i < 20:
            try:  # 如果有就点击，点击后退出
                self.driver.find_element_by_xpath( "xpath=//*[@text='这个家，有这样的婆婆，还有这样的他']" ).click()
                break
            except NoSuchElementException as e:  # 如果在当前视频没有找到就继续滑动查
                a.swipe_to_top()
                i += 1
        self.driver.press_keycode( 4 )

    def test_71_Personalpage_Like_into_video(self):
        self.driver = SetUp.android_driver()
        os.system( main_UIcontrol.Restart )
        logging.info( "case_71" )
        self.driver.implicitly_wait( 5 )
        os.system( main_UIcontrol.Mine )
        self.driver.find_element_by_xpath( main_UIcontrol.Personalpage_Like ).click()
        self.driver.find_element_by_xpath( main_UIcontrol.Personalpage_FirstCard ).click()
        self.driver.press_keycode( 4 )

    def test_72_Hashtag_into_video(self):
        self.driver = SetUp.android_driver()
        os.system( main_UIcontrol.Restart )
        logging.info( "case_72" )
        self.driver.implicitly_wait( 5 )
        os.system( main_UIcontrol.Mine )
        self.driver.find_element_by_xpath( main_UIcontrol.Personalpage_Video ).click()
        self.driver.find_element_by_xpath( main_UIcontrol.Personalpage_FirstCard ).click()
        # 查找专门的视频
        i = 0
        a = BaseOpera( self.driver )
        while i < 20:
            try:  # 如果有就点击，点击后退出
                self.driver.find_element_by_xpath( "xpath=//*[@text='#为中国点赞']" ).click()
                break
            except NoSuchElementException as e:  # 如果在当前视频没有找到就继续滑动查
                a.swipe_to_top()
                i += 1
        self.driver.find_element_by_xpath( main_UIcontrol.shortvideo_Hashtag_video ).click()
        sleep( 2 )
        for i in range( 3 ):
            self.driver.press_keycode( 4 )

    def test_73_film_into_video(self):
        self.driver = SetUp.android_driver()
        os.system( main_UIcontrol.Restart )
        logging.info( "case_73" )
        self.driver.implicitly_wait( 5 )
        os.system( main_UIcontrol.Mine )
        self.driver.find_element_by_xpath( main_UIcontrol.Personalpage_Like ).click()
        self.driver.find_element_by_xpath( main_UIcontrol.Personalpage_FirstCard ).click()

        # 查找专门的视频
        i = 0
        a = BaseOpera( self.driver )
        while i < 20:
            try:  # 如果有就点击，点击后退出
                self.driver.find_element_by_xpath( "xpath=//*[@text='此处有同系列合集']" ).click()
                break
            except NoSuchElementException as e:  # 如果在当前视频没有找到就继续滑动查
                a.swipe_to_top()
                i += 1
        self.driver.find_element_by_xpath( "xpath=//*[@text='第1集 | ] 儿子#我在追剧']" ).click()
        sleep( 2 )
        for i in range( 3 ):
            self.driver.press_keycode( 4 )

    def test_74_YuanbaoCenter_video(self):
        self.driver = SetUp.android_driver()
        os.system( main_UIcontrol.Restart )
        logging.info( "case_74" )
        self.driver.implicitly_wait( 5 )
        os.system( main_UIcontrol.YuanbaoCenter )
        try:
            self.driver.find_element_by_xpath( main_UIcontrol.Personalpage_DollarCentre_close1 ).click()
        except NoSuchElementException as e:
            print( "尝试点击第一个关闭按钮" )
        try:
            self.driver.find_element_by_xpath( main_UIcontrol.Personalpage_DollarCentre_close2 ).click()
        except NoSuchElementException as e:
            print( "尝试点击第二个关闭按钮" )
        try:
            self.driver.find_element_by_xpath( main_UIcontrol.Personalpage_DollarCentre_close3 ).click()
        except NoSuchElementException as e:
            print( "尝试点击第三个关闭按钮" )
        i = 0
        a = BaseOpera( self.driver )
        while i < 10:
            try:
                self.driver.find_element_by_xpath( "xpath=//*[@text='看视频，嘻嘻哈哈']" ).click()
                sleep( 4 )
                break
            except NoSuchElementException as e:
                a.swipe_to_top()
                i += 1
        self.driver.press_keycode( 4 )

    def test_75_YuanbaoCenter_ADvideo(self):
        self.driver = SetUp.android_driver()
        os.system( main_UIcontrol.Restart )
        logging.info( "case_75" )
        self.driver.implicitly_wait( 5 )
        os.system( main_UIcontrol.YuanbaoCenter )
        try:
            self.driver.find_element_by_xpath( main_UIcontrol.Personalpage_DollarCentre_close1 ).click()
        except NoSuchElementException as e:
            print( "尝试点击第一个关闭按钮" )
        try:
            self.driver.find_element_by_xpath( main_UIcontrol.Personalpage_DollarCentre_close2 ).click()
        except NoSuchElementException as e:
            print( "尝试点击第二个关闭按钮" )
        try:
            self.driver.find_element_by_xpath( main_UIcontrol.Personalpage_DollarCentre_close3 ).click()
        except NoSuchElementException as e:
            print( "尝试点击第三个关闭按钮" )
        i = 0
        a = BaseOpera( self.driver )
        while i < 10:
            try:
                self.driver.find_element_by_xpath( "xpath=//*[@text='看视频']" ).click()
                sleep( 4 )
                break
            except NoSuchElementException as e:
                a.swipe_to_top()
                i += 1
        self.driver.press_keycode( 4 )

    def test_76_halfpage_video(self):
        self.driver = SetUp.android_driver()
        os.system( main_UIcontrol.Restart )
        logging.info( "case_76" )
        self.driver.implicitly_wait( 5 )
        os.system( main_UIcontrol.Somebodyxxxroom )
        self.driver.find_element_by_xpath( main_UIcontrol.xxxroom_Avatar ).click()
        self.driver.find_element_by_xpath( main_UIcontrol.xxxroom_FirstCard ).click()
        sleep( 3 )
        for i in range( 3 ):
            self.driver.press_keycode( 4 )

    def test_77_YuanbaoCenter_walking(self):
        self.driver = SetUp.android_driver()
        os.system( main_UIcontrol.Restart )
        logging.info( "case_77" )
        self.driver.implicitly_wait( 5 )
        os.system( main_UIcontrol.YuanbaoCenter )
        try:
            self.driver.find_element_by_xpath( main_UIcontrol.Personalpage_DollarCentre_close1 ).click()
        except NoSuchElementException as e:
            print( "尝试点击第一个关闭按钮" )
        try:
            self.driver.find_element_by_xpath( main_UIcontrol.Personalpage_DollarCentre_close2 ).click()
        except NoSuchElementException as e:
            print( "尝试点击第二个关闭按钮" )
        try:
            self.driver.find_element_by_xpath( main_UIcontrol.Personalpage_DollarCentre_close3 ).click()
        except NoSuchElementException as e:
            print( "尝试点击第三个关闭按钮" )
        self.driver.find_element_by_xpath( "xpath=//*[@text='支付宝运动']" ).click()
        try:
            self.driver.find_element_by_xpath( "xpath=//*[@text='始终允许']" ).click()
        except NoSuchElementException as e:
            pass
        self.driver.find_element_by_xpath( "xpath=//*[@text='支付宝赚步数']" ).click()
        self.driver.find_element_by_xpath( "xpath=//*[contains(@text, '支付宝看视频')]" ).click()
        sleep( 5 )
        self.driver.press_keycode( 4 )
        self.driver.find_element_by_xpath( "xpath=//*[@text='残忍离开']" ).click()
        for i in range( 4 ):
            self.driver.press_keycode( 4 )

    def test_78_YuanbaoCenter_Workinjob(self):
        self.driver = SetUp.android_driver()
        os.system( main_UIcontrol.Restart )
        logging.info( "case_78" )
        self.driver.implicitly_wait( 5 )
        os.system( main_UIcontrol.YuanbaoCenter )
        try:
            self.driver.find_element_by_xpath( main_UIcontrol.Personalpage_DollarCentre_close1 ).click()
        except NoSuchElementException as e:
            print( "尝试点击第一个关闭按钮" )
        try:
            self.driver.find_element_by_xpath( main_UIcontrol.Personalpage_DollarCentre_close2 ).click()
        except NoSuchElementException as e:
            print( "尝试点击第二个关闭按钮" )
        try:
            self.driver.find_element_by_xpath( main_UIcontrol.Personalpage_DollarCentre_close3 ).click()
        except NoSuchElementException as e:
            print( "尝试点击第三个关闭按钮" )
        self.driver.find_element_by_xpath( "xpath=//*[@text='打工赚抖币']" ).click()

        self.driver.find_element_by_xpath(
            "xpath=//*[@text='O1CN01SksiDb1OoSa2Pknzh_!!6000000001752-2-tps-147-152']" ).click()
        self.driver.find_element_by_xpath( "xpath=//*[contains(@text, '看视频')]" ).click()
        sleep( 5 )
        self.driver.press_keycode( 4 )
        self.driver.find_element_by_xpath( "xpath=//*[@text='残忍离开']" ).click()
        for i in range( 4 ):
            self.driver.press_keycode( 4 )

    def test_79_push(self):
        self.driver = SetUp.android_driver()
        os.system( main_UIcontrol.Restart )
        logging.info( "case_78" )
        self.driver.implicitly_wait( 5 )
        os.system( main_UIcontrol.Mine )
        self.driver.find_element_by_xpath( main_UIcontrol.Personalpage_Scan ).click()
        try:
            self.driver.find_element_by_xpath( "xpath=//*[@text='始终允许']" ).click()
        except NoSuchElementException as e:
            pass
        self.driver.find_element_by_xpath( "xpath=//*[@text='相册']" ).click()

        try:
            self.driver.find_element_by_xpath( "xpath=//*[@text='始终允许']" ).click()
        except NoSuchElementException as e:
            pass
        self.driver.find_element_by_xpath( "xpath=//*[@text='图库']" ).click()
        self.driver.find_element_by_xpath( "xpath=//*[@text='appium测试使用']" ).click()
        self.driver.find_element_by_xpath( "xpath=//*[@resource-id='com.android.gallery3d:id/top_frame']" ).click()
        self.driver.find_element_by_xpath(
            "xpath=//*[@resource-id='com.android.gallery3d:id/head_select_right']" ).click()
        sleep( 3 )
        for i in range( 3 ):
            self.driver.press_keycode( 4 )


if __name__ == '__main__':
    unittest.main()
