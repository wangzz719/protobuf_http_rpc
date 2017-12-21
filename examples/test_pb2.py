# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: test.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import service as _service
from google.protobuf import service_reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='test.proto',
  package='test',
  serialized_pb=_b('\n\ntest.proto\x12\x04test\"\x1b\n\x0b\x45\x63hoRequest\x12\x0c\n\x04text\x18\x01 \x02(\t\"\x1c\n\x0c\x45\x63hoResponse\x12\x0c\n\x04text\x18\x01 \x02(\t\"\r\n\x0bPingRequest\"\x0e\n\x0cPingResponse\";\n\x1aMathBinaryOperationRequest\x12\r\n\x05\x66irst\x18\x01 \x02(\x02\x12\x0e\n\x06second\x18\x02 \x02(\x02\"\x1e\n\x0cMathResponse\x12\x0e\n\x06result\x18\x01 \x02(\x02\x32\x64\n\x04Test\x12-\n\x04Ping\x12\x11.test.PingRequest\x1a\x12.test.PingResponse\x12-\n\x04\x45\x63ho\x12\x11.test.EchoRequest\x1a\x12.test.EchoResponse2\x85\x01\n\x04Math\x12;\n\x03\x41\x64\x64\x12 .test.MathBinaryOperationRequest\x1a\x12.test.MathResponse\x12@\n\x08Multiply\x12 .test.MathBinaryOperationRequest\x1a\x12.test.MathResponseB\t\x80\x01\x01\x88\x01\x01\x90\x01\x01')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_ECHOREQUEST = _descriptor.Descriptor(
  name='EchoRequest',
  full_name='test.EchoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='test.EchoRequest.text', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=20,
  serialized_end=47,
)


_ECHORESPONSE = _descriptor.Descriptor(
  name='EchoResponse',
  full_name='test.EchoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='test.EchoResponse.text', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=49,
  serialized_end=77,
)


_PINGREQUEST = _descriptor.Descriptor(
  name='PingRequest',
  full_name='test.PingRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=79,
  serialized_end=92,
)


_PINGRESPONSE = _descriptor.Descriptor(
  name='PingResponse',
  full_name='test.PingResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=94,
  serialized_end=108,
)


_MATHBINARYOPERATIONREQUEST = _descriptor.Descriptor(
  name='MathBinaryOperationRequest',
  full_name='test.MathBinaryOperationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='first', full_name='test.MathBinaryOperationRequest.first', index=0,
      number=1, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='second', full_name='test.MathBinaryOperationRequest.second', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=110,
  serialized_end=169,
)


_MATHRESPONSE = _descriptor.Descriptor(
  name='MathResponse',
  full_name='test.MathResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='test.MathResponse.result', index=0,
      number=1, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=171,
  serialized_end=201,
)

DESCRIPTOR.message_types_by_name['EchoRequest'] = _ECHOREQUEST
DESCRIPTOR.message_types_by_name['EchoResponse'] = _ECHORESPONSE
DESCRIPTOR.message_types_by_name['PingRequest'] = _PINGREQUEST
DESCRIPTOR.message_types_by_name['PingResponse'] = _PINGRESPONSE
DESCRIPTOR.message_types_by_name['MathBinaryOperationRequest'] = _MATHBINARYOPERATIONREQUEST
DESCRIPTOR.message_types_by_name['MathResponse'] = _MATHRESPONSE

EchoRequest = _reflection.GeneratedProtocolMessageType('EchoRequest', (_message.Message,), dict(
  DESCRIPTOR = _ECHOREQUEST,
  __module__ = 'test_pb2'
  # @@protoc_insertion_point(class_scope:test.EchoRequest)
  ))
_sym_db.RegisterMessage(EchoRequest)

EchoResponse = _reflection.GeneratedProtocolMessageType('EchoResponse', (_message.Message,), dict(
  DESCRIPTOR = _ECHORESPONSE,
  __module__ = 'test_pb2'
  # @@protoc_insertion_point(class_scope:test.EchoResponse)
  ))
_sym_db.RegisterMessage(EchoResponse)

PingRequest = _reflection.GeneratedProtocolMessageType('PingRequest', (_message.Message,), dict(
  DESCRIPTOR = _PINGREQUEST,
  __module__ = 'test_pb2'
  # @@protoc_insertion_point(class_scope:test.PingRequest)
  ))
_sym_db.RegisterMessage(PingRequest)

PingResponse = _reflection.GeneratedProtocolMessageType('PingResponse', (_message.Message,), dict(
  DESCRIPTOR = _PINGRESPONSE,
  __module__ = 'test_pb2'
  # @@protoc_insertion_point(class_scope:test.PingResponse)
  ))
_sym_db.RegisterMessage(PingResponse)

MathBinaryOperationRequest = _reflection.GeneratedProtocolMessageType('MathBinaryOperationRequest', (_message.Message,), dict(
  DESCRIPTOR = _MATHBINARYOPERATIONREQUEST,
  __module__ = 'test_pb2'
  # @@protoc_insertion_point(class_scope:test.MathBinaryOperationRequest)
  ))
_sym_db.RegisterMessage(MathBinaryOperationRequest)

MathResponse = _reflection.GeneratedProtocolMessageType('MathResponse', (_message.Message,), dict(
  DESCRIPTOR = _MATHRESPONSE,
  __module__ = 'test_pb2'
  # @@protoc_insertion_point(class_scope:test.MathResponse)
  ))
_sym_db.RegisterMessage(MathResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\200\001\001\210\001\001\220\001\001'))

_TEST = _descriptor.ServiceDescriptor(
  name='Test',
  full_name='test.Test',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=203,
  serialized_end=303,
  methods=[
  _descriptor.MethodDescriptor(
    name='Ping',
    full_name='test.Test.Ping',
    index=0,
    containing_service=None,
    input_type=_PINGREQUEST,
    output_type=_PINGRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Echo',
    full_name='test.Test.Echo',
    index=1,
    containing_service=None,
    input_type=_ECHOREQUEST,
    output_type=_ECHORESPONSE,
    options=None,
  ),
])

Test = service_reflection.GeneratedServiceType('Test', (_service.Service,), dict(
  DESCRIPTOR = _TEST,
  __module__ = 'test_pb2'
  ))

Test_Stub = service_reflection.GeneratedServiceStubType('Test_Stub', (Test,), dict(
  DESCRIPTOR = _TEST,
  __module__ = 'test_pb2'
  ))



_MATH = _descriptor.ServiceDescriptor(
  name='Math',
  full_name='test.Math',
  file=DESCRIPTOR,
  index=1,
  options=None,
  serialized_start=306,
  serialized_end=439,
  methods=[
  _descriptor.MethodDescriptor(
    name='Add',
    full_name='test.Math.Add',
    index=0,
    containing_service=None,
    input_type=_MATHBINARYOPERATIONREQUEST,
    output_type=_MATHRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Multiply',
    full_name='test.Math.Multiply',
    index=1,
    containing_service=None,
    input_type=_MATHBINARYOPERATIONREQUEST,
    output_type=_MATHRESPONSE,
    options=None,
  ),
])

Math = service_reflection.GeneratedServiceType('Math', (_service.Service,), dict(
  DESCRIPTOR = _MATH,
  __module__ = 'test_pb2'
  ))

Math_Stub = service_reflection.GeneratedServiceStubType('Math_Stub', (Math,), dict(
  DESCRIPTOR = _MATH,
  __module__ = 'test_pb2'
  ))


# @@protoc_insertion_point(module_scope)
