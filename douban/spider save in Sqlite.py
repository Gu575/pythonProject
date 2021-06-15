# -*- coding = utf-8 -*-
# coding=gbk
from bs4 import BeautifulSoup  #��ҳ��������ȡ����
import re   #������ʽ����������ƥ��
import urllib.request,urllib.error  #�ƶ�URL��ȡ��ҳ����
import xlwt #����Excel����
import sqlite3 #����SQLITE���ݿ����
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')

def main():
    baseurl = "https://movie.douban.com/top250?start=0"
    #1.��ȡ��ҳ
    datalist = getData(baseurl)
    dbpath = "movie.db"
    #2.��������
    #3.��������
    #saveData(datalist, savepath) #��datalist������savepath·����
    savedata2DB(datalist, dbpath)
#ӰƬ�������ӵĹ���
findlink = re.compile(r'<a href="(.*?)">')     #����������ʽ����ʾ�����ַ�����ģʽ;��������ʽ������ַ
#ӰƬͼƬ������
findImagSrc = re.compile(r'<img.*src="(.*?)"',re.S)  #re.S�û��з��������ַ���
#ӰƬ��Ƭ��
findTitle = re.compile(r'<span class="title">(.*)</span>')
#ӰƬ����
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
#�ҵ���������
findJudge = re.compile(r'<span>(\d*)������</span>')
#�ҵ��ſ�
findInq = re.compile(r'<span class="inq">(.*)</span>')
#�ҵ�ӰƬ���������
findBd = re.compile(r'<p class="">(.*?)</p>',re.S)

#��ȡ��ҳ
def getData(baseurl):
    datalist = []
    for i in range(0,10):     #���û�ȡҳ��ĺ���10��
        url = baseurl + str(i*25)
        html = askURL(url)     #�����ȡ������ҳԴ��
        #��һ��������

        soup = BeautifulSoup(html.replace('&nbsp;', ' '), "lxml") #ʹ��lxml��html�ļ����н���
        for item in soup.find_all('div', class_="item"):     #���ҷ���Ҫ����ַ������γ��б�;class_��ʾ����
            #print(item) #����:�鿴��Ӱitemȫ����Ϣ
            data = []  #����һ����Ӱ��������Ϣ
            item = str(item)        #str()�������ڱ���ַ���

            #ӰƬ��������
            link = re.findall(findlink,item)[0]     #re��ͨ��������ʽ����ָ���ַ���
            data.append(link) #���б�׷����Ϣ

            imgSrc = re.findall(findImagSrc,item)[0]
            data.append(imgSrc) #���ͼƬ

            titles = re.findall(findTitle, item)  #Ƭ������ֻ��һ��������
            if(len(titles) == 2):
                ctitle = titles[0]  #����ж����������ֻȡ��һ��
                data.append(ctitle)
                otitle = titles[1].replace("/","")#���������������ȥ��/���������
                data.append(otitle)
            else:
                data.append(titles[0])
                data.append('')     #��������ʹû�У�ҲҪ����λ�ã���������

            rating = re.findall(findRating, item)[0]
            data.append(rating)

            judgeNum = re.findall(findJudge, item)[0]
            data.append(judgeNum) #������۷���

            inq = re.findall(findInq, item)
            if len(inq) != 0:
                inq = inq[0].replace("��", "") #ȥ�����
                data.append(inq)      #��Ӹ���
            else:
                data.append("")            #����

            bd = re.findall(findBd, item)[0]
            bd = re.sub('<br(/s+)>(\s+)?', "",bd) #ȥ��һЩ����Ҫ��Ԫ��\s=�ո��
            bd = re.sub('/',"",bd)  #�滻/
            data.append(bd.strip())  #strip()ȥ��ǰ�����пո�

            datalist.append(data)   #�Ѵ���õ�һ����Ӱ��Ϣ����datalist
    print(datalist)
    return datalist

#�õ�ָ��һ��URL����ҳ����
def askURL(url):
    head = {            #ģ���������ͷ����Ϣ���¸����������������Ϣ
        "User-Agent": "Mozilla / 5.0(Windows NT 10.0; Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 91.0.4472.77Safari / 537.36"
    }
    #�û�������ʾ���߶����������������ʲô���͵Ļ���-��������������Ǹ�������������ǿ��Խ���ʲôˮƽ�����ݣ�
    #����վ������Ϣ���� = ��.����.��װ����ַ��ͷ����Ϣ������Ϊ����ͷ����Ϣ����headers,urllib.requestЯ��ͷ����Ϣ����url
    request = urllib.request.Request(url,headers = head)
    #���ַ����洢��Ϣ
    html = ""
    #���ǿ��ܷ���������
    try:
        #response��Ӧ��ʾ�ܹ����ջ�����һ������,urlopen����һ����װ�õĶ���
        response = urllib.request.urlopen(request)
        #��ȡresponse�е���Ϣ
        html = response.read().decode("utf-8")
        #print(html.encode('GBK','ignore').decode('GBk')) #����GBK�������⣬ֻ���Ⱥ��������±���
        #Ԥ�ȹ��ƿ�������������
    except urllib.error.URLError as e:
        #��ӡ����
        if hasattr(e, "code"):#�ж�e����������Ƿ����code�������
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)

    return html


#��������
def saveData(datalist, savepath):
    print("save....")
    book = xlwt.Workbook(encoding="utf-8",style_compression=0)#����workbook����
    sheet = book.add_sheet('�����ӰTop250',cell_overwrite_ok=True)#����������
    col = ("��Ӱ��������", "ͼƬ����", "ӰƬ������", "ӰƬ������", "����", "������", "�ſ�", "�����Ϣ")
    for i in range(0,8):
        sheet.write(0, i, col[i]) #����
    for i in range(0,250):
        print("��%d��"%i)
        data = datalist[i]
        for j in range(0,8):
            sheet.write(i+1,j,data[j])     #����

    book.save(savepath)  #����


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
    '''#�������ݱ�
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()


if __name__ == "__main__":     #����ִ��ʱ
#���ú���
    main()

    print("��ȡ��ϣ�")
