#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: wangzhizhao
@contact: wzhizhao@gmail.com
@file: test_service.py
@time: 2017/12/21
"""

from examples.test_pb2 import Test, Math
from examples.test_pb2 import EchoResponse, PingResponse, MathResponse

from protobuf_tornado_rpc.rpc_server import RpcServer


class TestService(Test):
    def Echo(self, rpc_controller, request, done):
        response = EchoResponse()
        response.text = request.text
        done(response)

    def Ping(self, rpc_controller, request, done):
        response = PingResponse()
        done(response)


class MathService(Math):
    def Add(self, rpc_controller, request, done):
        response = MathResponse()
        response.result = request.first + request.second
        done(response)

    def Multiply(self, rpc_controller, request, done):
        response = MathResponse()
        response.result = request.first * request.second
        done(response)


if __name__ == '__main__':
    test_service = TestService()
    math_service = MathService()
    rpc_server = RpcServer(port=8889, services=[test_service, math_service])
    rpc_server.run()
