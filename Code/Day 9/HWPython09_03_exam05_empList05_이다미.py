import csv
file=open('./../_dataSet01/emp2.csv','r')
emp_csv=csv.reader(file)
empList = 0

print("사원 중 보너스가 0이 아닌 사원 리스트 출력")

print("보너스 확인")

print("-"*30)
print("이름   보너스")
print("-"*30)

for empList in emp_csv:
	if empList[6] != "0":
		print(empList[1], "\t", empList[6])