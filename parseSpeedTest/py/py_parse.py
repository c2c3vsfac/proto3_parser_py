from py import parser
import json

def parse(byte_str, packet_id:str):
    dict_result = parser.parse(byte_str, packet_id)
    json_result = json.dumps(dict_result, indent=2, ensure_ascii=False)
    return json_result

