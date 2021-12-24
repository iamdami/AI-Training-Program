
import csv

f = open('./../_dataSetGilBut01/SEOUL.csv', 'r')
data = csv.reader(f, delimiter=',')
print(data)

dataList = []
dataListChk = []
for itemList in data:
	dataList.append(itemList)

del dataList[0]
print("총 데이터 갯수: "+str(len(dataList)))
avg = 0
low = 0
high = 0

a=0
for i in dataList:
	if (i[2] == '') or (i[3] == '') or (i[4] == '') :
		del dataList[a]
		a = a - 1
		print(a)
	else:
		dataListChk.append(i)
	a+=1

print("Null값 제거 된 후 데이터 갯수: "+str(len(dataListChk)))

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


csvfile = open('./../_dataSetGilBut01/seoulNullChk.csv','w', newline='')

csvwriter = csv.writer(csvfile)
for row in dataListChk:
	csvwriter.writerow(row)
csvfile.close()