# -*- coding: UTF8 -*
"""
@author: Jiang
@file name: __init__.py
@create date: 2022/8/19 20:23
@description:
"""

from flask import Flask
from flask_cors import CORS

from api.resource import api
from base.log_config import init_log

from config import config, Config


def create_app(config_name):
    app = Flask(__name__)
    # 验证
    CORS(app, supports_credentials=True)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    # 初始化数据库
    # db.init_app(app)
    # 返回数据中response为中文
    app.config['JSON_AS_ASCII'] = False

    # 初始化日志###
    init_log()
    api.init_app(app)
    return app
