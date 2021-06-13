# -*- coding = utf-8 -*-
# coding=gbk


#正则表达式：字符串模式（判断字符串是否符合一定的标准)
import re
"""
#创建模式对象

pat = re.compile("AA") #此处的AA是正则表达式，用来去验证其他的字符串
pat.search("")          #search后面的字符串为被校验的内容

#m = pat.search("ABCAA")
#m = pat.search("ABCAADDDCCAAA")  #search只能找到第一次出现的字符串
print(m)
"""

"""
#没有模式对象
m = re.search("asd", "Aasd")  #前面的字符串是规则（模板），后面的字符串是被校验的对象
print(m)
"""

#print(re.findall("a", "ASDaDFGAa"))     #前面的字符串是规则（模板），后面的字符串是被校验的对象
#print(re.findall("[A-Z]", "ASDaDFGAa"))


#sub（分隔替换）

print(re.sub("a", "A", "absdasd"))   #找到a用A替换，在第三个字符串中查找

#建议在正则表达式中，被比较的字符串前面加上r(不用担心转义字符的问题)Z.B a = r"\aabd-\'"



