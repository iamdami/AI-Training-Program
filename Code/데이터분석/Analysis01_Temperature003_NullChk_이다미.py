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
print("총 데이터 갯수: "+str(len(dataList)))

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
print("평균 온도의 null값: "+str(avg))
print("최저 온도의 null값: "+str(low))
print("최고 온도의 null값: "+str(high))