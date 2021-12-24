import csv

regionMenu = []
temperRegionFileList = ['seoulNullChk.csv', 'daejeonNullChk.csv', 'daeguNullChk.csv', 'busanNullChk.csv', 'gwangjuNullChk.csv']
temperFirstLine= []
regionName = []
regionNum = []

mydict = {}

with open('./../_dataSetGilBut01/temperRegionChk.csv', mode='r') as rData:
    rData = csv.reader(rData)
    mydict = {rows[0]:rows[1] for rows in rData}



for dataIdx in range(len(temperRegionFileList)):
	regionData = open("./../_dataSetGilBut01/"+temperRegionFileList[dataIdx], 'r')
	vData = csv.reader(regionData)
	vHeader = next(vData)
	temperFirstLine.append(vHeader)
	regionData.close()
	
for key, value in mydict.items():
	for idx in temperFirstLine:
		if key == idx[1]:
			regionNum.append(idx[1])
			regionName.append(value)
			regionMenu.append(value+":"+idx[1])
regionMenu.append("Q. 종료")
print(regionName)
print(regionNum)
print(regionMenu)

def regionTitle():
	print("="*30+"기온 공공데이터 분석 프로젝트 Ver01."+"="*30)
	s = "     ".join(regionMenu)
	for i in regionMenu:
		print("    "+i, end='   ')
	print('\n'+"="*96)


def menuSel():
	menuNum = input("메뉴 선택: ")
	if menuNum.upper() == 'Q':
		exit()
	
			
while True:
	Menu()
	menuSel()