Day 11
===

## Selection Sort
-정렬하려는 배열의 요소들을 하나씩 선택해 비교 연산 이용해 가장 작은 값의 요소 찾아내 정렬  
-계속해서 최소값을 찾아 제자리에 정렬해 줌  
<pre>
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
</pre>
  
## Practice with StuData
  

