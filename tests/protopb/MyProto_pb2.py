# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: MyProto.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import ImportMessage_pb2 as ImportMessage__pb2
from . import ImportEnum_pb2 as ImportEnum__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rMyProto.proto\x1a\x13ImportMessage.proto\x1a\x10ImportEnum.proto\"\xb8\x10\n\x07MyProto\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x15\n\rlength_uint32\x18\x02 \x01(\r\x12\x17\n\x0frepeated_string\x18\x03 \x03(\t\x12\x0f\n\x07success\x18\x04 \x01(\x08\x12\"\n\x0c\x65num_message\x18\x05 \x01(\x0e\x32\x0c.EnumMessage\x12*\n\x10\x65mbedded_message\x18\x06 \x01(\x0b\x32\x10.EmbeddedMessage\x12+\n\x15repeated_enum_message\x18\x07 \x03(\x0e\x32\x0c.EnumMessage\x12)\n\x14repeated_import_enum\x18\x08 \x03(\x0e\x32\x0b.ImportEnum\x12\x33\n\x19repeated_embedded_message\x18\t \x03(\x0b\x32\x10.EmbeddedMessage\x12/\n\x17repeated_import_message\x18\n \x03(\x0b\x32\x0e.ImportMessage\x12\t\n\x01x\x18\x0b \x01(\x02\x12\t\n\x01y\x18\x0c \x01(\x01\x12\x32\n\x0emap_string_int\x18\r \x03(\x0b\x32\x1a.MyProto.MapStringIntEntry\x12\x38\n\x11map_string_string\x18\x0e \x03(\x0b\x32\x1d.MyProto.MapStringStringEntry\x12G\n\x19map_string_import_message\x18\x0f \x03(\x0b\x32$.MyProto.MapStringImportMessageEntry\x12\x41\n\x16map_string_import_enum\x18\x10 \x03(\x0b\x32!.MyProto.MapStringImportEnumEntry\x12\x15\n\rrepeated_bool\x18\x11 \x03(\x08\x12\x15\n\rrepeated_uint\x18\x12 \x03(\r\x12\x14\n\x0clength_int32\x18\x13 \x01(\x05\x12\x14\n\x0clength_int64\x18\x14 \x01(\x03\x12\x15\n\rlength_uint64\x18\x15 \x01(\x04\x12\x15\n\rlength_sint64\x18\x16 \x01(\x12\x12\x15\n\rlength_sint32\x18\x17 \x01(\x11\x12\x16\n\x0elength_fixed64\x18\x18 \x01(\x06\x12\x16\n\x0elength_fixed32\x18\x19 \x01(\x07\x12\x17\n\x0flength_sfixed32\x18\x1a \x01(\x0f\x12\x17\n\x0flength_sfixed64\x18\x1b \x01(\x10\x12\x0e\n\x06\x62uffer\x18\x1c \x01(\x0c\x12 \n\x0bimport_enum\x18\x1d \x01(\x0e\x32\x0b.ImportEnum\x12&\n\x0eimport_message\x18\x1e \x01(\x0b\x32\x0e.ImportMessage\x12\x34\n\x11\x65mbedded_message2\x18\x1f \x01(\x0b\x32\x19.MyProto.EmbeddedMessage2\x1a\xa9\x06\n\x10\x45mbeddedMessage2\x12\x14\n\x07message\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x0e\n\x06number\x18\x02 \x01(\x05\x12\x41\n\rmap_uint_uint\x18\x03 \x03(\x0b\x32*.MyProto.EmbeddedMessage2.MapUintUintEntry\x12\\\n\x1bmap_string_embedded_message\x18\x04 \x03(\x0b\x32\x37.MyProto.EmbeddedMessage2.MapStringEmbeddedMessageEntry\x12X\n\x19map_string_import_message\x18\x05 \x03(\x0b\x32\x35.MyProto.EmbeddedMessage2.MapStringImportMessageEntry\x12R\n\x16map_string_import_enum\x18\x06 \x03(\x0b\x32\x32.MyProto.EmbeddedMessage2.MapStringImportEnumEntry\x12\x17\n\x0frepeated_string\x18\x07 \x03(\t\x12+\n\x15repeated_enum_message\x18\x08 \x03(\x0e\x32\x0c.EnumMessage\x12/\n\x17repeated_import_message\x18\t \x03(\x0b\x32\x0e.ImportMessage\x1a\x32\n\x10MapUintUintEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x1aQ\n\x1dMapStringEmbeddedMessageEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1f\n\x05value\x18\x02 \x01(\x0b\x32\x10.EmbeddedMessage:\x02\x38\x01\x1aM\n\x1bMapStringImportMessageEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1d\n\x05value\x18\x02 \x01(\x0b\x32\x0e.ImportMessage:\x02\x38\x01\x1aG\n\x18MapStringImportEnumEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1a\n\x05value\x18\x02 \x01(\x0e\x32\x0b.ImportEnum:\x02\x38\x01\x42\n\n\x08_message\x1a\x33\n\x11MapStringIntEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x1a\x36\n\x14MapStringStringEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1aM\n\x1bMapStringImportMessageEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1d\n\x05value\x18\x02 \x01(\x0b\x32\x0e.ImportMessage:\x02\x38\x01\x1aG\n\x18MapStringImportEnumEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1a\n\x05value\x18\x02 \x01(\x0e\x32\x0b.ImportEnum:\x02\x38\x01\">\n\x0f\x45mbeddedMessage\x12\x11\n\x07message\x18\x01 \x01(\tH\x00\x12\x10\n\x06number\x18\x02 \x01(\x05H\x00\x42\x06\n\x04\x64\x61ta*1\n\x0b\x45numMessage\x12\n\n\x06\x45NUM_A\x10\x00\x12\n\n\x06\x45NUM_B\x10\x01\x12\n\n\x06\x45NUM_C\x10\x02\x62\x06proto3')

