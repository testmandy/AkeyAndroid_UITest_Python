# -*- coding: utf-8 -*-

# @Time : 2021/9/24 14:42
# @Author : Mandy

from common.Init import TestInit


class Chat(TestInit):

    def setUp(self):
        # 每个测试用例执行之前做操作
        print('------------------setup----------------')
        # 如果发现更新提示，点击取消
        # if handle.find_element('btn_update'):
        #     handle.click(1, 'tv_update_cancel')
        # else:
        #     pass

    def tearDown(self):
        # 每个测试用例执行之后做操作
        print(u'[MyLog]--------用例执行完成，开始执行下一个')

    def favorite(self):
        # 点击我的收藏
        self.handle.click(1, 'chatBoxs', 0)
        # 长按录音键
        self.handle.tap_test('chat_voice_btn', 3)
        # 输入文字发送
        self.handle.send_keys(1, 'chat_content', 'test123456')
        # 键盘发送，66代表键盘的enter
        self.driver.keyevent(66)
        # 点击更多
        self.handle.click(1, 'chat_add_more_btn')
