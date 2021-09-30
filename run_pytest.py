# -*- coding: utf-8 -*-

# @Time : 2allure-results021/9/29 10:22
# @Author : Mandy
import os
import sys
from common.read_ini import ReadIni

config = ReadIni()


def run():
    print('参数个数为:', len(sys.argv), '个参数。')
    print('参数列表:', str(sys.argv))
    for i in range(1, len(sys.argv)):
        print("参数", i, sys.argv[i])
    if len(sys.argv) > 1:
        environment = sys.argv[1]
        config.set_ini('env', 'environment', str(environment))
        print("运行环境为：", environment)

    os.system('py.test testcases/ --alluredir ./target/allure-results')


if __name__ == '__main__':
    run()