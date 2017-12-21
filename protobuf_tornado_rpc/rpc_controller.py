#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: wangzhizhao
@contact: wzhizhao@gmail.com
@file: rpc_controller.py
@time: 2017/12/21
"""

from google.protobuf.service import RpcController as ProtobufRpcController


class RpcController(ProtobufRpcController):
    error = None

    def Reset(self):
        self.error = None

    def Failed(self):
        return self.error != None

    def ErrorText(self):
        return self.error

    def StartCancel(self):
        pass

    def SetFailed(self, reason):
        self.error = reason

    def IsCancelled(self):
        pass

    def NotifyOnCancel(self, callback):
        pass
