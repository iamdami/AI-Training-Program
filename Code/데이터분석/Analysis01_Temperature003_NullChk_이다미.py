# -*- coding: cp949 -*-
import csv

f = open('./../_dataSetGilBut01/SEOUL.csv', 'r')
data = csv.reader(f, delimiter=',')
print(data)

dataList = []
while True:
	line = f.readline().rstrip()
	if line:
		line=line.split(',')
		dataList.append(line)
	else:
		break
del dataList[0]
print("�� ������ ����: "+str(len(dataList)))

avg = 0
low = 0
high = 0

for i in dataList:
	if i[2] == '':
		avg += 1
	if i[3] == '':
		low += 1
	if i[4] == '':
		high += 1
print("��� �µ��� null��: "+str(avg))
print("���� �µ��� null��: "+str(low))
print("�ְ� �µ��� null��: "+str(high))