money = int(input("금액을 입력하세요: "))
card = bool(input("카드 있나요? True/False: "))

print(type(card))
print(card)

if money >= 3000 or card:
	print("택시 타세요")
else:
	print("걸어가세요")