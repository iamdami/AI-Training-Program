menu    = ['1. 회원가입', '2. 로그인', '3. 회원목록', '9. 메뉴종료']
itemList = ['ID', 'PWD', 'NAME', 'EMAIL', 'PHONE', 'ADDRESS']
menuChk = ['1','2','3','9']
memList = []

print('='*30,"메뉴선택",'='*30)

for x in range(len(menu)):
	print(menu[x],"\t", end=" ")	

print()

print('='*70)

while True:
	num=int(input('메뉴의 번호를 입력하세요:'))

	if num==1:
		print("1. 회원가입 알고리즘 chk")
	elif num==2:
		print('2. 로그인 알고리즘 chk.')
	elif num==3:
		print('3. 회원목록 알고리즘 chk.')
	elif num==9:
		print('9. 종료합니다.')
		break
	else:
		print('범위 내 숫자를 입력하세요.')