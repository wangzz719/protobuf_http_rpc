#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: wangzhizhao
@contact: wzhizhao@gmail.com
@file: test_proxy.py
@time: 2017/12/21
"""

from examples.test_pb2 import Test_Stub
from examples.test_pb2 import EchoRequest

from protobuf_tornado_rpc.rpc_channel import RpcChannel
from protobuf_tornado_rpc.rpc_client import RpcClient

if __name__ == '__main__':
    channel = RpcChannel(host='127.0.0.1', port=8889)
    client = RpcClient([Test_Stub(channel)])
    request = EchoRequest()
    request.text = "Hello World!"
    response = client.Text.Echo(request)
    print response