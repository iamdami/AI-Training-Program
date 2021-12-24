
import csv

f = open('./../_dataSetGilBut01/seoulNullChk.csv', 'r')
data = csv.reader(f, delimiter=',')
print(data)

dataList = []
highTemp = []
lowTemp= []
for itemList in data:
	dataList.append(itemList)

vMax = -999999

vMin = 999999

for idx in dataList:
	if vMax < float(idx[4]):
		vMax = float(idx[4])
		HDate = idx[0]

	if vMin > float(idx[3]):
		vMin = float(idx[3])
		LDate = idx[0]
	
for i in dataList:
	if float(i[4]) == vMax:
		highTemp.append(i)
	if float(i[3]) == vMin:
		lowTemp.append(i)
	
print(highTemp)
print(lowTemp)



print('최고 기온은 '+ HDate+"에 "+str(vMax))
print('최저 기온은 '+LDate+"에 "+str(vMin))
