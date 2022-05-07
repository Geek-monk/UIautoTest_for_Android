# This test code uses the Appium python client.
# Please input  "pip install Appium-Python-Client" to Terminal
# -*- coding: utf-8 -*-
'''
==============================================
# @Time         : 2021/7/2 5:10 下午
# @Author       : Geekmonk
# @Software     : PyCharm
# @Project name :UT_AutomatedTesting
# Case name     : Swipescreen.py
==============================================
'''
class BaseOpera(object):
    '''
    基础操作
    '''
    def __init__(self, driver):
        self.driver = driver
        self.duration = 1000
    @property
    def width(self):
        '''获取屏幕宽度'''
        return self.driver.get_window_size()['width']
    @property
    def height(self):
        '''获取屏幕高度'''
        return self.driver.get_window_size()['height']
    def swipe_to_left(self, base=0.1):
        '''从右向左滑动'''
        return self.driver.swipe(self.width*(1-base),
                                    self.height*0.5,
                                    self.width*base,
                                    self.height*0.5,
                                    self.duration
                                    )
    def swipe_to_right(self, base=0.1):
        '''从左向右滑动'''
        return self.driver.swipe(self.width*base,
                                    self.height*0.5,
                                    self.width*(1-base),
                                    self.height*0.5,
                                    self.duration
                                    )
    def swipe_to_top(self, base=0.9):
        '''从下向上滑动'''
        return self.driver.swipe(self.width*0.5,
                                    self.height*base,
                                    self.width*0.5,
                                    self.height*(1-base),
                                    self.duration
                                    )
    def swipe_to_bottom(self, base=0.9):
        '''从上向下滑动'''
        return self.driver.swipe(self.width*0.5,
                                    self.height*(1-base),
                                    self.width*0.5,
                                    self.height*base,
                                    self.duration
                                    )
