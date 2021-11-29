Day 13
===
  
## 리스트(List) 정리
- 리스트명 = [요소1, 요소2, 요소3, ...]  
  
-비어있는 리스트는 a=list()로 생성할 수도 있음  
<pre>
a = []
b = [1, 2, 3]
c = ['Life', 'is', 'too', 'short']
d = [1, 2, 'Life', 'is']
e = [1, 2, ['Life', 'is']]
print(a)
print(b)
print(c)
print(d)
print(e)
"""
[]
[1, 2, 3]
['Life', 'is', 'too', 'short']
[1, 2, 'Life', 'is']
[1, 2, ['Life', 'is']]
"""
</pre>
  
-리스트 인덱싱, 슬라이싱  
<pre>
a = [1, 2, 3]
print(a[0])  # 1
print(a[0]+a[2])  # 4
print(a[-1])  # 3
</pre>  
  
<pre>
a = [1, 2, 3, ['a', 'b', 'c']]
print(a[0])
print(a[-1])
print(a[3])
print('-'*15)
"""
1
['a', 'b', 'c']
['a', 'b', 'c']
"""

print(a[-1][0])
print(a[-1][1])
"""
a
b
"""
</pre>
  
-삼중리스트 인덱싱  
<pre>
a =[1, 2, ['a', 'b', ['Life', 'is']]]
print(a[2][2][0])  # Life
</pre>
  
-리스트 슬라이싱  
<pre>
a = [1, 2, 3, 4, 5]
print(a[0:2])
print(a[:2])
print(a[2:])
"""
[1, 2]
[1, 2]
[3, 4, 5]
"""
</pre>
  
-중첩된 리스트에서 슬라이싱  
<pre>
a = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
print(a[2:5])
print(a[3][:2])
"""
[3, ['a', 'b', 'c'], 4]
['a', 'b']
"""
</pre>
  
-리스트 연산  
<pre>
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)  # [1, 2, 3, 4, 5, 6]
</pre>
  
-리스트 반복  
<pre>
a = [1, 2, 3]
b = [4, 5, 6]
print(a*3) # [1, 2, 3, 1, 2, 3, 1, 2, 3]
</pre>
  
-리스트 길이  
<pre>
print(len(a))  # 3
print(str(a[2]) + "hi")  # 3hi
</pre>
  
-리스트 수정  
<pre>
a = [1, 2, 3]
a[2] = 4
print(a)  # [1, 2, 4]
</pre>
  
-del 함수 사용해 리스트 요소 삭제  
<pre>
a = [1, 2, 3]
del a[1]
print(a)  # [1, 3]
</pre>
  
<pre>
a = [1, 2, 3, 4, 5]
del a[2:]
print(a)  # [1, 2]
</pre>
  
-리스트 요소 추가  
<pre>
# append(x): 리스트 맨 마지막에 x 추가
a = [1, 2, 3]
a.append(4)
print(a)  # [1, 2, 3, 4]
</pre>
  
-리스트 정렬
<pre>
# sort(): 리스트 요소를 순서대로 정렬
a = [1, 4, 3, 2]
a.sort()
print(a)  # [1, 2, 3, 4]
  
# 문자 정렬 - 알파벳 순
a = ['a', 'c', 'b']
a.sort()
print(a)  # ['a', 'b', 'c']
</pre>
  
-리스트 뒤집기  
<pre>
# reverse(): 리스트 역순으로 뒤집어줌
# sort와는 상관 없음 - 정렬 후 뒤집는 게 아니라 현재 리스트를 그대로 거꾸로 뒤집음
a = ['a', 'c', 'b']
a.reverse()
print(a )  #['b', 'c', 'a']
</pre>
  
-위치 반환
<pre>
# index(x): 리스트에 x 값이 있다면 x의 위치 값 돌려줌
a = [1,2,3]
print(a.index(3))  # 2
print(a.index(1))  # 0
</pre>
  
-리스트 요소 삽입  
<pre>
# insert(a, b): 리스트의 a번째 위치에 b 삽입
a = [1, 2, 3]
a.insert(0, 4)
print(a)  # [4, 1, 2, 3]
</pre>
  
