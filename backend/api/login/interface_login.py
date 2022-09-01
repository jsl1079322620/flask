# -*- coding: UTF8 -*
"""
@author: Jiang
@file name: interface_login
@create date: 2022/9/1 10:43
@description:
"""
import uuid

from flask import request
from flask_restful import Resource

from comm.comm_model_enum import modelEnum
from comm.comm_request_process import req
from comm.comm_response_process import response_result_process
from utils.log_config import logger
from comm.comm_response_code import response_code


class InterfaceLogin(Resource):

    def post(self):
        try:
            request_data = req.request_process(request)
            logger.info(request_data)

            # parse_response_data_ret, request_data = response_data_verify(request_data)
            # if not parse_response_data_ret:
            #     return request_data
            # fields = ['username', 'password']
            # must = req.verify_all_param_must(request_data, fields)
            # if must:
            #     return response_result_process(must)
            # par_type = {'username': str, 'password': str}
            # param_type = req.verify_all_param_type(request_data, par_type)
            # if param_type:
            #     return response_result_process(param_type)


            data = {
                'code': 20000,
                'data': {
                    'token': 'admin-token'
                }
            }

            return response_result_process(data)
        except Exception as e:
            logger.error(e)
            error_data = response_code.EXCEPTION_ERROR(e)
            return response_result_process(error_data)
