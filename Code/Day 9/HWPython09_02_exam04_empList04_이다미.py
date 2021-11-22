import csv
file=open('./../_dataSet01/emp2.csv','r')
emp_csv=csv.reader(file)
empList = 0

EmpSalMin = int(input("검색할 연봉 하한값 입력하세요: "))
EmpSalMax = int(input("검색할 연봉 상한값 입력하세요: "))

print("연봉 %s ~ %s 인 사원 리스트" % (EmpSalMin, EmpSalMax))

print("-"*30)
print("이름   연봉")
print("-"*30)

for empList in emp_csv:
	if int(empList[5]) >= EmpSalMin and  int(empList[5]) <= EmpSalMax:
		print(empList[1], "\t", empList[5])