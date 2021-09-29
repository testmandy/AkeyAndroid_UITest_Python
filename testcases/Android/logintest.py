# -*- coding: utf-8 -*-

# @Time : 2021/9/24 14:42
# @Author : Mandy
import time
from common.Init import TestInit


class Test(TestInit):
    def setUp(self):
        # 每个测试用例执行之前做操作
        print('------------------setup----------------')
        # 如果发现更新提示，点击取消
        if self.handle.find_element('btn_update'):
            self.handle.click(1, 'tv_update_cancel')
        else:
            pass

    def tearDown(self):
        # 每个测试用例执行之后做操作
        print(u'[MyLog]--------用例执行完成，开始执行下一个')

    def guide(self):
        # 点击同意协议
        self.handle.click(1, 'tvAgree')
        # 获取截屏
        self.handle.capture("tvAgree")

    def join(self):
        # 点击加入企业密信
        self.handle.click(1, 'join_server_btn')
        # 获取截屏
        self.handle.capture("join_server_btn")

    def search(self):
        # 输入服务器名
        self.handle.send_keys(1, 'edit_enterprise_name', 'akeychat')
        # 点击确认
        self.handle.click(1, 'sure')
        time.sleep(5)
        self.handle.capture('search')

    def phoneLogin(self):
        if self.handle.find_element('accountInput'):
            # 输入手机号
            self.handle.send_keys(2, 'accountInput', '15356658837')
            # 输入密码
            self.handle.send_keys(1, 'codeInput', 'lulu1314')
            # 如果协议没有被勾选，点击同意协议
            # self.handle.element_is_selected('check_privacy'):
            # self.handle.click(1, 'check_privacy')
            # 点击登录
            self.handle.click(1, 'realLogin')
            time.sleep(10)
            self.handle.capture('login')
        else:
            assert 'Failed-------没有找到登录页面哦'

    def changeServer(self):
        # 点击换一个
        if self.handle.get_element('choose_server'):
            self.handle.capture('choose_server')
            self.handle.click(1, 'choose_server')
            self.search()
        else:
            assert 'Failed-------没有找到登录页面哦'

    def logout(self):
        # 如果当前不在一级页面，一直点击返回按钮
        while self.handle.find_element('tv_title_back'):
            self.handle.click(1, 'tv_title_back')
            print('[MyLog]--------返回上一页')
        # 点击我的
        self.handle.click(1, 'tab_mine')
        self.handle.capture('tab_mine')
        # 点击设置
        self.handle.click(1, 'start_settings_layout')
        # 页面上滑
        self.handle.swipe_on('up')
        self.handle.capture('logout')
        # 点击退出登录
        self.handle.click(1, 'logout_btn')
        # 弹窗点击确认
        self.handle.click(1, 'btn_p')
        time.sleep(20)

    def favorite(self):
        # 如果当前不在一级页面，一直点击返回按钮
        while self.handle.find_element('tv_title_back'):
            self.handle.click(1, 'tv_title_back')
            print('[MyLog]--------返回上一页')
        # 点击密信
        self.handle.click(1, 'tab_message')
        # 点击我的收藏
        self.handle.click(1, 'contact_avatar_img', 0)
        self.handle.capture('my_favorite')
        # 点击录音键
        self.handle.click(3, 'chat_voice_btn')
        # 点击或长按录音
        # self.handle.tap_test('record_button')
        self.handle.long_press('voice_record_img')
        # 输入文字发送
        self.handle.send_keys(1, 'chat_content', 'test123456')
        # 点击发送按钮
        self.handle.click(1, 'chat_normal_sendbtn')
        self.handle.capture('message')
        # 点击更多
        self.handle.click(1, 'chat_add_more_btn')

    def test(self):
        flag = self.driver.find_element_by_id('com.view.asim.enterprise:id/check_privacy').is_selected()
        print(flag)
        if not flag:
            self.handle.click(1, 'check_privacy')