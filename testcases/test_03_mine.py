# -*- coding: utf-8 -*-

# @Time : 2021/9/28 14:40
# @Author : Mandy
import time

import pytest
from common.TestInit import Init


@pytest.mark.run
class TestMine(Init):
    def setup_method(self):
        time.sleep(5)
        """每个测试用例执行之前做操作"""
        # 如果发现更新提示，点击取消
        if self.handle.find_element('btn_update'):
            print(u'[MyLog]--------下次再说')
            self.handle.click(1, 'tv_update_cancel')
        else:
            print(u'[MyLog]--------不需要更新')
        # 如果发现不在一级页面，点击返回到一级页面
        while self.handle.find_element('tv_title_back'):
            self.handle.click(1, 'tv_title_back')
            print(u'[MyLog]--------返回上一页')
        # 如果发现当前没有登录，先登录
        if not self.handle.find_element('tab_mine'):
            self.login_pass()

    def login_pass(self):
        """登录成功"""
        self.login_page.send_username('15356658837')
        self.login_page.send_password('lulu1314')
        self.login_page.click_accept()
        self.login_page.click_login()
        time.sleep(15)

    @pytest.mark.run
    def test_edit_info(self):
        """修改个人信息"""
        time.sleep(2)
        self.common_page.click_tab_mine()
        self.mine_page.click_mycard()
        self.mine_page.click_edit_info()
        self.mine_page.send_nickname('万露test')
        self.mine_page.send_signature('test签名')
        self.mine_page.click_male()
        self.mine_page.click_save_info()
        time.sleep(2)

