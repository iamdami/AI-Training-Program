Day 6
===

## Multi for loop
outer for : 시침  
inner for : 분침

Input:  
<pre>
for x in range(1, 4): 
  for y in range(1, 2):
    print(x, y)
</pre>
Output:  
<pre>
1 1
1 2
2 1
2 2
3 1
3 2
</pre>
<br>

## append()
appends x to the end of the sequence (same as s[len(s):len(s)] = [x])  
<pre>
a = [1, 2, 3, 4]
result = []

for num in a:
	result.append(num*3)

print(result)
# [3, 6, 9, 12]
</pre>
<br>

- 표현식 사용 예제  
<pre>
a = [1, 2, 3, 4]
result = [num*3 for num in a]
print(result)
# [3, 6, 9, 12]
</pre>
<br>

+)표현식 안에 계속 추가 가능
<pre>
a = [1, 2, 3, 4]
result = [num*3 for num in a if num%2==0]
print(result)
# [6, 12]
</pre>
<br>

+)구구단 출력
<pre>
result = [f"{inner}X{outer}={inner*outer}" for outer in range(2, 10) for inner in range(2, 10)]
print(result)
</pre>
<br>

