#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: wangzhizhao
@contact: wzhizhao@gmail.com
@file: setup.py
@time: 2017/12/21
"""

from setuptools import setup, find_packages

setup(
    name="protobuf_tornado_rpc",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'protobuf',
        'twisted',
        'tornado'
    ],
    entry_points={
    }
)
