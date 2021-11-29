"""
import random
x = 0
i = 0
stuName = (input("4인 이상의 이름을 입력하세요.: (종료:0)"))
sp_stuName = list(len(stuName)).split(" ")

if sp_stuName >= 4 :
	print("%d 명 Chk" % sp_stuName)
	for i in range(sp_stuName):
		while True:
			x = random.randint(1, sp_stuName)
			list(x)
			random.shuffle(x)
			print(x)
			break
			
elif stuName < 4 :
	print("4인 이상 명수를 확인하세요.")

"""

import random

stuName = (input("4인 이상의 이름을 입력하세요.: (종료:0)").split(" "))


if len(stuName) >= 4 :
	print("%d 명 Chk" % len(stuName))
	for i in range(len(stuName)):
		while True:
			print(random.randint(1, len(stuName)))
			break
elif stuName < 4 :
	print("4인 이상 명수를 확인하세요.")




# print(random.shuffle(randLen))



"""
import random

stuName = (input("4인 이상의 이름을 입력하세요.: (종료:0)").split(" "))


if len(stuName) >= 4 :
	print("%d 명 Chk" % len(stuName))
	for i in range(len(stuName)):
		while True:
			randLen = random.randint(1, len(stuName))
			list_randLen = list(randLen)
			random.shuffle(list_randLen)
			print(list_randLen)
			break
elif stuName < 4 :
	print("4인 이상 명수를 확인하세요.")

"""
"""
stuName = (input("4인 이상의 이름을 입력하세요.: (종료:0)").split(" "))
random.shuffle(stuName)
print(stuName)
"""