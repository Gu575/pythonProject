# -*- coding = utf-8 -*-
# coding=gbk

#�����ݱ���ΪEXCEL��ʽ
import xlwt
"""
workbook = xlwt.Workbook(encoding="utf-8") #����workbook����
worksheet = workbook.add_sheet('sheet1')    #����������
worksheet.write(0,0,'')                   #д�����ݣ���һ��������ʾ�У��ڶ�����ʾ�У�������Ϊ����
workbook.save('student.xls')                   #��������
"""

#��99�˷���д��Excel��ʽ
from openpyxl import Workbook
wb = Workbook()
ws = wb.active      #����Ĭ�Ϲ�����
ws.title = "99�˷���"

for i in range(1,10):
    for j in range(1,i+1):
        cell = ws.cell(row = i, column = j)
        cell_value = str(i) + "��" + str(j) + "=" + str(i*j)
        cell.value =  cell_value
        #ws.write(i,j, "%d*%d=%d"%(i+1,j+1,(i+1)*(j+1)))
wb.save("�žų˷���.xlsx")

print("��ϲ�㣬��񴴽��ɹ��ˣ�����")