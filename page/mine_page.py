# -*- coding: utf-8 -*-

# @Time : 2021/9/28 14:20
# @Author : Mandy
import time


class MinePage:
    def __init__(self, driver):
        self.driver = driver

    def click_mycard(self):
        """点击头像"""
        self.driver.click(1, 'iv_modify')

    def click_edit_info(self):
        """点击编辑个人信息"""
        self.driver.click(1, 'rl_to_edit')

    def send_nickname(self, name):
        """输入我的昵称"""
        self.driver.send_keys(1, 'nickname_input', name)

    def send_signature(self, sign):
        """输入签名"""
        self.driver.send_keys(1, 'et_signature', sign)

    def click_save_info(self):
        """点击保存昵称签名修改"""
        self.driver.click(1, 'nickname_cfm_btn')

    def click_male(self):
        """点击性别-男"""
        self.driver.click(1, 'gender_radio_male')

    def click_female(self):
        """点击性别-女"""
        self.driver.click(1, 'gender_radio_female')

    def click_share(self):
        """点击分享邀请码"""
        self.driver.click(1, 'tv_share_akchat')

    def click_broadcast(self):
        """点击群发助手"""
        self.driver.send_keys(1, 'tv_broadcast_message')

    def click_settings(self):
        """点击设置"""
        self.driver.click(1, 'start_settings_layout')

    def click_id(self):
        """点击密信号"""
        self.driver.click(1, 'll_akid')

    def click_phone(self):
        """点击手机号"""
        self.driver.click(1, 'layout_cellphone')

    def click_email(self):
        """点击邮箱"""
        self.driver.click(1, 'layout_email_address')

    def click_address(self):
        """点击地址"""
        self.driver.click(1, 'layout_location')

    def click_logout(self):
        """点击地址"""
        self.driver.click(1, 'logout_btn')
