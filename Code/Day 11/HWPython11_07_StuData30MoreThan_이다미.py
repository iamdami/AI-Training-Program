# 나이가 30 이상인 학생들의 이름, 나이
import csv
file=open('./../_dataSet01/StuDataSet02.csv','r')

stu_csv=csv.reader(file)
print(stu_csv)

stuList=0
stuAge=0

for stuList in stu_csv:

	if stuList[2][:1] == "0":
		stuAge = 2021 - (int(stuList[2][:2])+2000)
	else:
		stuAge = 2021 - (int(stuList[2][:2])+1900)
	
	if stuAge >= 30:
		print(stuList[1]+" "+str(stuAge))