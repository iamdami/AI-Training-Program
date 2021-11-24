a = [75,65,100,80,90,55,95,30,20,50]
i=0
print("Before Sort: ", a)
for i in range(i, len(a)-1):
	minIdx=i
	
	for j in range(i+1, len(a)):
		if a[minIdx] > a[j]:
			minIdx = j
	a[i], a[minIdx] = a[minIdx], a[i]

print("After Sort: ", a)