# -*- coding = utf-8 -*-
# coding=gbk
from bs4 import BeautifulSoup  #网页解析，获取数据
import re   #正则表达式，进行文字匹配
import urllib.request,urllib.error  #制定URL获取网页数据
import xlwt #进行Excel操作
import sqlite3 #进行SQLITE数据库操作
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')

def main():
    baseurl = "https://movie.douban.com/top250?start=0"
    #1.爬取网页
    datalist = getData(baseurl)
    dbpath = "movie.db"
    #2.解析数据
    #3.保存数据
    #saveData(datalist, savepath) #将datalist保存在savepath路径下
    savedata2DB(datalist, dbpath)
#影片详情链接的规则
findlink = re.compile(r'<a href="(.*?)">')     #创建正则表达式，表示规则（字符串的模式;用正则表达式描述网址
#影片图片的链接
findImagSrc = re.compile(r'<img.*src="(.*?)"',re.S)  #re.S让换行符包含在字符中
#影片的片名
findTitle = re.compile(r'<span class="title">(.*)</span>')
#影片评分
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
#找到评价人数
findJudge = re.compile(r'<span>(\d*)人评价</span>')
#找到概况
findInq = re.compile(r'<span class="inq">(.*)</span>')
#找到影片的相关内容
findBd = re.compile(r'<p class="">(.*?)</p>',re.S)

#爬取网页
def getData(baseurl):
    datalist = []
    for i in range(0,10):     #调用获取页面的函数10次
        url = baseurl + str(i*25)
        html = askURL(url)     #保存获取到的网页源码
        #逐一解析数据

        soup = BeautifulSoup(html.replace('&nbsp;', ' '), "lxml") #使用lxml对html文件进行解析
        for item in soup.find_all('div', class_="item"):     #查找符合要求的字符串，形成列表;class_表示属性
            #print(item) #测试:查看电影item全部信息
            data = []  #保存一部电影的所有信息
            item = str(item)        #str()将括号内变成字符串

            #影片详情链接
            link = re.findall(findlink,item)[0]     #re库通过正则表达式查找指定字符串
            data.append(link) #像列表追加信息

            imgSrc = re.findall(findImagSrc,item)[0]
            data.append(imgSrc) #添加图片

            titles = re.findall(findTitle, item)  #片名可能只有一个中文名
            if(len(titles) == 2):
                ctitle = titles[0]  #如果有多个中文名，只取第一个
                data.append(ctitle)
                otitle = titles[1].replace("/","")#如果有外文名，则去掉/输出外文名
                data.append(otitle)
            else:
                data.append(titles[0])
                data.append('')     #外文名即使没有，也要留空位置，否则会混乱

            rating = re.findall(findRating, item)[0]
            data.append(rating)

            judgeNum = re.findall(findJudge, item)[0]
            data.append(judgeNum) #添加评价分数

            inq = re.findall(findInq, item)
            if len(inq) != 0:
                inq = inq[0].replace("。", "") #去掉句号
                data.append(inq)      #添加概述
            else:
                data.append("")            #留空

            bd = re.findall(findBd, item)[0]
            bd = re.sub('<br(/s+)>(\s+)?', "",bd) #去掉一些不需要的元素\s=空格键
            bd = re.sub('/',"",bd)  #替换/
            data.append(bd.strip())  #strip()去掉前后所有空格

            datalist.append(data)   #把处理好的一部电影信息放入datalist
    print(datalist)
    return datalist

#得到指定一个URL的网页内容
def askURL(url):
    head = {            #模拟浏览器的头部信息，下个豆瓣服务器发送消息
        "User-Agent": "Mozilla / 5.0(Windows NT 10.0; Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 91.0.4472.77Safari / 537.36"
    }
    #用户代理，表示告诉豆瓣服务器，我们是什么类型的机器-浏览器（本质上是告诉浏览器，我们可以接受什么水平的内容）
    #向网站发送消息变量 = 库.对象.封装（网址，头部信息）作用为：把头部信息给到headers,urllib.request携带头部信息访问url
    request = urllib.request.Request(url,headers = head)
    #用字符串存储信息
    html = ""
    #考虑可能发生的问题
    try:
        #response响应表示能够接收回来的一个对象,urlopen传递一个封装好的对象
        response = urllib.request.urlopen(request)
        #读取response中的信息
        html = response.read().decode("utf-8")
        #print(html.encode('GBK','ignore').decode('GBk')) #出现GBK编译问题，只能先忽略再重新编译
        #预先估计可能遇到的问题
    except urllib.error.URLError as e:
        #打印问题
        if hasattr(e, "code"):#判断e这个对象里是否包含code这个属性
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)

    return html


#保存数据
def saveData(datalist, savepath):
    print("save....")
    book = xlwt.Workbook(encoding="utf-8",style_compression=0)#创建workbook对象
    sheet = book.add_sheet('豆瓣电影Top250',cell_overwrite_ok=True)#创建工作表
    col = ("电影详情链接", "图片链接", "影片中文名", "影片外文名", "评分", "评价数", "概况", "相关信息")
    for i in range(0,8):
        sheet.write(0, i, col[i]) #列名
    for i in range(0,250):
        print("第%d条"%i)
        data = datalist[i]
        for j in range(0,8):
            sheet.write(i+1,j,data[j])     #数据

    book.save(savepath)  #保存


def savedata2DB(datalist, dbpath):
    init_db(dbpath)
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()

    for data in datalist:
        for index in range(len(data)):
            if index == 4 or index == 5:
                continue
            data[index] = '"'+data[index]+'"'
        sql = '''
                insert into movie250(
                info_link,pic_link,cname,ename,score,rated,instruction,info)
                values(%s)'''%",".join(data)
        print(sql)
        cur.execute(sql)
        conn.commit()
    cur.close()
    conn.close()

def init_db(dbpath):
    sql = '''
        create table movie250
        (
        id integer primary key autoincrement,
        info_link text,
        pic_link text,
        cname varchar,
        ename varchar,
        score numeric,
        rated numeric,
        instruction text,
        info text
        )
    '''#创建数据表
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()


if __name__ == "__main__":     #程序执行时
#调用函数
    main()

    print("爬取完毕！")
