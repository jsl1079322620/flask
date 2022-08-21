# -*- coding: UTF8 -*
"""
@author: Jiang
@file name: comm_file
@create date: 2022/8/21 20:58
@description:
"""
import os

from utils.log_config import logger as comm_file_logger


def makeDirs(_path: str):
    try:
        path = _path.strip()
        if not os.path.exists(path):
            os.makedirs(path)
            comm_file_logger.info(f'文件夹创建成功: {path}')
        else:
            comm_file_logger.info(f'文件夹已经存在: {path}')
    except Exception as e:
        comm_file_logger.info(f"创建日志目录失败: {str(e)}")
        exit(1)


def remove_dir(path: str) -> bool:
    """
    删除一个非空目录
    :return:
    """
    try:
        if os.path.isdir(path):
            os.rmdir(path)
            comm_file_logger.info(f'文件夹删除成功: {path}')
            # todo 建议记录到数据库
            return True
        else:
            comm_file_logger.warning(f'不是文件夹, 不做删除: {path}')
            return False
    except Exception as e:
        comm_file_logger.error(f'文件夹 {path} 删除失败：{str(e)}')
        return False
