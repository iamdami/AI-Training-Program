## paging
'''
===================
** 계략적 변수 이해
   totalData		:  총데이터 수
   dataPerPage 		:  페이지당 보여질 데이터 수

   totalPage		:  총페이지수
   nowPage		:  현제페이지 위치

   dataOfBeginPage		:  시작페이지의 레코드값
   '''
def getTotalPage(m, n):
  if m % n == 0:
    return m // n
  else:
    return m // n + 1
        

while True:
  totalData=int(input("총 데이터 갯수 : "))
  dataPerPage=int(input("페이지당 보여줄 데이터 갯수:"))
  totalPage=getTotalPage(totalData, dataPerPage)
  print("총"+str(totalPage)+"페이지입니다.")

  nowPage=int(input("확인할 페이지를 입력하세요. :"))
  for x in range(((nowPage-1)*dataPerPage),(nowPage*dataPerPage)):
    if x > totalData:
      print()
      print("페이지를 다시 입력해주세요.")
      break
    else:
      print(str(x)+ "번 데이터 확인")