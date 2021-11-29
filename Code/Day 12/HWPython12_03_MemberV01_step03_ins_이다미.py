menu    = ['1. 회원가입', '2. 로그인', '3. 회원목록', '9. 메뉴종료']
itemList = ['ID', 'PWD', 'NAME', 'EMAIL', 'PHONE', 'ADDRESS']
menuChk = ['1','2','3','9']
userList=[]
temp=[]
i=0
j=0

print('='*30,"메뉴선택",'='*30)

for i in range(len(menu)):
	print(menu[i],"\t", end=" ")	

print()

print('='*70)

for i in range(len(menu)):
	num=int(input('메뉴의 번호를 입력하세요: '))

	if num==1:
		print("^SignUp !")
		
		for i in range(len(itemList)) :
			print(f'\t{itemList[i]:<10}:',end=" ")
			temp.append(input())
		userList.append(temp)
		temp=[]
		#print(userList)
		for i in range(len(userList)):
			print(' '.join(userList[i]), end=" \n")
		print("현재 회원 수는 %d명 입니다." % len(userList))

	elif num==2:
		print('2. 로그인 알고리즘 chk.')

	elif num==3:
		if len(userList) == 0 :
			print("회원가입을 해주세요.")
		else:
			print("^Member List !")
			print()
			print('='*70)

			for j in range(len(itemList)):
				print(itemList[j], end="\t")
			
			for i in range(len(userList)):
				print('\t'.join(userList[i]), end=" \n")

			print('='*70)
		
	elif num==9:
		print('9. 종료합니다.')
		break

	else:
		print('범위 내 숫자를 입력하세요.')

	print()
