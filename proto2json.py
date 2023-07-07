import re
import os
import json


def read_proto(file):
    try:
        with open(file, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("找不到文件：" + file)
        return False
    proto_name = os.path.basename(file).split(".")[0]
    need_import = []
    enum_dict = {}
    message_return_dict = {}
    message_prop_name = {}
    other_message = {}
    save = []
    for line in lines:
        line = line.lstrip()
        if not line.startswith("//"):

            # 去掉注释
            end_pos = line.find(";")
            if end_pos != -1:
                line = line[:end_pos + 1]

            # 解的proto有时用\t有时用空格
            split_line = re.split(" ", line)
            split_line = [each for each in split_line if each] # 连续多空格
            if line.startswith("import"):
                file_whole_name = re.findall(r'"(.*)"', split_line[1])[0]
                file_name = re.sub(".proto", "", file_whole_name)
                need_import.append(file_name)
                continue
            elif line.startswith("message"):
                save.append((split_line[0], split_line[1], {}, {}))
                continue
            elif line.startswith("enum"):
                save.append((split_line[0], split_line[1], {}))
                continue
            elif line.startswith("}\n") or line.startswith("}"):
                if save:  # oneof 会有多余的括号
                    if save[-1][0] == "message":
                        if save[-1][1] == proto_name:
                            message_return_dict = save[-1][2]
                            message_prop_name = save[-1][3]
                        else:
                            other_message[save[-1][1]] = [save[-1][2], save[-1][3]]
                        save.pop(-1)
                    elif save[-1][0] == "enum":
                        enum_dict[save[-1][1]] = save[-1][2]
                        save.pop(-1)
                continue
            if save:
                if save[-1][0] == "enum":
                    data_id = re.findall("\d+", split_line[2])[0]
                    save[-1][2][data_id] = split_line[0]
                else:
                    if len(split_line) > 3:  # 空行,忽略oneof
                        if split_line[0] == 'optional':
                            split_line.pop(0)
                        if len(split_line) == 4:
                            prop = split_line[1]
                            data_id = re.findall("\d+", split_line[3])[0]
                            save[-1][2][data_id] = split_line[0]
                            save[-1][3][data_id] = prop
                        elif len(split_line) == 5:  # repeated and map
                            if split_line[0] == "repeated":
                                data_type = split_line[1]
                                prop = split_line[2]
                                data_id = re.findall("\d+", split_line[4])[0]
                                save[-1][2][data_id] = "repeated_" + data_type
                                save[-1][3][data_id] = prop
                            else:
                                data_type = split_line[0] + split_line[1]
                                type_name = re.findall("map<(.*)>", data_type)[0]
                                type1, type2 = re.split(",", type_name)
                                prop = split_line[2]
                                data_id = re.findall("\d+", split_line[4])[0]
                                save[-1][2][data_id] = [type1, type2]
                                save[-1][3][data_id] = prop
    return need_import, enum_dict, message_return_dict, message_prop_name, other_message

def convert(proto_name, other=False, other_struct:tuple=None):
    if other:
        need_import, enum_dict, encoding_rules, prop_name, other_message = other_struct
    else:
        file_path = os.getcwd()
        proto_name = file_path + "\\proto\\" + proto_name + ".proto"
        need_import, enum_dict, encoding_rules, prop_name, other_message = read_proto(proto_name)
    for key, value in encoding_rules.items():
        if value in need_import:
            import_enum_dict, d_rule, d_name = convert(value)
            if value in import_enum_dict:
                encoding_rules[key] = "enum"
                prop_name[key] = {prop_name[key]: import_enum_dict[value]}
            else:
                encoding_rules[key] = [d_rule, d_name]
        elif isinstance(value, list):  # map第一位只能为整数或字符串
            if value[1] in need_import:
                import_enum_dict, d_rule, d_name = convert(value[1])
                if value[1] in import_enum_dict:
                    encoding_rules[key] = {"map": [value[0], ["enum", import_enum_dict[value[1]]]]}
                else:
                    encoding_rules[key] = {"map": [value[0], [d_rule, d_name]]}
            elif value[1] in other_message:
                other_message_enum_dict, d_rule, d_name = convert("", other=True, other_struct=(
                need_import, enum_dict, other_message[value[1]][0], other_message[value[1]][1], other_message))
                encoding_rules[key] = {"map": [value[0], [d_rule, d_name]]}
            else:
                encoding_rules[key] = {"map": value}
        elif value.replace("repeated_", "") in need_import:
            need_import_proto_name = value.replace("repeated_", "")
            import_enum_dict, d_rule, d_name = convert(need_import_proto_name)
            if need_import_proto_name in import_enum_dict:
                encoding_rules[key] = "repeated_enum"
                prop_name[key] = [prop_name[key], import_enum_dict[need_import_proto_name]]
            else:
                encoding_rules[key] = {"repeated": [d_rule, d_name]}
        elif value.startswith("repeated_") and re.sub("repeated_", "", value) in enum_dict:
            embedded_enum_proto_name = value.replace("repeated_", "")
            encoding_rules[key] = "repeated_enum"
            prop_name[key] = [prop_name[key], enum_dict[embedded_enum_proto_name]]
        elif value in other_message:
            other_message_enum_dict, d_rule, d_name = convert("", other=True, other_struct=(need_import, enum_dict, other_message[value][0], other_message[value][1], other_message))
            encoding_rules[key] = [d_rule, d_name]
        elif value.replace("repeated_", "") in other_message and value.startswith("repeated_"):
            other_message_proto_name = value.replace("repeated_", "")
            other_message_enum_dict, d_rule, d_name = convert("", other=True, other_struct=(
            need_import, enum_dict, other_message[other_message_proto_name][0], other_message[other_message_proto_name][1], other_message))
            encoding_rules[key] = {"repeated": [d_rule, d_name]}
        elif value in enum_dict:
            encoding_rules[key] = "enum"
            prop_name[key] = {prop_name[key]: enum_dict[value]}
    return enum_dict, encoding_rules, prop_name

f = open("packet_serialization.json", "w", encoding="utf-8")
f.write("{\n")
_, encoding_rules, prop_names = convert("MyProto")
f.write(json.dumps("1") + ": " + json.dumps([encoding_rules, prop_names]))
f.write("\n}")
f.close()

