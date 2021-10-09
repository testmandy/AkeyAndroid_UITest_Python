# -*- coding: utf-8 -*-

# @Time : 2021/9/28 14:40
# @Author : Mandy
import time

import pytest
from common.TestInit import Init


@pytest.mark.run
class TestServer(Init):
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
        time.sleep(15)

    @pytest.mark.run
    def test_search_success(self):
        """查询服务器"""
        self.login_page.click_chooseServer()
        self.login_page.send_server('perftest')
        self.login_page.click_joinServer()

    @pytest.mark.run
    def test_search_failed(self):
        """查询服务器"""
        self.login_page.click_chooseServer()
        self.login_page.send_server('p')
        self.login_page.click_joinServer()

    @pytest.mark.run
    def test_search_failed2(self):
        """查询服务器"""
        self.login_page.click_chooseServer()
        self.login_page.send_server('ppppppppppppppppppppppppppppppppppppppppppppppp')
        self.login_page.click_joinServer()

    @pytest.mark.run
    def test_scan_failed(self):
        """查询服务器"""
        self.login_page.click_chooseServer()
        self.login_page.click_scan()
        self.login_page.click_qr_image()
        self.common_page.choose_image()
        self.common_page.click_confirm()
        self.common_page.click_btn_sure()


