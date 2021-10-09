# -*- coding: utf-8 -*-

# @Time : 2021/9/28 14:40
# @Author : Mandy
import time

import pytest
from common.TestInit import Init


@pytest.mark.run
class TestMine(Init):
    def setup_method(self):
        """
        如果发现更新提示，点击取消
        如果发现当前没有登录，先登录
        """
        self.common_page.cancel_update()
        if not self.common_page.has_logged_in():
            self.common_page.login_pass()

    @pytest.mark.run
    def test_edit_info(self):
        """修改个人信息"""
        time.sleep(2)
        self.common_page.click_tab_mine()
        self.mine_page.click_mycard()
        self.mine_page.click_edit_info()
        self.mine_page.send_nickname('test210000000000')
        self.mine_page.send_signature('test签名')
        self.mine_page.click_male()
        self.mine_page.click_save_info()
        time.sleep(2)

