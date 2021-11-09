grade = int(input("점수 입력하세요 : "))

x=["A", "B", "c"]

if grade >= 90:
	print("당신의 학점은 " + x[0] + "학점 입니다") 
elif grade >= 80:
	print("당신의 학점은 " + x[1] + "학점 입니다") 
elif grade >= 70:
	print("당신의 학점은 " + x[2] + "학점 입니다") 
else:
	print("재수강..?")