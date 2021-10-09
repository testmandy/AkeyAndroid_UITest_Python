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

    @pytest.mark.skip
    def test_favorite(self):
        # 点击密信
        self.common_page.click_tab_message()
        # 点击我的收藏
        self.chat_page.click_chatBox(0)
        self.handle.capture('my_favorite')
        # 点击录音键
        self.chat_page.click_voice()
        # 点击或长按录音
        # self.chat_page.press_btn_voice()
        # 输入文字发送
        self.chat_page.send_message('test123456')
        # 点击发送按钮
        self.chat_page.click_send()
        self.handle.capture('message')
        # 点击更多
        self.chat_page.click_more()

    @pytest.mark.run
    def test_chat(self):
        # 点击密信
        self.common_page.click_tab_message()
        # 点击我的收藏
        self.chat_page.click_chatBox(1)
        # 点击录音键
        self.chat_page.click_voice()
        # 输入文字发送
        self.chat_page.send_message('test123456')
        # 点击发送按钮
        self.chat_page.click_send()
        self.handle.capture('message')
        # 点击图片
        self.chat_page.click_photo()
        # 选择第一张照片
        self.common_page.choose_image()
        # 点击确认发送
        self.common_page.click_confirm()
        # 点击相机
        self.chat_page.click_camera()
        # 点击拍照
        self.common_page.click_shutter()
        # 点击确认
        self.common_page.click_camera_btn_done()
        self.handle.capture('message')
        # 点击更多
        self.chat_page.click_more()
