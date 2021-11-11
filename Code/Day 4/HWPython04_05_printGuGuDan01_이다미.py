result = int(input('확인하고자 하는 단 수를 입력하세요: '))
print('='*20)
print(result, '단')
print('='*20)

i = result
j = 1
while i>0 and j>0:
	print(i, 'x', j, '=', (i*j))
	if(j==9):
		break

	j+=1