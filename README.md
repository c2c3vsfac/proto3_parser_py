# proto3_parser_py
不依赖google protobuf库，性能更高的proto3格式解析程序

## Usage

```
- directory
  - proto_directory
  - proto2json.py
```

运行proto2json.py，自动生成`packet_serialization.json`文件;

## 与google protobuf对比

### 结果/result

```
google protobuf parse:
{'name': 'my_proto', 'repeated_string': ['', '一', 'two'], 'success': True, 'enum_message': 'ENUM_B', 'embedded_message': {'message': ''}, 'repeated_enum_message': ['ENUM_A', 'ENUM_B', 'ENUM_C', 'ENUM_B'], 'repeated_import_enum': ['ENUM_E', 'ENUM_D', 'ENUM_E'], 'repeated_embedded_message': [{'number': 12345}, {'message': '上山打老虎'}], 'repeated_import_message': [{'number': -129}], 'x': 1122.12377929688, 'y': -7799.55698871223, 'map_string_int': {'2': 0, '1': 4294967295}, 'map_string_string': {'1': '', '2': '\n'}, 'map_string_import_message': {'一': {'success': True, 'number': -268435456}}, 'map_string_import_enum': {'enum': 'ENUM_E'}, 'repeated_bool': [True, False, False], 'repeated_uint': [123456789, 2345678, 0, 34567], 'length_int32': 22222222, 'length_int64': '-9223372036854775808', 'length_uint64': '18446744073709551615', 'length_sint32': -2147483648, 'length_fixed64': '7777777777777', 'length_fixed32': 777777777, 'length_sfixed32': 777777777, 'length_sfixed64': '-7777777777777', 'import_enum': 'ENUM_E', 'import_message': {'number': 12999}, 'embedded_message2': {'message': 'Hello World', 'map_uint_uint': {'13579': 24680}, 'map_string_embedded_message': {'1': {'message': ''}}, 'map_string_import_message': {'1': {}}, 'map_string_import_enum': {'enum': 'ENUM_E'}, 'repeated_string': ['', '一', 'two'], 'repeated_enum_message': ['ENUM_A', 'ENUM_B', 'ENUM_C', 'ENUM_B'], 'repeated_import_message': [{'number': -129}]}}

my parser parse:
{'name': 'my_proto', 'repeated_string': ['', '一', 'two'], 'success': True, 'enum_message': 'ENUM_B', 'embedded_message': {'message': ''}, 'repeated_enum_message': ['ENUM_A', 'ENUM_B', 'ENUM_C', 'ENUM_B'], 'repeated_import_enum': ['ENUM_E', 'ENUM_D', 'ENUM_E'], 'repeated_embedded_message': [{'number': 12345}, {'message': '上山打老虎'}], 'repeated_import_message': [{'number': -129}], 'x': 1122.123779296875, 'y': -7799.55698871223, 'map_string_int': {'2': 0, '1': 4294967295}, 'map_string_string': {'2': '\n', '1': ''}, 'map_string_import_message': {'一': {'success': True, 'number': -268435456}}, 'map_string_import_enum': {'enum': 'ENUM_E'}, 'repeated_bool': [True, False, False], 'repeated_uint': [123456789, 2345678, 0, 34567], 'length_int32': 22222222, 'length_int64': -9223372036854775808, 'length_uint64': 18446744073709551615, 'length_sint32': -2147483648, 'length_fixed64': 7777777777777, 'length_fixed32': 777777777, 'length_sfixed32': 777777777, 'length_sfixed64': -7777777777777, 'import_enum': 'ENUM_E', 'import_message': {'number': 12999}, 'embedded_message2': {'message': 'Hello World', 'map_uint_uint': {13579: 24680}, 'map_string_embedded_message': {'1': {'message': ''}}, 'map_string_import_message': {'1': {}}, 'map_string_import_enum': {'enum': 'ENUM_E'}, 'repeated_string': ['', '一', 'two'], 'repeated_enum_message': ['ENUM_A', 'ENUM_B', 'ENUM_C', 'ENUM_B'], 'repeated_import_message': [{'number': -129}]}}
```

### 速度/speed

```
1557106
google protocol buffer parse 9350 package(s) cost 2.337148 second(s)
python parse 9350 package(s) cost 1.407989 second(s)

python parse 9350 package(s) cost 1.368603 second(s)
google protocol buffer parse 9350 package(s) cost 2.081040 second(s)
```
