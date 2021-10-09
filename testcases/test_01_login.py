# -*- coding: utf-8 -*-

# @Time : 2021/9/28 14:40
# @Author : Mandy
import time

import pytest
from common.TestInit import Init


@pytest.mark.run
class TestLogin(Init):
    def setup_method(self):
        """
        如果发现更新提示，点击取消
        如果已登录则退出登录
        """
        self.common_page.cancel_update()
        if self.common_page.has_logged_in():
            self.logout()

    def logout(self):
        """前提是当前已经登录，登录成功"""
        self.common_page.click_tab_mine()
        self.mine_page.click_settings()
        self.handle.swipe_on('up')
        self.mine_page.click_logout()
        self.common_page.click_btn_sure()
        time.sleep(10)

    @pytest.mark.run
    def test_login_pass(self):
        """登录成功"""
        self.login_page.send_username('21000000000')
        self.login_page.send_password('q11111111')
        self.login_page.click_accept()
        self.login_page.click_login()
        time.sleep(10)

    @pytest.mark.skip
    def test_login_user_error(self):
        """登录成功"""
        self.login_page.send_username('000000')
        self.login_page.send_password('123456')
        self.login_page.click_accept()
        self.login_page.click_login()
        user_flag = self.login_page.get_fail_toast('账号未注册')
        if user_flag:
            return True
        else:
            return False

    @pytest.mark.skip
    def test_login_password_error(self):
        """登录成功"""
        self.login_page.send_username('210000000000')
        self.login_page.send_password('123456')
        self.login_page.click_accept()
        self.login_page.click_login()
        user_flag = self.login_page.get_fail_toast('登录密码错误')
        if user_flag:
            return True
        else:
            return False

