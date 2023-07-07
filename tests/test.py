from tests import parser
import json
from protopb.MyProto_pb2 import MyProto, EmbeddedMessage
from protopb.ImportMessage_pb2 import ImportMessage
from google.protobuf import json_format

def parse(byte_str, packet_id:str):
    dict_result = parser.parse(byte_str, packet_id)
    # json_result = json.dumps(dict_result, indent=2, ensure_ascii=False, sort_keys=True)
    return dict_result

my_proto = MyProto(
    name="my_proto",
    length_uint32=0,
    repeated_string=["", "一", "two"],
    success=True,
    enum_message=1,
    embedded_message=EmbeddedMessage(message=""),
    repeated_enum_message=[0, 1, 2, 1],
    repeated_import_enum=[1, 0, 1],
    repeated_embedded_message=[EmbeddedMessage(number=12345), EmbeddedMessage(message="上山打老虎")],
    repeated_import_message=[ImportMessage(success=False, number=-129)],
    x=1122.123789654,
    y=-7799.55698871223,
    map_string_int={"1":2**32-1, "2":0},
    map_string_string={"1":"", "2":"\n"},
    map_string_import_message={"一":ImportMessage(success=True, number=-2**28)},
    map_string_import_enum={"enum": 1},
    repeated_bool=[True, False, False],
    repeated_uint=[123456789, 2345678, 0, 34567],
    length_int32=22222222,
    length_int64=-2**63,
    length_uint64=2**64-1,
    length_sint64=0,
    length_sint32=-2**31,
    length_fixed64=7777777777777,
    length_fixed32=777777777,
    length_sfixed32=777777777,
    length_sfixed64=-7777777777777,
    buffer=b'',
    import_enum=1,
    import_message=ImportMessage(success=False, number=12999),
)

embedded_message2 = my_proto.embedded_message2
embedded_message2.message = "Hello World"
embedded_message2.number=0
embedded_message2.map_uint_uint[13579]=24680
em2_msem = embedded_message2.map_string_embedded_message["1"]
em2_msem.message = ""
em2_msim = embedded_message2.map_string_import_message["1"]
em2_msim.success = False
embedded_message2.map_string_import_enum["enum"] = 1
embedded_message2.repeated_string.extend(["", "一", "two"])
embedded_message2.repeated_enum_message.extend([0, 1, 2, 1])
embedded_message2.repeated_import_message.extend([ImportMessage(success=False, number=-129)])

b_str = my_proto.SerializeToString()
print(b_str)

pb_parse = MyProto()
pb_parse.ParseFromString(b_str)
dict_result = json_format.MessageToDict(pb_parse, preserving_proto_field_name=True, float_precision=15)

print("google protobuf parse:")
print(dict_result)
print()

print("my parser parse:")
result = parse(b_str, "1")
print(result)
