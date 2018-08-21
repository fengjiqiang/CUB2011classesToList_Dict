# 列表类型
f = open('classes.txt', 'r')
re = []
for i in f.readlines():
    lst = i.strip().split(".")
    if(lst[1] not in re):
        re.append(lst[1])
f.close()
# print(re)

# fromfile.txt来源
# for index, item in enumerate(re):
    # print(index, item)

# 字典类型
dt = {}
with open('fromfile.txt', 'r') as dict_file:
    for line in dict_file:
        (key, value) = line.strip().split(' ')
        dt[key] = value
# with open语句不必调用f.close()方法
print(dt)

# 列表写入txt文件
# f1 = open('new_classes.txt', 'w')
# for s in re:
#     f1.write(s)
#     f1.write('\n')
# f1.close()
