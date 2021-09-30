# -*- coding: utf-8 -*-

# @Time : 2021/9/28 14:20
# @Author : Mandy
import time


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def click_chooseServer(self):
        """点击换一个服务器"""
        self.driver.click(1, 'choose_server')

    def send_server(self, server):
        """输入服务器名"""
        self.driver.send_keys(1, 'edit_enterprise_name', server)

    def click_joinServer(self):
        """点击加入服务器"""
        self.driver.click(1, 'sure')

    def send_username(self, user):
        """输入用户名"""
        self.driver.send_keys(1, 'accountInput', user)

    def send_password(self, password):
        """输入密码"""
        self.driver.send_keys(1, 'codeInput', password)

    def click_accept(self):
        """点击同意协议"""
        # if not self.driver.find_element_by_id('com.view.asim.enterprise:id/check_privacy').is_selected():
        if not self.driver.get_element('check_privacy').is_selected():
            self.driver.click(1, 'check_privacy')

    def click_login(self):
        """点击登录"""
        self.driver.click(1, 'realLogin')

    def click_goGegister(self):
        """点击去注册"""
        self.driver.click(1, 'tv_register_count_new')

    def click_loginSelect(self):
        """点击换个方式登录"""
        self.driver.click(1, 'loginCategorySelect')

    def click_forgetPassword(self):
        """点击忘记密码"""
        self.driver.click(1, 'forgetPassword')

    def click_policy(self):
        """点击用户协议"""
        self.driver.click(1, 'tv_policy')

    def click_privacy(self):
        """点击隐私协议"""
        self.driver.click(1, 'tv_privacy')

    def click_scan(self):
        """点击扫描二维码"""
        self.driver.click(1, 'choose_enterprise_scan')

    def get_fail_toast(self, message):
        '''获取toast，根据返回信息进行反数据'''
        toast_element = self.driver.get_tost_element(message)
        if toast_element:
            return True
        else:
            return False



