## paging
# ===================
# ** 계략적 변수 이해
#    totalData		:  총데이터 수
#    dataPerPage 		:  페이지당 보여질 데이터 수
#    totalPage		:  총페이지수 
#    nowPage		:  현제페이지 위치
#    dataOfBeginPage		:  시작페이지의 레코드값
import csv
temperData=open("../_dataSetGilBut01/seoulNullChk.csv","r")
temperData=csv.reader(temperData)

def getTotalPage(m, n):
  if m % n == 0:
    return m // n
  else:
    return m // n + 1

dataList = []
for i in temperData:
  dataList.append(i)

dataPerPage=int(input("한 페이지당 출력할 레코드 수를 입력하세요:"))
totalPage=getTotalPage(len(dataList), dataPerPage)


print("-"*40)
print("기온 공공데이터 개수: "+str(len(dataList)))
print("기온 공공데이터 페이지 개수: "+str(totalPage))
print("-"*40)



Page=0
showPage=1
while True:
  print("Enter를 치면 다음", showPage,"/",totalPage, "페이지", dataPerPage,"개 레코드 확인") 
  nowPage=input("확인할 페이지를 입력 또는 Enter[Q:종료]:")
  if nowPage.upper()=="Q":
    print("종료합니다.")
    break
  elif nowPage=="":
    showPage+=1
    if showPage==totalPage:
      print("마지막 페이지입니다.")
    else:
      for dataOfBeginPage in range(Page,(Page+dataPerPage)):
        print(dataOfBeginPage,"/",len(dataList), dataOfBeginPage,"번째", dataList[dataOfBeginPage])
        Page+=1
      print("-"*50)
  else:
    dataOfBeginPage=(int(nowPage)-1)*dataPerPage
    for dataOfBeginPage in range((dataOfBeginPage),(dataOfBeginPage+dataPerPage)):
      for idx in range(len(dataList)):
        pass
      if dataOfBeginPage > len(dataList)-1:
        print("페이지 초과.")
        break
      else:
        print(dataOfBeginPage,"/",len(dataList), dataOfBeginPage,"번째", dataList[dataOfBeginPage])
        showPage=int(nowPage)
