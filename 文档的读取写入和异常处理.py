# -*- coding: gbk -*-
#�����쳣
"""
try:
    print("-----test-----1---")

    f = open("123.txt","r")

    print("---test----2---")

except IOError:
    pass
"""

"""
#�쳣������Ҫ��������Ҫ����һ��
try:
    print(num)
except NameError:
    print("��������")
"""
"""
#�����ܲ����������쳣����ȫ������С����
try:
    print("-----test-----1---")
    f = open("123.txt", "r")
    print("---test----2---")

    print(num)
except (NameError,IOError):
    print("��������")
"""
"""
#��ȡ����������
try:
    print("-----test-----1---")
    f = open("123.txt", "r")
    print("---test----2---")

    print(num)
except (NameError,IOError) as result:
    print("��������")
    print(result)
"""
"""
#��ȡ�����쳣��Exception
try:
    print("-----test-----1---")
    f = open("123.txt", "r")
    print("---test----2---")

    print(num)
except Exception as result:
    print("��������")
    print(result)
"""
"""
#try.....finally ��Ƕ��
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
        print("�ر��ļ�")

except Exception as result:
    print("�����쳣")

"""
# -*- coding: utf-8 -*-
#�½�gushi.txt
import codecs
f = codecs.open("gushi.txt", "w")
#��gushi.txtд��һ��ʫ
f.write("��ǰ���¹⣬\n")
f.write("���ǵ���˪��\n")
f.write("��ͷ�����£�\n")
f.write("��ͷ˼���硣\n")
f.close()

#д������������һ����ȡһ�����Ƶ�copy.txt�У���������Ƴɹ�
#�����ļ���copy.txt�ĺ���
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

