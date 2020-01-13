# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: syft_proto/frameworks/torch/tensors/interpreters/v1/additive_shared.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from syft_proto.generic.pointers.v1 import pointer_tensor_pb2 as syft__proto_dot_generic_dot_pointers_dot_v1_dot_pointer__tensor__pb2
from syft_proto.types.syft.v1 import id_pb2 as syft__proto_dot_types_dot_syft_dot_v1_dot_id__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='syft_proto/frameworks/torch/tensors/interpreters/v1/additive_shared.proto',
  package='syft_proto.frameworks.torch.tensors.interpreters.v1',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nIsyft_proto/frameworks/torch/tensors/interpreters/v1/additive_shared.proto\x12\x33syft_proto.frameworks.torch.tensors.interpreters.v1\x1a\x33syft_proto/generic/pointers/v1/pointer_tensor.proto\x1a!syft_proto/types/syft/v1/id.proto\"\xb8\x02\n\x15\x41\x64\x64itiveSharingTensor\x12,\n\x02id\x18\x01 \x01(\x0b\x32\x1c.syft_proto.types.syft.v1.IdR\x02id\x12\x1d\n\nfield_size\x18\x02 \x01(\x03R\tfieldSize\x12J\n\x12\x63rypto_provider_id\x18\x03 \x01(\x0b\x32\x1c.syft_proto.types.syft.v1.IdR\x10\x63ryptoProviderId\x12?\n\x0clocation_ids\x18\x04 \x03(\x0b\x32\x1c.syft_proto.types.syft.v1.IdR\x0blocationIds\x12\x45\n\x06shares\x18\x05 \x03(\x0b\x32-.syft_proto.generic.pointers.v1.PointerTensorR\x06sharesb\x06proto3')
  ,
  dependencies=[syft__proto_dot_generic_dot_pointers_dot_v1_dot_pointer__tensor__pb2.DESCRIPTOR,syft__proto_dot_types_dot_syft_dot_v1_dot_id__pb2.DESCRIPTOR,])




_ADDITIVESHARINGTENSOR = _descriptor.Descriptor(
  name='AdditiveSharingTensor',
  full_name='syft_proto.frameworks.torch.tensors.interpreters.v1.AdditiveSharingTensor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='syft_proto.frameworks.torch.tensors.interpreters.v1.AdditiveSharingTensor.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='id', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='field_size', full_name='syft_proto.frameworks.torch.tensors.interpreters.v1.AdditiveSharingTensor.field_size', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='fieldSize', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='crypto_provider_id', full_name='syft_proto.frameworks.torch.tensors.interpreters.v1.AdditiveSharingTensor.crypto_provider_id', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='cryptoProviderId', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='location_ids', full_name='syft_proto.frameworks.torch.tensors.interpreters.v1.AdditiveSharingTensor.location_ids', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='locationIds', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shares', full_name='syft_proto.frameworks.torch.tensors.interpreters.v1.AdditiveSharingTensor.shares', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='shares', file=DESCRIPTOR),
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
  serialized_start=219,
  serialized_end=531,
)

_ADDITIVESHARINGTENSOR.fields_by_name['id'].message_type = syft__proto_dot_types_dot_syft_dot_v1_dot_id__pb2._ID
_ADDITIVESHARINGTENSOR.fields_by_name['crypto_provider_id'].message_type = syft__proto_dot_types_dot_syft_dot_v1_dot_id__pb2._ID
_ADDITIVESHARINGTENSOR.fields_by_name['location_ids'].message_type = syft__proto_dot_types_dot_syft_dot_v1_dot_id__pb2._ID
_ADDITIVESHARINGTENSOR.fields_by_name['shares'].message_type = syft__proto_dot_generic_dot_pointers_dot_v1_dot_pointer__tensor__pb2._POINTERTENSOR
DESCRIPTOR.message_types_by_name['AdditiveSharingTensor'] = _ADDITIVESHARINGTENSOR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AdditiveSharingTensor = _reflection.GeneratedProtocolMessageType('AdditiveSharingTensor', (_message.Message,), {
  'DESCRIPTOR' : _ADDITIVESHARINGTENSOR,
  '__module__' : 'syft_proto.frameworks.torch.tensors.interpreters.v1.additive_shared_pb2'
  # @@protoc_insertion_point(class_scope:syft_proto.frameworks.torch.tensors.interpreters.v1.AdditiveSharingTensor)
  })
_sym_db.RegisterMessage(AdditiveSharingTensor)


# @@protoc_insertion_point(module_scope)