-리스트 요소 제거  
<pre>
# remove(x): 리스트에서 첫 번째로 나오는 x 삭제
a = [1, 2, 3, 1, 2, 3]
a.remove(3)
print(a )  # [1, 2, 1, 2, 3]
</pre>
  
-리스트 요소 끄집어내기  
<pre>
# pop(): 리스트의 맨 마지막 요소 돌려주고 그 요소는 삭제
a = [1,2,3]
print(a.pop())  # 3
print(a)  # [1, 2]
</pre>
  
-리스트에 포함된 요소 x의 개수 세기  
<pre>
# count(x): 리스트 안에 x가 몇 개 있는지 조사해 그 개수를 돌려줌
a = [1,2,3,1]
print(a.count(1))  # 2
</pre>
  
-리스트 확장  
<pre>
# extend(x): x에는 리스트만 올 수 있으며 원래의 a 리스트에 x 리스트 더하게 됨
a = [1,2,3]
a.extend([4,5])
print(a)  # [1, 2, 3, 4, 5]

b = [6, 7]
a.extend(b)
print(a)  # [1, 2, 3, 4, 5, 6, 7]
</pre>
  
<br>

## 튜플(Tuple)  

1. round brackets
2. store multiple items in a single variable
3. unchangeable
4. ordered, allow duplicate values
  
**-Allow Duplicates**  
**-Tuple Length**  
**-Create Tuple With One Item**  
you have to add a comma after the item, otherwise Python will not recognize it as a tuple  
**-Tuple Items - Data Types**  
A tuple can contain different data types  
**-The tuple() Constructor**  
note the double round-brackets(inner-tuple, outer-method())  
  
<br>

### Access Tuple Items  

1. index number_ square brackets  
  
**-Negative Indexing**  
Negative indexing means start from the end  
**-Range of Indexes**  
When specifying a range, the return value will be a new tuple with the specified items  
**-By leaving out the start value, the range will start at the first item  
-By leaving out the end value, the range will go on to the end of the list  
-Range of Negative Indexes  
-Check if Item Exists**  
using **in** keyword  
    
<br>

## Update Tuples  

unchangeable, meaning that **you cannot change, add, or remove items once the tuple is created**  
<br>
But there is a workaround  
You can **convert the tuple into a list, change the list, and convert the list back into a tuple**  

-**Change Tuple Values**  
-**Add Items**  
Convert into a list, Add tuple to a tuple  
-You are **allowed to add tuples to tuples**,  
so if you want to add one item, (or many),  
create a new tuple with the item(s),  
and add it to the existing tuple  
-**Remove Items**  
Tuples are unchangeable, so convert the tuple into a list, remove "apple", and convert it back into a tuple  
-**del keyword can delete the tuple completely**  
  
<br>

## Unpack Tuples  

-**Packing a tuple**  
<pre>
fruits = ("apple", "banana", "cherry")
print(fruits)
</pre>
-**Unpacking a tuple**  
<pre>
fruits1 = ("apple", "banana", "cherry")
(green, yellow, red) = fruits1

print(green)
print(yellow)
print(red)
</pre>
-**Using Asterisk**  
If the number of variables is less than the number of values,  
you can add an * to the variable name and the values will be assigned to the variable as a list  
<br>
If the asterisk is added to another variable name than the last,  
Python will assign values to the variable until the number of values left matches the number of variables left  
  
<br>

## Loop Tuples  

-**Loop Through a Tuple**  
Iterate through the items and print the values  
-**Loop Through the Index Numbers**  
You can also loop through the tuple items by referring to their index number  
Use the range() and len() functions  
-Using a While Loop  
Print all items, using a while loop to go through all the index numbers  
  
<br>

## Join Tuples  

-**Join Two Tuples(+)**  
-**Multiply Tuples(*)**  
  
<br>

## Tuple Methods  

- **count()**: Returns the number of times a specified value occurs in a tuple  
- **index()**: Searches the tuple for a specified value and returns the position of where it was found  
