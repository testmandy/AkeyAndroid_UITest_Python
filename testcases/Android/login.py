# -*- coding: utf-8 -*-

# @Time : 2021/9/24 14:42
# @Author : Mandy
import time
import unittest

from common.base_driver import BaseDriver
from utils.handle import Handle
from utils.server import Server


class Login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 必须使用@classmethod 装饰器,所有test运行前运行一次
        global handle, driver
        # 调用get_driver
        server = Server()
        server.main()
        base_driver = BaseDriver(0)
        driver = base_driver.android_driver()
        # 实例化handle
        handle = Handle(driver)

    @classmethod
    def tearDownClass(cls):
        # 必须使用 @ classmethod装饰器, 所有test运行完后运行一次
        print(u'[MyLog]--------关闭driver')
        driver.quit()

    def setUp(self):
        # 每个测试用例执行之前做操作
        print('------------------setup----------------')
        # 如果发现更新提示，点击取消
        if handle.find_element('btn_update'):
            handle.click(1, 'tv_update_cancel')
        else:
            pass

    def tearDown(self):
        # 每个测试用例执行之后做操作
        print(u'[MyLog]--------用例执行完成，开始执行下一个')

    def guide(self):
        # 点击同意协议
        handle.click(1, 'tvAgree')
        # 获取截屏
        handle.capture("tvAgree")

    def join(self):
        # 点击加入企业密信
        handle.click(1, 'join_server_btn')
        # 获取截屏
        handle.capture("join_server_btn")

    def search(self):
        # 输入服务器名
        handle.send_keys(1, 'edit_enterprise_name', 'akeychat')
        # 点击确认
        handle.click(3, 'sure')

    def phoneLogin(self):
        # 输入手机号
        handle.send_keys(3, 'accountInput', '15356658837')
        # 输入密码
        handle.send_keys(1, 'codeInput', 'lulu1314')
        # 如果协议没有被勾选，点击同意协议
        print('[MyLog]--------元素是否被选中' )
        # if not handle.element_is_selected('check_privacy'):
        if not driver.find_element_by_id('com.view.asim.enterprise:id/check_privacy'):
            print('[MyLog]--------点击同意协议')
            handle.click(1, 'check_privacy')
        # 点击登录
        handle.click(1, 'realLogin')
        time.sleep(15)

    def changeServer(self):
        # 点击换一个
        handle.click(1, 'choose_server')
        self.search()

    def logout(self):
        # 如果当前不在一级页面，一直点击返回按钮
        while handle.find_element('tv_title_back'):
            handle.click(1, 'tv_title_back')
            print('[MyLog]--------返回上一页')
        # 点击我的
        handle.click(1, 'tab_mine')
        # 点击设置
        handle.click(1, 'start_settings_layout')
        # 页面上滑
        handle.swipe_on('up')
        # 点击退出登录
        handle.click(1, 'logout_btn')
        # 弹窗点击确认
        handle.click(1, 'btn_p')
        time.sleep(10)

    def favorite(self):
        # 点击我的收藏
        handle.click(1, 'chatBoxs', 0)
        # 长按录音键
        handle.tap_long('chat_voice_btn', 3)
        # 输入文字发送
        handle.send_keys(1, 'chat_content', 'test123456')
        # 键盘发送，66代表键盘的enter
        driver.keyevent(66)
        # 点击更多
        handle.click(1, 'chat_add_more_btn')