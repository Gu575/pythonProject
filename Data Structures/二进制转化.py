# -*- coding = utf-8 -*-
# coding=gbk
from pythonds.basic import Stack

def a(decNumber):
    remstack = Stack()

    while decNumber > 0:
        rem =  decNumber % 2
        remstack.push(rem)
        decNumber = decNumber // 2

    binstring = ""
    while not remstack.isEmpty():
        binstring = binstring + str(remstack.pop())

    return binstring

print(a(42))