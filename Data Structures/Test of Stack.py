# -*- coding = utf-8 -*-
# coding=gbk
from pythonds.basic import Stack
s = Stack()

print(s.isEmpty()) #�����Ƿ�Ϊ��
s.push(4)           #���4������
s.push("dog")       #��ӡ�dog��������
print(s.peek())     #���ض�����Ŀ����ɾ��
s.push(True)        #���True������
print(s.size())     #�鿴��Ŀ��
print(s.isEmpty())
s.push(8.4)
print(s.pop())      #ɾ��������Ŀ
print(s.pop())
print(s.size())