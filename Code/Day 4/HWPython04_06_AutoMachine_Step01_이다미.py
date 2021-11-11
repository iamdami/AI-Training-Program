while True:
	print('*'*6,'과일 판매머신 V01', '*'*6)
	print('1. 오렌지   :  1000원')
	print('2. 딸  기   :  2500원')
	print('3. 복숭아   :  1500원')
	print('4. 망  고   :  2000원')
	print('5. 포  도   :  2000원')
	print('6. 종료')
	print('='*50)
	num=int(input('구매번호를 입력하세요 (1~6): '))

	if num==1:
		print("오렌지는 1000원입니다.")
	elif num==2:
		print('딸기는 2500원입니다.')
	elif num==3:
		print('복숭아는 1500원입니다.')
	elif num==4:
		print('망고는 2000원입니다.')
	elif num==5:
		print('포도는 2000원입니다.')
	elif num==6:
		print('종료')
		break
	else:
		print('범위 내 숫자를 입력하세요.')
		