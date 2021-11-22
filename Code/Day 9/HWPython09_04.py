import csv
file=open('D:\dami\PythonTest\HWPython09_02_exam04_empList04_이다미\_dataSet01\emp2.csv','r')
emp_csv=csv.reader(file)
empList = 0

EmpJob = str(input("검색할 직업을 입력하세요: ").split(","))

print("직업이 %s 인 직원 리스트" % EmpJob )

print("-"*30)
print("이름     직업     급여")
print("-"*30)

for empList in emp_csv:
	if str(empList[2]) == EmpJob or  str(empList[2]) == EmpJob:
		print(empList[1], "\t", empList[2], "\t", empList[5])