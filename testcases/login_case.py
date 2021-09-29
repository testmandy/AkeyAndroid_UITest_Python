# -*- coding: utf-8 -*-

# @Time : 2021/9/28 14:40
# @Author : Mandy
from page.login_page import LoginPage


class LoginCase:
    def __init__(self):
        self.login_page = LoginPage()

    def login_pass(self):
        """登录成功"""
        self.login_page.send_username('15356658837')
        self.login_page.send_password('lulu1314')
        self.login_page.click_accept()
        self.login_page.click_login()

    def login_user_error(self):
        """登录成功"""
        self.login_page.send_username('15012345678')
        self.login_page.send_password('123456')
        self.login_page.click_accept()
        self.login_page.click_login()
        user_flag = self.login_page.get_fail_toast('账号未注册')
        if user_flag:
            return True
        else:
            return False

    def login_password_error(self):
        """登录成功"""
        self.login_page.send_username('15356658837')
        self.login_page.send_password('123456')
        self.login_page.click_accept()
        self.login_page.click_login()
        user_flag = self.login_page.get_fail_toast('登录密码错误')
        if user_flag:
            return True
        else:
            return False

