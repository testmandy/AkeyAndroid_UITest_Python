# -*- coding: utf-8 -*-

# @Time : 2021/9/28 14:20
# @Author : Mandy
import time


class RegisterPage:
    def __init__(self, driver):
        self.driver = driver

    def click_get_code(self):
        """注册页面-点击获取验证码"""
        self.driver.click(1, 'sign_continue')

    def click_goLogin(self):
        """注册页面-点击去登录"""
        self.driver.click(1, 'to_login')

    def send_phone(self, phone):
        """忘记密码-输入手机号码"""
        self.driver.send_keys(1, 'accountInput', phone)

    def click_next(self):
        """忘记密码-点击下一步"""
        self.driver.click(1, 'nextStep')


