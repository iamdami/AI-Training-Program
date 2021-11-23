fruits = ["apple", "banana", "cherry", "cherry", "cherry"]
returnCnt = fruits.count("cherry")
sum = 0
i = 0

for i in fruits:
	if i == "cherry":
		sum += 1

print(sum)

print(returnCnt)

"""
while i<len(fruits):
	if  fruits[i] == "cherry":
		sum += 1
	i+=1
print(sum)
"""