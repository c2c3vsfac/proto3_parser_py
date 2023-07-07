from cpp import cpp_parse
from protobuf import pb_parse
from py import py_parse
import time

source = []
#
with open("20230702021809.txt", "r", encoding="utf-8") as source_file:
    lines = source_file.readlines()
    for line in lines:
        index = line[:10].find(" ")
        source.append((line[:index], eval(line[index+1:-1])))

total = len(source)

length = 0
for each in source:
    length += len(each[1])
print(length)


# start_time = time.time()
# # pb = open("google.txt", "w")
# for each in source:
#     result = pb_parse.parse(each[1], each[0])
#     # pb.write(each[0] + "\n")
#     # pb.write(result + "\n")
# end_time = time.time()
# print("google protocol buffer parse %d package(s) cost %f second(s)" % (total, end_time-start_time))
# #
# start_time = time.time()
# # py = open("py.txt", "w")
# for each in source:
#     result = py_parse.parse(each[1], each[0])
#     # py.write(each[0] + "\n")
#     # py.write(result + "\n")
# end_time = time.time()
# print("python parse %d package(s) cost %f second(s)" % (total, end_time-start_time))

start_time = time.time()
# py = open("py.txt", "w")
for each in source:
    result = py_parse.parse(each[1], each[0])
    # py.write(each[0] + "\n")
    # py.write(result + "\n")
end_time = time.time()
print("python parse %d package(s) cost %f second(s)" % (total, end_time-start_time))

start_time = time.time()
# pb = open("google.txt", "w")
for each in source:
    result = pb_parse.parse(each[1], each[0])
    # pb.write(each[0] + "\n")
    # pb.write(result + "\n")
end_time = time.time()
print("google protocol buffer parse %d package(s) cost %f second(s)" % (total, end_time-start_time))

# start_time = time.time()
# for each in source:
#     cpp_parse.parse(each[1], each[0])
# end_time = time.time()
# print("c++ parse %d package(s) cost %f second(s)" % (total, end_time-start_time))

