grade = [90, 30, 60, 50, 80]

#for idx in range(len(grade)): 
   #result = grade[idx] 
   #print('{idx+1}번 학생 {result} 점 합 격' if result >= 60 else f'{idx+1}번 학생 {result} 점 불합격'))


for idx in range(len(grade)): 
   result = "합격" if grade[idx] >= 60 else "불합격"
   print("%d번 학생 %3d 점 %3s 입니다." % (idx+1, grade[idx], result))