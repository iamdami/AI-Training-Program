# 검색 연령 하한, 상한값 입력 -> 이름 나이 통신사 전번
import csv
file=open('./../_dataSet01/StuDataSet02.csv','r')

stu_csv=csv.reader(file)
print(stu_csv)

ageMin= int(input("검색할 연령(하한)을 입력하세요: "))
ageMax=int(input("검색할 연령(상한)을 입력하세요: "))
print()
print("## %d세 ~ %d세 학생 리스트 " % (ageMin, ageMax))
print()
print("="*30)
print("이름 ", "나이 ", "통신사 ", "전화번호 ")
print("-"*30)

for stuList in stu_csv:

	if stuList[2][:1] == "0":
		stuAge = 2021 - (int(stuList[2][:2])+2000)
	else:
		stuAge = 2021 - (int(stuList[2][:2])+1900)

	if stuAge <= ageMax and stuAge >= ageMin:
		print(stuList[1]+" "+str(stuAge)+" "+stuList[4]+" "+stuList[3])
