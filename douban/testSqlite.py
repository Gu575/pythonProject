# -*- coding = utf-8 -*-
# coding=gbk
import sqlite3

#1.连接数据库
conn = sqlite3.connect("test1.db")   #打开或创建数据库文件

#print("open database successfully")
print("成功打开数据库")

#2.创建数据表
'''
c = conn.cursor()       #获取游标
'''
sql = '''
    create table company
        (id int primary key not null,
        name text not null,
        age int not null,
        address char(50),
        salary real);
'''
'''

c.execute(sql)          #执行sql
conn.commit()           #提交sql操作
conn.close()            #关闭数据库链接

print("成功建表")

'''

#4.插入数据
'''
c = conn.cursor()       #获取游标
'''
sql1 = '''
    insert OR IGNORE into company(id, name ,age,address,salary)
    values(1,'张三',32,"苏州",8000)

'''
'''
'''
sql2 = '''
    insert OR IGNORE into company(id, name ,age,address,salary)
    values(2,'李四',30,"苏州",800)

'''
'''
c.execute(sql1)          #执行sql
c.execute(sql2)
conn.commit()           #提交sql操作
conn.close()            #关闭数据库链接

print("插入数据完毕")
'''

#查询数据
c = conn.cursor()       #获取游标

sql1 = '''
    select id, name, address, salary from company
'''

cursor = c.execute(sql1)          #执行sql
for row in cursor:
    print("id = ", row[0])
    print("name =", row[1])
    print("address = ",row[2])
    print("salar = ",row[3],"\n")
conn.close()            #关闭数据库链接

print("查询完毕")






