# -*- coding: utf-8 -*-

# @Time : 2021/9/28 14:20
# @Author : Mandy
import time


class FriendsPage:
    def __init__(self, driver):
        self.driver = driver

    def click_add_friend(self):
        """点击添加好友"""
        self.driver.click(1, 'add_user_txt')

    def click_chanel(self):
        """点击频道"""
        self.driver.click(1, 'tv_chanel')

    def click_bot(self):
        """点击机器人"""
        self.driver.click(1, 'tv_bot')

    def click_address_book(self):
        """点击通讯录"""
        self.driver.click(1, 'address_book_tv')

    def click_manage_group(self):
        """点击我管理的群组"""
        self.driver.click(1, 'group')

    def click_my_group(self):
        """点击我加入的群组"""
        self.driver.click(1, 'group')

    def click_friends_list(self):
        """点击好友列表"""
        self.driver.click(1, 'group')

    def click_global_search(self):
        """点击搜索手机号/密信号"""
        self.driver.click(1, 'global_search_input')







