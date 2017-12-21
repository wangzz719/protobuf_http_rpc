#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: wangzhizhao
@contact: wangzhizhao@gmail.com
@file: rpc_server.py
@time: 2017/12/21
"""
import tornado.ioloop
from tornado.web import RequestHandler
from tornado.web import Application

from protobuf_tornado_rpc.rpc_callback import RpcCallback
from protobuf_tornado_rpc.rpc_controller import RpcController


class RpcRequestHandler(RequestHandler):
    def post(self, *args, **kwargs):
        data = self.request.body
        rpc_api = self.request.headers.get('PROTOBUF-RPC-API')
        service_name, method_name = rpc_api.split('.')
        service = self.settings['services'][service_name]
        method = service.GetDescriptor().FindMethodByName(method_name)
        if method:
            request = service.GetRequestClass(method)()
            request.ParseFromString(data)
            controller = RpcController()
            callback = RpcCallback()
            service.CallMethod(method, controller, request, callback)
            response = callback.response.SerializeToString()
            self.write(response)


class RpcServer(object):
    services = {}

    def __init__(self, port, services):
        self._port = port
        for s in services:
            self.services[s.GetDescriptor().name] = s

    def run(self):
        settings = {'services': self.services}
        app = Application([(r'/service', RpcRequestHandler)], **settings)
        app.listen(self._port)
        tornado.ioloop.IOLoop.instance().start()
