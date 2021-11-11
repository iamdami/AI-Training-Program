money=int(input('돈 얼마있나용:'))
card=eval(input('카드 있나용? :'))

if money >=3000 or card:
	print('택시타세요')
else:
	print('걸어가세요')

print(type(card))
