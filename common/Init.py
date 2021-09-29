# -*- coding: utf-8 -*-

# @Time : 2021/9/28 11:41
# @Author : Mandy

import unittest
from common.base_driver import BaseDriver
from utils.handle import Handle
from utils.server import Server


class TestInit(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        # 必须使用@classmethod 装饰器,所有test运行前运行一次
        global operation, driver
        # 调用get_driver
        server = Server()
        server.main()
        base_driver = BaseDriver(0)
        cls.driver = base_driver.android_driver()
        # 实例化Operation
        cls.handle = Handle(cls.driver)

    @classmethod
    def tearDownClass(cls):
        # 必须使用 @ classmethod装饰器, 所有test运行完后运行一次
        print(u'[MyLog]--------关闭driver')
        cls.driver.quit()
