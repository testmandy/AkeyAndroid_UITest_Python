# -*- coding: utf-8 -*-

# @Time : 2021/9/28 14:20
# @Author : Mandy
import time


class CommonPage:
    def __init__(self, driver):
        self.driver = driver

    def click_btn_cancel(self):
        """点击弹窗-取消"""
        self.driver.click(1, 'btn_n')

    def click_btn_sure(self):
        """点击弹窗-确认"""
        self.driver.click(1, 'btn_p')

    def click_back(self):
        """点击左上角返回"""
        self.driver.click(1, 'tv_title_back')

    def click_upper_search(self):
        """点击右上角-搜索"""
        self.driver.click(1, 'iv_search')

    def click_upper_more(self):
        """点击右上角-更多"""
        self.driver.click(1, 'more_btn')

    def click_tab_message(self):
        """点击tab_密信"""
        self.driver.click(1, 'tab_message')

    def click_tab_app(self):
        """点击tab_工作台"""
        self.driver.click(1, 'tab_app')

    def click_tab_contacts(self):
        """点击tab_好友"""
        self.driver.click(1, 'tab_contacts')

    def click_tab_news(self):
        """点击tab_资讯"""
        self.driver.click(1, 'tab_news')

    def click_tab_mine(self):
        """点击tab_我的"""
        self.driver.click(1, 'tab_mine')





