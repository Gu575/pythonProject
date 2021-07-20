# -*- coding = utf-8 -*-
# coding=gbk
from pythonds import Stack
#判断括号是否平衡的函数
#流程：1.出现“（”时将它放入堆栈 2.出现“）”时从堆栈删除顶部一个项目 3.堆栈为空时表示平衡

def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top,symbol):
                       balanced = False
        index = index + 1
    if balanced and s.isEmpty():
        return True
    else:
        return False

def matches(open,close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)


print(parChecker('{({([][])}())}'))
print(parChecker('[{()]'))