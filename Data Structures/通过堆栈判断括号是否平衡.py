# -*- coding = utf-8 -*-
# coding=gbk
from pythonds import Stack
#判断括号是否平衡的函数
#流程：1.出现“（”时将它放入堆栈 2.出现“）”时从堆栈删除顶部一个项目 3.堆栈为空时表示平衡

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
        return "平衡"
    else:
        return "不平衡"


print(parChecker('((()))'))
print(parChecker('(()'))