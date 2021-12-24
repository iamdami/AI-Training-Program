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


print(mydict)
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

print(temperFirstLine)
print(regionName)
print(regionName)
print(regionNum)


menuNum = ''
def regionTitle():
	while True:

		print("="*30+"기온 공공데이터 분석 프로젝트 Ver01."+"="*30)
		s = "     ".join(regionMenu)
		for i in regionMenu:
			print("    "+i, end='   ')
		print('\n'+"="*96)
		menuNum = input("메뉴 선택 [Q:종료]: ")
		if menuNum.upper() == 'Q':
			print("종료합니다.")
			exit()
		selMenuChk = 0
		for mNum in range(len(regionNum)):
			if menuNum == regionNum[mNum]:
				selMenuChk = 1
				reGion = regionName[mNum]
			
		if 	selMenuChk == 1:
			print(reGion+' 지역이 선택 되었습니다.')
			break
		else:
			print(menuNum+"는 해당 지역이 없습니다.")
		

def subMenuTitle():
	print("1. 데이터 확인   2. 최고/최저 기온   3. MenuChk   4. MenuChk   5.MenuChk   6. MenuChk")
	print("-"*95)
	selMenu = input("메뉴 번호를 선택해주세요[Q:상위 메뉴]. : ")
	if selMenu.upper() == 'Q':
		return
#def subMenuChk(menuNum):

		


			
while True:
	regionTitle()
	subMenuTitle()
	#subMenuChk()