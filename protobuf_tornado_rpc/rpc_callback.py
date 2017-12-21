#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: wangzhizhao
@contact: wzhizhao@gmail.com
@file: rpc_callback.py
@time: 2017/12/21
"""


class RpcCallback(object):
    def __init__(self):
        self.response = None

    def __call__(self, response):
        self.response = response
