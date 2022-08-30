# -*- coding: UTF8 -*
"""
@author: Jiang
@file name: test
@create date: 2022/8/20 16:00
@description:
"""
import datetime
import os
import shutil

from comm.comm_time import string_to_date, get_system_time_stamp, get_system_datetime


def test():
    path = r"C:\Users\Jiang\IdeaProjects\log"
    files = os.listdir(path)
    print(files)
    for i in files:
        cur_path = os.path.join(path, i)
        if os.path.isdir(cur_path):
            print(f'{cur_path} 是目录')
            i_30 = string_to_date(i) + datetime.timedelta(days=30)
            now = get_system_datetime()
            print(f'{i}一个月后的日期是{i_30},当前时间为{now}')
            print(i_30 > now)
            if i_30<now:
                # shutil.rmtree(cur_path)
                os.rmdir(cur_path)
                print(f'删除目录 {cur_path}')
        else:
            print(f'{cur_path} 是文件')


if __name__ == '__main__':
    # test()
    # print(os.path.dirname(os.path.abspath(__file__)))
    from jupyter_core.paths import jupyter_path
    print(jupyter_path())
