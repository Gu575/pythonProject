# -*- coding = utf-8 -*-
# coding=gbk
import sqlite3

#1.�������ݿ�
conn = sqlite3.connect("test1.db")   #�򿪻򴴽����ݿ��ļ�

#print("open database successfully")
print("�ɹ������ݿ�")

#2.�������ݱ�
'''
c = conn.cursor()       #��ȡ�α�
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

c.execute(sql)          #ִ��sql
conn.commit()           #�ύsql����
conn.close()            #�ر����ݿ�����

print("�ɹ�����")

'''

#4.��������
'''
c = conn.cursor()       #��ȡ�α�
'''
sql1 = '''
    insert OR IGNORE into company(id, name ,age,address,salary)
    values(1,'����',32,"����",8000)

'''
'''
'''
sql2 = '''
    insert OR IGNORE into company(id, name ,age,address,salary)
    values(2,'����',30,"����",800)

'''
'''
c.execute(sql1)          #ִ��sql
c.execute(sql2)
conn.commit()           #�ύsql����
conn.close()            #�ر����ݿ�����

print("�����������")
'''

#��ѯ����
c = conn.cursor()       #��ȡ�α�

sql1 = '''
    select id, name, address, salary from company
'''

cursor = c.execute(sql1)          #ִ��sql
for row in cursor:
    print("id = ", row[0])
    print("name =", row[1])
    print("address = ",row[2])
    print("salar = ",row[3],"\n")
conn.close()            #�ر����ݿ�����

print("��ѯ���")






