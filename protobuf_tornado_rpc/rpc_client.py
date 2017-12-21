#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: wangzhizhao
@contact: wzhizhao@gmail.com
@file: rpc_client.py
@time: 2017/12/21
"""
from protobuf_tornado_rpc.rpc_proxy import RpcProxy


class RpcClient(object):
    stubs = {}

    def __init__(self, stubs):
        for s in stubs:
            self.stubs[s.GetDescriptor().name] = RpcProxy(s)

    def __getattr__(self, item):
        return self.stubs[item]
