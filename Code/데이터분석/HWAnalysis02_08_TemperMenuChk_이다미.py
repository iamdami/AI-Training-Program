import csv

regionMenu = ["서울 : 108","대전 : 133","대구 : 143", "부산 : 159" , "광주 : 156", "Q. 종료"]
temperRegionFileList = ['seoulNullChk.csv', 'daejeonNullChk.csv', 'daeguNullChk.csv', 'busanNullChk.csv', 'gwangjuNullChk.csv']
temperFirstLine= []

for dataName in range(len(temperRegionFileList)):
	regionData = open("./../_dataSetGilBut01/"+temperRegionFileList[dataName], 'r')
	vData = csv.reader(regionData)
	header = next(vData)
	temperFirstLine.append(header)
	
print(temperFirstLine)

def Menu():
	print("="*30+"기온 공공데이터 분석 프로젝트 Ver01."+"="*30)
	s = "     ".join(regionMenu)
	for i in regionMenu:
		print(i, end=' ')
	print('\n'+"="*96)


def menuSel():
	menuNum = input("메뉴 선택: ")
	if menuNum.upper() == 'Q':
		exit()
	
			
while True:
	Menu()
	menuSel()