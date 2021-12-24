import math
def getTotalPage():
	totalData = input("총 데이터 수를 입력하세요. : ")
	showData = input("페이지당 표시할 데이터 수를 입력하세요. : ")
	
	calData = int(totalData)/int(showData)
	Page = math.ceil(calData)
	

	print("총 " +str(Page)+ "페이지 입니다.")


getTotalPage()
