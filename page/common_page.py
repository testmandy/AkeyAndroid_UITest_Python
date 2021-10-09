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

    def cancel_update(self):
        """如果发现更新提示，点击取消"""
        if self.driver.find_element('btn_update'):
            self.driver.click(1, 'tv_update_cancel')
        else:
            pass

    def back_to_main_screen(self):
        """如果发现不在一级页面，点击返回到一级页面"""
        while self.driver.find_element('tv_title_back'):
            self.driver.click(1, 'tv_title_back')
            print('[MyLog]--------返回上一页')

    def has_logged_in(self):
        """如果返回到一级页面发现是登录状态，执行退出登录"""
        while self.driver.find_element('tv_title_back'):
            self.driver.click(1, 'tv_title_back')
        if self.driver.find_element('tab_mine'):
            return True
        else:
            return False

    def choose_image(self):
        """选择第一张照片"""
        self.driver.click(3, 'id_item_images', 0)

    def click_confirm(self):
        """点击确认"""
        self.driver.click(1, 'button_confirm')

    def click_shutter(self):
        """点击拍照"""
        self.driver.click(1, 'shutter_button')

    def click_camera_btn_done(self):
        """点击确认发送"""
        self.driver.click(3, 'btn_done')

    def click_camera_btn_cancel(self):
        """点击取消发送"""
        self.driver.click(1, 'btn_cancel')

