print("-"*30)
print('사원명   연봉')
print("-"*30)

import csv
file=open('./../_dataSet01/emp2.csv','r')

emp_csv=csv.reader(file)
#print(type(emp_csv))
#print(emp_csv)
for empList in emp_csv:
	#print(type(empList))
	#print(empList)
	print(empList[0], '\t',empList[5])