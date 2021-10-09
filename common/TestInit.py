# -*- coding: utf-8 -*-

# @Time : 2021/9/28 11:41
# @Author : Mandy

from common.base_driver import BaseDriver
from page.common_page import CommonPage
from page.login_page import LoginPage
from page.mine_page import MinePage
from page.register_page import RegisterPage
from utils.handle import Handle
from utils.server import Server


class Init(object):
    driver = None

    def setup_class(cls) -> None:
        # 必须使用@classmethod 装饰器,所有test运行前运行一次
        global handle, driver
        # 调用get_driver
        cls.server = Server()
        cls.server.main()
        base_driver = BaseDriver(0)
        cls.driver = base_driver.android_driver()
        # 实例化Operation
        cls.handle = Handle(cls.driver)
        cls.login_page = LoginPage(cls.handle)
        cls.mine_page = MinePage(cls.handle)
        cls.common_page = CommonPage(cls.handle)
        cls.register_page = RegisterPage(cls.handle)

    def teardown_class(cls) -> None:
        # 必须使用 @ classmethod装饰器, 所有test运行完后运行一次
        print(u'[MyLog]--------关闭driver')
        cls.driver.quit()
        cls.server.kill_server()
