#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: wangzhizhao
@contact: wzhizhao@gmail.com
@file: rpc_proxy.py
@time: 2017/12/21
"""

from protobuf_tornado_rpc.rpc_callback import RpcCallback
from protobuf_tornado_rpc.rpc_controller import RpcController


class RpcProxy(object):
    def __init__(self, stub):
        self._stub = stub

    def call(self, method, request):
        controller = RpcController()
        callback = RpcCallback()
        method(controller, request, callback)
        return callback.response

    def __getattr__(self, item):
        return lambda request: self.call(item, request)
