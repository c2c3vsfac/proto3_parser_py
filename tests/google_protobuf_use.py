import re
import os

# 第一步 编译所需proto及依赖链

file_path = os.getcwd()

def export_need_import(proto_name):
    full_file_path = file_path + "\\proto\\" + proto_name + ".proto"
    need_import = []
    import_line = {proto_name + ".proto"}
    try:
        f = open(full_file_path, "r")
        lines = f.readlines()
        f.close()
    except FileNotFoundError:
        return False
    for line in lines:
        if line.startswith("import"):
            file_whole_name = re.findall(r'"(.*)"', re.split(" ", line)[1])[0]
            file_name = file_whole_name.replace(".proto", "")
            need_import.append(file_name)
    if need_import:
        for import_name in need_import:
            extend_line = export_need_import(import_name)
            import_line |= extend_line
    return import_line

set_result = export_need_import("your_proto_name")
str_res = " ".join(set_result)
print(str_res)

# protoc -I input_directory --python_out=output_directory proto_and_import_line or input_directory\*.proto

# 第二步 修改import(可选)

# 若不修改，python文件必须和编译后的proto放在同一目录下，否则只要proto间有依赖就会报错ImportError
# 文件结构如下所示
"""
- directory
    - main.py
    - compile_pb2_file.py
"""

def replace_import(proto_name):
    full_file_path = file_path + "\\protopb\\" + proto_name
    try:
        with open(full_file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        return False

    new_text = ""
    for line in lines:
        if line.startswith("import ") and line.endswith("__pb2\n") and " as " in line:
            new_text += "from . " + line
        else:
            new_text += line

    with open(full_file_path, "w", encoding="utf-8") as fw:
        fw.write(new_text)

pb2_files = os.listdir("./protopb")
for file in pb2_files:
    replace_import(file)

# 修改后的编译后的proto可以放在与python文件不同的目录下，运行时会自动处理依赖关系
# 文件结构如下所示
"""
- directory
    - main.py
    - protopb
        - compile_pb2_file.py
"""

# 使用

from protopb.GCGAskDuelRsp_pb2 import GCGAskDuelRsp
from protopb.GCGMsgAddDice_pb2 import GCGMsgAddDice
from protopb.GCGMessage_pb2 import GCGMessage
from protopb.GCGMessagePack_pb2 import GCGMessagePack
from protopb.GCGDuel_pb2 import GCGDuel
from protopb.GCGMsgDiceRoll_pb2 import GCGMsgDiceRoll
from google.protobuf import json_format

# 推荐使用 字段名=值 的方式， 否则列表和map需要以如下方式
# enum直接用对应的编号

add_dice_message = GCGMsgAddDice()
add_dice_message.JMNNIEOBKHA.update({1: 1, 2: 3, 5: 1, 3: 3, 4: 1, 6: 3}) # map
dice_roll = GCGMsgDiceRoll()
dice_roll.dice_side_list.extend([1, 2, 3, 4, 5]) # repeated
gcg_message = GCGMessage(add_dice=add_dice_message)
gcg_message2 = GCGMessage(dice_roll=dice_roll)
gcg_message_pack = GCGMessagePack(msg_list=[gcg_message, gcg_message2])
gcg_duel = GCGDuel(history_msg_pack_list=[gcg_message_pack])
gcg_ask_duel = GCGAskDuelRsp(duel=gcg_duel)

# 序列化
b_str = gcg_ask_duel.SerializeToString()

# 反序列化
add_dice = GCGAskDuelRsp()
add_dice.ParseFromString(b_str)
json_result = json_format.MessageToJson(add_dice, preserving_proto_field_name=True) # 不设为True会以小驼峰命名法命名字段名