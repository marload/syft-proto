# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: syft_proto/core/message/run_class_method_message.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='syft_proto/core/message/run_class_method_message.proto',
  package='syft_proto.core.message.v1',
  syntax='proto3',
  serialized_options=b'\n\'org.openmined.syftproto.core.message.v1',
  serialized_pb=b'\n6syft_proto/core/message/run_class_method_message.proto\x12\x1asyft_proto.core.message.v1\"\x17\n\x15RunClassMethodMessageB)\n\'org.openmined.syftproto.core.message.v1b\x06proto3'
)




_RUNCLASSMETHODMESSAGE = _descriptor.Descriptor(
  name='RunClassMethodMessage',
  full_name='syft_proto.core.message.v1.RunClassMethodMessage',
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=86,
  serialized_end=109,
)

DESCRIPTOR.message_types_by_name['RunClassMethodMessage'] = _RUNCLASSMETHODMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RunClassMethodMessage = _reflection.GeneratedProtocolMessageType('RunClassMethodMessage', (_message.Message,), {
  'DESCRIPTOR' : _RUNCLASSMETHODMESSAGE,
  '__module__' : 'syft_proto.core.message.run_class_method_message_pb2'
  # @@protoc_insertion_point(class_scope:syft_proto.core.message.v1.RunClassMethodMessage)
  })
_sym_db.RegisterMessage(RunClassMethodMessage)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
