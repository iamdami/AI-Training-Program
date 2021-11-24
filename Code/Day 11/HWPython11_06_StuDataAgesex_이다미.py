import csv
file=open('./../_dataSet01/StuDataSet02.csv','r')

stu_csv=csv.reader(file)
print(stu_csv)

stuList=0
stuAge=0
stuGender=0

for stuList in stu_csv:

	if stuList[2][:1] == "0":
		stuAge = 2021 - (int(stuList[2][:2])+2000)
	else:
		stuAge = 2021 - (int(stuList[2][:2])+1900)
	
	if int(stuList[2][7]) == 1 or int(stuList[2][7]) == 3:
		stuGender="남자"
	elif int(stuList[2][7]) == 2 or int(stuList[2][7]) == 4:
		stuGender="여자"
	else:
		pass
	print(stuList[1]+" "+str(stuAge)+" "+str(stuGender))