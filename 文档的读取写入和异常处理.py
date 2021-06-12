# -*- coding: gbk -*-
#捕获异常
"""
try:
    print("-----test-----1---")

    f = open("123.txt","r")

    print("---test----2---")

except IOError:
    pass
"""

"""
#异常类型想要被捕获，需要类型一致
try:
    print(num)
except NameError:
    print("发生错误")
"""
"""
#将可能产生的所有异常类型全都放入小括号
try:
    print("-----test-----1---")
    f = open("123.txt", "r")
    print("---test----2---")

    print(num)
except (NameError,IOError):
    print("发生错误")
"""
"""
#获取错误描述：
try:
    print("-----test-----1---")
    f = open("123.txt", "r")
    print("---test----2---")

    print(num)
except (NameError,IOError) as result:
    print("发生错误")
    print(result)
"""
"""
#获取所有异常：Exception
try:
    print("-----test-----1---")
    f = open("123.txt", "r")
    print("---test----2---")

    print(num)
except Exception as result:
    print("发生错误")
    print(result)
"""
"""
#try.....finally 和嵌套
import time
try:
    f = open("test.txt", "r")

    try:
        while True:
            content = f.readline()
            if len(content) == 0:
                break
            time.sleep(2)
            print(content)
    finally:
        f.close()
        print("关闭文件")

except Exception as result:
    print("发生异常")

"""
# -*- coding: utf-8 -*-
#新建gushi.txt
import codecs
f = codecs.open("gushi.txt", "w")
#向gushi.txt写入一首诗
f.write("床前明月光，\n")
f.write("疑是地上霜。\n")
f.write("举头望明月，\n")
f.write("低头思故乡。\n")
f.close()

#写入两个函数，一个读取一个复制到copy.txt中，并输出复制成功
#复制文件到copy.txt的函数
def copy():
        f = open("gushi.txt", "r")
        F = open("copy.txt", "r+")

        content = f.readlines()
        for i in content:
            F.write(i)
        content1 = F.readlines()
        print(content1)
        f.close()
        F.close()

copy()

