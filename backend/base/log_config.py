# -*- coding: UTF8 -*
"""
@author: Jiang
@file name: log_config.py
@create date: 2022/8/19 20:27
@description:
"""
import os
import logging
import logging.handlers

from comm.comm_time import get_system_date_str, get_system_time_str

logger = logging.getLogger("info")


def init_log(transaction_code=''):
    log_path = os.path.join(os.getcwd(), '../../log', get_system_date_str(), transaction_code)
    try:
        if not os.path.exists(log_path):
            os.makedirs(log_path)
            print(f'文件夹创建成功: {log_path}')
        else:
            print(f'文件夹已经存在: {log_path}')
    except:
        print("创建日志目录失败")
        exit(1)
    if len(logger.handlers) == 0:  # 避免重复
        # 2.创建handler(负责输出，输出到屏幕 StreamHandler,输出到文件filehandler)
        # filename = os.path.join(log_path, 'user_api.log')
        filename = os.path.join(log_path, get_system_time_str() + '.log')
        fh = logging.FileHandler(filename, mode="a", encoding="utf-8")  # 默认mode 为a模式，默认编码方式为utf-8
        sh = logging.StreamHandler()
        # 3.创建formatter：
        formatter = logging.Formatter('[%(asctime)s %(filename)s: %(lineno)d] %(message)s', '%H:%M:%S')
        # 4.绑定关系：①logger绑定handler
        logger.addHandler(fh)
        logger.addHandler(sh)
        # # ②为handler绑定formatter
        fh.setFormatter(formatter)
        sh.setFormatter(formatter)
        # # 5.设置日志级别(日志级别两层关卡必须都通过，日志才能正常记录)
        logger.setLevel(40)
        fh.setLevel(40)
        sh.setLevel(40)


if __name__ == '__main__':
    path = os.path.join(os.getcwd(), '../../log')
    try:
        if not os.path.exists(path):
            os.makedirs(path)
    except:
        print("创建日志目录失败")
        exit(1)