_ENUMMESSAGE = DESCRIPTOR.enum_types_by_name['EnumMessage']
EnumMessage = enum_type_wrapper.EnumTypeWrapper(_ENUMMESSAGE)
ENUM_A = 0
ENUM_B = 1
ENUM_C = 2


_MYPROTO = DESCRIPTOR.message_types_by_name['MyProto']
_MYPROTO_EMBEDDEDMESSAGE2 = _MYPROTO.nested_types_by_name['EmbeddedMessage2']
_MYPROTO_EMBEDDEDMESSAGE2_MAPUINTUINTENTRY = _MYPROTO_EMBEDDEDMESSAGE2.nested_types_by_name['MapUintUintEntry']
_MYPROTO_EMBEDDEDMESSAGE2_MAPSTRINGEMBEDDEDMESSAGEENTRY = _MYPROTO_EMBEDDEDMESSAGE2.nested_types_by_name['MapStringEmbeddedMessageEntry']
_MYPROTO_EMBEDDEDMESSAGE2_MAPSTRINGIMPORTMESSAGEENTRY = _MYPROTO_EMBEDDEDMESSAGE2.nested_types_by_name['MapStringImportMessageEntry']
_MYPROTO_EMBEDDEDMESSAGE2_MAPSTRINGIMPORTENUMENTRY = _MYPROTO_EMBEDDEDMESSAGE2.nested_types_by_name['MapStringImportEnumEntry']
_MYPROTO_MAPSTRINGINTENTRY = _MYPROTO.nested_types_by_name['MapStringIntEntry']
_MYPROTO_MAPSTRINGSTRINGENTRY = _MYPROTO.nested_types_by_name['MapStringStringEntry']
_MYPROTO_MAPSTRINGIMPORTMESSAGEENTRY = _MYPROTO.nested_types_by_name['MapStringImportMessageEntry']
_MYPROTO_MAPSTRINGIMPORTENUMENTRY = _MYPROTO.nested_types_by_name['MapStringImportEnumEntry']
_EMBEDDEDMESSAGE = DESCRIPTOR.message_types_by_name['EmbeddedMessage']
MyProto = _reflection.GeneratedProtocolMessageType('MyProto', (_message.Message,), {

  'EmbeddedMessage2' : _reflection.GeneratedProtocolMessageType('EmbeddedMessage2', (_message.Message,), {

    'MapUintUintEntry' : _reflection.GeneratedProtocolMessageType('MapUintUintEntry', (_message.Message,), {
      'DESCRIPTOR' : _MYPROTO_EMBEDDEDMESSAGE2_MAPUINTUINTENTRY,
      '__module__' : 'MyProto_pb2'
      # @@protoc_insertion_point(class_scope:MyProto.EmbeddedMessage2.MapUintUintEntry)
      })
    ,

    'MapStringEmbeddedMessageEntry' : _reflection.GeneratedProtocolMessageType('MapStringEmbeddedMessageEntry', (_message.Message,), {
      'DESCRIPTOR' : _MYPROTO_EMBEDDEDMESSAGE2_MAPSTRINGEMBEDDEDMESSAGEENTRY,
      '__module__' : 'MyProto_pb2'
      # @@protoc_insertion_point(class_scope:MyProto.EmbeddedMessage2.MapStringEmbeddedMessageEntry)
      })
    ,

    'MapStringImportMessageEntry' : _reflection.GeneratedProtocolMessageType('MapStringImportMessageEntry', (_message.Message,), {
      'DESCRIPTOR' : _MYPROTO_EMBEDDEDMESSAGE2_MAPSTRINGIMPORTMESSAGEENTRY,
      '__module__' : 'MyProto_pb2'
      # @@protoc_insertion_point(class_scope:MyProto.EmbeddedMessage2.MapStringImportMessageEntry)
      })
    ,

    'MapStringImportEnumEntry' : _reflection.GeneratedProtocolMessageType('MapStringImportEnumEntry', (_message.Message,), {
      'DESCRIPTOR' : _MYPROTO_EMBEDDEDMESSAGE2_MAPSTRINGIMPORTENUMENTRY,
      '__module__' : 'MyProto_pb2'
      # @@protoc_insertion_point(class_scope:MyProto.EmbeddedMessage2.MapStringImportEnumEntry)
      })
    ,
    'DESCRIPTOR' : _MYPROTO_EMBEDDEDMESSAGE2,
    '__module__' : 'MyProto_pb2'
    # @@protoc_insertion_point(class_scope:MyProto.EmbeddedMessage2)
    })
  ,

  'MapStringIntEntry' : _reflection.GeneratedProtocolMessageType('MapStringIntEntry', (_message.Message,), {
    'DESCRIPTOR' : _MYPROTO_MAPSTRINGINTENTRY,
    '__module__' : 'MyProto_pb2'
    # @@protoc_insertion_point(class_scope:MyProto.MapStringIntEntry)
    })
  ,

  'MapStringStringEntry' : _reflection.GeneratedProtocolMessageType('MapStringStringEntry', (_message.Message,), {
    'DESCRIPTOR' : _MYPROTO_MAPSTRINGSTRINGENTRY,
    '__module__' : 'MyProto_pb2'
    # @@protoc_insertion_point(class_scope:MyProto.MapStringStringEntry)
    })
  ,

  'MapStringImportMessageEntry' : _reflection.GeneratedProtocolMessageType('MapStringImportMessageEntry', (_message.Message,), {
    'DESCRIPTOR' : _MYPROTO_MAPSTRINGIMPORTMESSAGEENTRY,
    '__module__' : 'MyProto_pb2'
    # @@protoc_insertion_point(class_scope:MyProto.MapStringImportMessageEntry)
    })
  ,

  'MapStringImportEnumEntry' : _reflection.GeneratedProtocolMessageType('MapStringImportEnumEntry', (_message.Message,), {
    'DESCRIPTOR' : _MYPROTO_MAPSTRINGIMPORTENUMENTRY,
    '__module__' : 'MyProto_pb2'
    # @@protoc_insertion_point(class_scope:MyProto.MapStringImportEnumEntry)
    })
  ,
  'DESCRIPTOR' : _MYPROTO,
  '__module__' : 'MyProto_pb2'
  # @@protoc_insertion_point(class_scope:MyProto)
  })
