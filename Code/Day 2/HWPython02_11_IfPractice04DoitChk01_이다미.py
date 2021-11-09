"""
money = input("돈이 있나요? True or False ").lower().strip()
if money == "true":
	print("택시 타세요")
elif money == "false":
	print("걸어 가세요")
else:
	print("Error")
"""

"""
money = int(input("얼마 있나요? ").lower().strip())
if money >= 3000:
	print("택시 타세요")
else:
	print("걸어 가세요")
"""

money = int(input("얼마 있나요? ").lower().strip())
card =  input("카드가 있나요? True or False ").lower().strip()
if money >= 3000 or card == "true":
	print("택시 타세요")
else:
	print("걸어 가세요")