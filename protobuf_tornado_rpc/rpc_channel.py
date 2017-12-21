#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: wangzhizhao
@contact: wzhizhao@gmail.com
@file: rpc_channel.py
@time: 2017/12/21
"""
import requests

from google.protobuf.service import RpcChannel as ProtobufRpcChannel


class RpcChannel(ProtobufRpcChannel):
    def __init__(self, host, port):
        super(RpcChannel, self).__init__()
        self.host = host
        self.port = port

    def CallMethod(self, method_descriptor, rpc_controller, request, response_class, done=None):
        service_name = method_descriptor.containing_service.name
        method_name = method_descriptor.name
        headers = {'PROTOBUF-RPC-API': '{}.{}'.format(service_name, method_name)}
        request_data = request.SerializeToString()
        req = requests.post('http://{}:{}/service'.format(self.host, self.port), data=request_data, headers=headers)
        response = response_class()
        response.ParseFromString(req.content)
        done(response)
