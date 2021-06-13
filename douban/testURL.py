# -*- coding = utf-8 -*-
# coding=gbk
import urllib.request

#获取一个get请求：
#response = urllib.request.urlopen("http://www.baidu.com")
#print(response.read().decode('utf-8'))#对获取的源码进行解码

#获取一个post请求：
"""
import urllib.parse #键值对解析器并且封装
data = bytes(urllib.parse.urlencode({"Hello":"word"}), encoding="utf-8") #把信息转换成二进制数据包，包里含有键值对
response = urllib.request.urlopen("http://httpbin.org/post", data= data)#data=data表示传递给post的内容
print(response.read().decode("utf-8"))
"""

#超时处理
"""
try:
    response = urllib.request.urlopen("http://httpbin.org/get",timeout = 0.01)
    print(response.read().decode("utf-8"))
except urllib.error.URLError as e:
    print("time out!")
"""

"""
#获取Headers信息
response = urllib.request.urlopen("http://www.baidu.com")
#print(response.status) #打印response的状态
print(response.getheader("Server")) #打印响应头
"""

#将爬虫伪装成浏览器
#url = "http://www.douban.com"
"""
url = "http://httpbin.org/post"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"
}
data = bytes(urllib.parse.urlencode({'name':'eric'}),encoding="utf-8")
req = urllib.request.Request(url=url,data=data,headers=headers,method="POST")
response = urllib.request.urlopen(req)#req为请求对象，需要用urlopen发送请求对象
print(response.read().decode("utf-8"))
"""

#使用伪装访问豆瓣
url = "http://www.douban.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"
}
req = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(req)#req为请求对象，需要用urlopen发送请求对象
print(response.read().decode("utf-8"))




