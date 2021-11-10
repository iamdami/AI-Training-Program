money = int(input("얼마 있나요? "))
card =  input("카드가 있나요? True or False ")

if card == "true":
	card == 1
elif card == "false":
	card == 0
else:
	print("error")

if money >= 3000 or card:
	print("택시 타세요")
else:
	print("걸어 가세요")