import os

file_path = "."

def replace_import(proto_name):
    full_file_path = file_path + "\\protopb\\" + proto_name
    try:
        with open(full_file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("%s not found" % proto_name)
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
    if file.endswith(".py"):
        replace_import(file)