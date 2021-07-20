# -*- coding = utf-8 -*-
# coding=gbk
from pythonds import Stack
#�ж������Ƿ�ƽ��ĺ���
#���̣�1.���֡�����ʱ���������ջ 2.���֡�����ʱ�Ӷ�ջɾ������һ����Ŀ 3.��ջΪ��ʱ��ʾƽ��

def parChecker(symbolString):
    s = Stack()
    index = 0
    while index < len(symbolString):
        symbol =  symbolString[index]
        if symbol == "(":
            s.push(symbol)
        else:
            s.pop()
        index += 1

    if s.isEmpty():
        return "ƽ��"
    else:
        return "��ƽ��"


print(parChecker('((()))'))
print(parChecker('(()'))