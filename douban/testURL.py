# -*- coding = utf-8 -*-
# coding=gbk
import urllib.request

#��ȡһ��get����
#response = urllib.request.urlopen("http://www.baidu.com")
#print(response.read().decode('utf-8'))#�Ի�ȡ��Դ����н���

#��ȡһ��post����
"""
import urllib.parse #��ֵ�Խ��������ҷ�װ
data = bytes(urllib.parse.urlencode({"Hello":"word"}), encoding="utf-8") #����Ϣת���ɶ��������ݰ������ﺬ�м�ֵ��
response = urllib.request.urlopen("http://httpbin.org/post", data= data)#data=data��ʾ���ݸ�post������
print(response.read().decode("utf-8"))
"""

#��ʱ����
"""
try:
    response = urllib.request.urlopen("http://httpbin.org/get",timeout = 0.01)
    print(response.read().decode("utf-8"))
except urllib.error.URLError as e:
    print("time out!")
"""

"""
#��ȡHeaders��Ϣ
response = urllib.request.urlopen("http://www.baidu.com")
#print(response.status) #��ӡresponse��״̬
print(response.getheader("Server")) #��ӡ��Ӧͷ
"""

#������αװ�������
#url = "http://www.douban.com"
"""
url = "http://httpbin.org/post"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"
}
data = bytes(urllib.parse.urlencode({'name':'eric'}),encoding="utf-8")
req = urllib.request.Request(url=url,data=data,headers=headers,method="POST")
response = urllib.request.urlopen(req)#reqΪ���������Ҫ��urlopen�����������
print(response.read().decode("utf-8"))
"""

#ʹ��αװ���ʶ���
url = "http://www.douban.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"
}
req = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(req)#reqΪ���������Ҫ��urlopen�����������
print(response.read().decode("utf-8"))




