# -*- coding = utf-8 -*-
# coding=gbk


#������ʽ���ַ���ģʽ���ж��ַ����Ƿ����һ���ı�׼)
import re
"""
#����ģʽ����

pat = re.compile("AA") #�˴���AA��������ʽ������ȥ��֤�������ַ���
pat.search("")          #search������ַ���Ϊ��У�������

#m = pat.search("ABCAA")
#m = pat.search("ABCAADDDCCAAA")  #searchֻ���ҵ���һ�γ��ֵ��ַ���
print(m)
"""

"""
#û��ģʽ����
m = re.search("asd", "Aasd")  #ǰ����ַ����ǹ���ģ�壩��������ַ����Ǳ�У��Ķ���
print(m)
"""

#print(re.findall("a", "ASDaDFGAa"))     #ǰ����ַ����ǹ���ģ�壩��������ַ����Ǳ�У��Ķ���
#print(re.findall("[A-Z]", "ASDaDFGAa"))


#sub���ָ��滻��

print(re.sub("a", "A", "absdasd"))   #�ҵ�a��A�滻���ڵ������ַ����в���

#������������ʽ�У����Ƚϵ��ַ���ǰ�����r(���õ���ת���ַ�������)Z.B a = r"\aabd-\'"



