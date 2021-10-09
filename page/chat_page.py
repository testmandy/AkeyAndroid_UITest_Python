# -*- coding: utf-8 -*-

# @Time : 2021/9/28 14:20
# @Author : Mandy
import time


class ChatPage:
    def __init__(self, driver):
        self.driver = driver

    def click_chatBox(self, i):
        """点击我的收藏"""
        self.driver.click(1, 'contact_avatar_img', i)

    def click_voice(self):
        """点击录音按钮"""
        self.driver.click(2, 'chat_voice_btn')

    def press_btn_voice(self):
        """点击录音按钮"""
        self.driver.long_press('chat_voice_btn')

    def send_message(self, msg):
        """输入信息"""
        self.driver.send_keys(1, 'chat_content', msg)

    def click_send(self):
        """点击发送"""
        self.driver.click(1, 'chat_normal_sendbtn')

    def click_more(self):
        """点击更多"""
        self.driver.click(1, 'chat_add_more_btn')

    def click_emoji(self):
        """点击表情"""
        self.driver.click(1, 'chat_emoji_btn')

    def click_photo(self):
        """点击照片"""
        self.driver.click(1, 'image_sml_btn')

    def click_camera(self):
        """点击相机"""
        self.driver.click(1, 'photo_sml_btn')

    def click_video(self):
        """点击视频"""
        self.driver.click(1, 'video_sml_btn')