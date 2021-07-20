# -*- coding = utf-8 -*-
# coding=gbk
from pythonds.basic import Stack
s = Stack()

print(s.isEmpty()) #测试是否为空
s.push(4)           #添加4到顶部
s.push("dog")       #添加“dog”到顶部
print(s.peek())     #返回顶部项目但不删除
s.push(True)        #添加True到顶部
print(s.size())     #查看项目数
print(s.isEmpty())
s.push(8.4)
print(s.pop())      #删除顶部项目
print(s.pop())
print(s.size())