_sym_db.RegisterMessage(MyProto)
_sym_db.RegisterMessage(MyProto.EmbeddedMessage2)
_sym_db.RegisterMessage(MyProto.EmbeddedMessage2.MapUintUintEntry)
_sym_db.RegisterMessage(MyProto.EmbeddedMessage2.MapStringEmbeddedMessageEntry)
_sym_db.RegisterMessage(MyProto.EmbeddedMessage2.MapStringImportMessageEntry)
_sym_db.RegisterMessage(MyProto.EmbeddedMessage2.MapStringImportEnumEntry)
_sym_db.RegisterMessage(MyProto.MapStringIntEntry)
_sym_db.RegisterMessage(MyProto.MapStringStringEntry)
_sym_db.RegisterMessage(MyProto.MapStringImportMessageEntry)
_sym_db.RegisterMessage(MyProto.MapStringImportEnumEntry)

EmbeddedMessage = _reflection.GeneratedProtocolMessageType('EmbeddedMessage', (_message.Message,), {
  'DESCRIPTOR' : _EMBEDDEDMESSAGE,
  '__module__' : 'MyProto_pb2'
  # @@protoc_insertion_point(class_scope:EmbeddedMessage)
  })
_sym_db.RegisterMessage(EmbeddedMessage)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _MYPROTO_EMBEDDEDMESSAGE2_MAPUINTUINTENTRY._options = None
  _MYPROTO_EMBEDDEDMESSAGE2_MAPUINTUINTENTRY._serialized_options = b'8\001'
  _MYPROTO_EMBEDDEDMESSAGE2_MAPSTRINGEMBEDDEDMESSAGEENTRY._options = None
  _MYPROTO_EMBEDDEDMESSAGE2_MAPSTRINGEMBEDDEDMESSAGEENTRY._serialized_options = b'8\001'
  _MYPROTO_EMBEDDEDMESSAGE2_MAPSTRINGIMPORTMESSAGEENTRY._options = None
  _MYPROTO_EMBEDDEDMESSAGE2_MAPSTRINGIMPORTMESSAGEENTRY._serialized_options = b'8\001'
  _MYPROTO_EMBEDDEDMESSAGE2_MAPSTRINGIMPORTENUMENTRY._options = None
  _MYPROTO_EMBEDDEDMESSAGE2_MAPSTRINGIMPORTENUMENTRY._serialized_options = b'8\001'
  _MYPROTO_MAPSTRINGINTENTRY._options = None
  _MYPROTO_MAPSTRINGINTENTRY._serialized_options = b'8\001'
  _MYPROTO_MAPSTRINGSTRINGENTRY._options = None
  _MYPROTO_MAPSTRINGSTRINGENTRY._serialized_options = b'8\001'
  _MYPROTO_MAPSTRINGIMPORTMESSAGEENTRY._options = None
  _MYPROTO_MAPSTRINGIMPORTMESSAGEENTRY._serialized_options = b'8\001'
  _MYPROTO_MAPSTRINGIMPORTENUMENTRY._options = None
  _MYPROTO_MAPSTRINGIMPORTENUMENTRY._serialized_options = b'8\001'
  _ENUMMESSAGE._serialized_start=2227
  _ENUMMESSAGE._serialized_end=2276
  _MYPROTO._serialized_start=57
  _MYPROTO._serialized_end=2161
  _MYPROTO_EMBEDDEDMESSAGE2._serialized_start=1091
  _MYPROTO_EMBEDDEDMESSAGE2._serialized_end=1900
  _MYPROTO_EMBEDDEDMESSAGE2_MAPUINTUINTENTRY._serialized_start=1603
  _MYPROTO_EMBEDDEDMESSAGE2_MAPUINTUINTENTRY._serialized_end=1653
  _MYPROTO_EMBEDDEDMESSAGE2_MAPSTRINGEMBEDDEDMESSAGEENTRY._serialized_start=1655
  _MYPROTO_EMBEDDEDMESSAGE2_MAPSTRINGEMBEDDEDMESSAGEENTRY._serialized_end=1736
  _MYPROTO_EMBEDDEDMESSAGE2_MAPSTRINGIMPORTMESSAGEENTRY._serialized_start=1738
  _MYPROTO_EMBEDDEDMESSAGE2_MAPSTRINGIMPORTMESSAGEENTRY._serialized_end=1815
  _MYPROTO_EMBEDDEDMESSAGE2_MAPSTRINGIMPORTENUMENTRY._serialized_start=1817
  _MYPROTO_EMBEDDEDMESSAGE2_MAPSTRINGIMPORTENUMENTRY._serialized_end=1888
  _MYPROTO_MAPSTRINGINTENTRY._serialized_start=1902
  _MYPROTO_MAPSTRINGINTENTRY._serialized_end=1953
  _MYPROTO_MAPSTRINGSTRINGENTRY._serialized_start=1955
  _MYPROTO_MAPSTRINGSTRINGENTRY._serialized_end=2009
  _MYPROTO_MAPSTRINGIMPORTMESSAGEENTRY._serialized_start=1738
  _MYPROTO_MAPSTRINGIMPORTMESSAGEENTRY._serialized_end=1815
  _MYPROTO_MAPSTRINGIMPORTENUMENTRY._serialized_start=1817
  _MYPROTO_MAPSTRINGIMPORTENUMENTRY._serialized_end=1888
  _EMBEDDEDMESSAGE._serialized_start=2163
  _EMBEDDEDMESSAGE._serialized_end=2225
# @@protoc_insertion_point(module_scope)
