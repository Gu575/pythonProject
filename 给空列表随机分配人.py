import random
offices = [[], [], []]
teacher = ["a", "b", "c", "d", "e", "f", "g", "h"]

#从教师列表中提取教师名字
for name in teacher:
    index = random.randint(0, 2)
    offices[index].append(name)

#查看每间教室有几个老师
i = 1
for office in offices:
    print("办公室%d的人数为：%d"%(i, len(office)))
    i += 1
    for name in office:
        print("%s"%name, end="\t")
    print("\n")
    print("-"*20)