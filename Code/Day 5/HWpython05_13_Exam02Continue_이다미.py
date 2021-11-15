grade = [90, 30, 60, 50, 80]

result = "합격"

for idx in range(len(grade)): 
	if grade[idx] < 60:
		continue
	print("%d번 학생 %3d 점 %3s 입니다." % (idx+1, grade[idx], result))