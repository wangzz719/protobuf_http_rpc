# protobuf_tornado_rpc
## 介绍
protobuf_tornado_rpc 是一个基于 protobuf 和 tornado 的 rpc 框架
- 框架使用 google protobuf rpc 协议
- 消息的传输位于 http 层，使用 tornado 作为服务器实现

## protobuf 介绍
### proto 文件编写规则
proto 文件的编写规则参见： [google protobuf](https://developers.google.com/protocol-buffers/docs/proto)

**在使用PRC协议时，必须加上 `option py_generic_services  = true;`可选项，要不然编译器不会生成包含 connect_server 函数的 Service 描述**

### 编译命令
`protoc --python_out={output_dir} {proto_file}`

## 运行 example
1. 在本项目目录下运行 `buildout` （使用 `pip install zc.buildout` 安装 `buildout` 命令）
2. 启动 test server，运行命令：`bin/python examples/test_service.py`
3. 调用 test server 服务接口，运行命令：`bin/python examples/test_client.py`

## 参考
\[1\] [https://github.com/modeswitch/protobuf-rpc](https://github.com/modeswitch/protobuf-rpc)

\[2\] [python通过protobuf实现rpc](http://www.cnblogs.com/chengxuyuancc/p/5245749.html)
