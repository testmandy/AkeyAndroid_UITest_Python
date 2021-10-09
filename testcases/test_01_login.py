# -*- coding: utf-8 -*-

# @Time : 2021/9/28 14:40
# @Author : Mandy
import time

import pytest
from common.TestInit import Init


@pytest.mark.run
class TestLogin(Init):
    def setup_method(self):
        """每个测试用例执行之前做操作"""
        # 如果发现更新提示，点击取消
        if self.handle.find_element('btn_update'):
            self.handle.click(1, 'tv_update_cancel')
        else:
            pass
        # 如果发现不在一级页面，点击返回到一级页面
        while self.handle.find_element('tv_title_back'):
            self.handle.click(1, 'tv_title_back')
            print('[MyLog]--------返回上一页')
        # 如果返回到一级页面发现是登录状态，执行退出登录
        if self.handle.find_element('tab_mine'):
            self.logout()

    def logout(self):
        """前提是当前已经登录，登录成功"""
        self.common_page.click_tab_mine()
        self.mine_page.click_settings()
        self.handle.swipe_on('up')
        self.mine_page.click_logout()
        self.common_page.click_btn_sure()
        time.sleep(15)

    @pytest.mark.run
    def test_login_pass(self):
        """登录成功"""
        self.login_page.send_username('15356658837')
        self.login_page.send_password('lulu1314')
        self.login_page.click_accept()
        self.login_page.click_login()
        time.sleep(15)

    @pytest.mark.skip
    def test_login_user_error(self):
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

    @pytest.mark.skip
    def test_login_password_error(self):
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

