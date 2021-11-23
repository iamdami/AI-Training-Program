Day 10
===

## Change List Items
-Change Item Value  
-Change a Range of Item Values  
-Change the second value by replacing it with two new values  
-Change the second and third value by replacing it with one value  
-Insert Items  
To insert a new list item, without replacing any of the existing values  
  
## Add List Items  
-Append Items
-Insert Items  
-Extend List  
-Add Any Iterable  
you can add any iterable object (lists, tuples, sets, dictionaries etc.)  
  
## Remove List Items
-Remove Specified Item  
-Remove Specified Index  
-If you do not specify the index, the pop() method removes the last item  
-del  
-del keyword can also delete the list completely  
-Clear the List  
  
## Loop Lists
-Loop Through a List  
-Loop Through the Index Numbers  
Use the range() and len() functions to create a suitable iterable  
-Using a While Loop  
-Looping Using List Comprehension  
shortest syntax(표현식)  
저장하고 싶으면 변수에 담아 저장해야 함  
  
## List Comprehension
-With list comprehension you can do all that with only one line of code  
- The Syntax
<pre>
newlist = [expression for item in iterable if condition == True]
</pre>
  
-Only accept items that are not "apple"(ex)  
-With no if statement  
-Iterable  
use the range() function to create an iterable  
-Expression: upper()  
  
## sort: 정렬
01. 오름차순  
-한글: ㄱ ~ ㅎ
-영문: A ~ Z  
-숫자: 작 ~ 큰  
  
02. 내림차순
-한글: ㅎ ~ ㄱ  
-영문: Z ~ A    
-숫자: 큰 ~ 작  
  
<pre>sort(*, key=None, reverse=False)</pre>
**key** specifies a function of one argument that is used to extract a comparison key from each list element  
(for example, key=str.lower)  
**reverse** is a boolean value.  
If set to True, then the list elements are sorted as if each comparison were reversed  
  
## ASCII(American Standard Code for Information Interchange)
![ASCII](https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/ASCII-Table-wide.svg/800px-ASCII-Table-wide.svg.png)  
-숫자 0은 아스키코드 값으로 48  
-대문자 A는 65, 소문자 a는 97 -> 32 차이  
  
## 사용자 정의 함수  
변수: 값 저장하는 공간, 변하는 수  
변수가 함수() 안에 들어가면 매개변수  
매개변수: 함수 호출할 때 값 할당  
  
## Case Insensitive Sort
By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters  
Case sensitive sorting can give an unexpected result  
  
-case-insensitive sort of the list  
  
## Reverse Order
reverse()  
위치만 뒤바꿔주기  
  
## Copy Lists
cannot copy a list simply by typing list2 = list1,  
because: list2 will only be a reference to list1,  
and changes made in list1 will automatically also be made in list2  
  
- call by value  
<pre>
list1 = [1, 2, 3]
list2 = [1, 2, 3]

print(list1)
print(list2)

list1[2] = "Three"

print(list1)
print(list2)

print("="*10)
</pre>
<br>

- call by reference  
<pre>
list3 = [4, 5, 6]
list4 = [7, 8, 9]

print(list3)
print(list4)

list3 = list4

print(list3)
print(list4)
</pre>
<br>
  
## Join in Lists
-using the **+** operator  
-**Append** list2 into list1  
-Use the **extend()** to add list2 at the end of list1  
  
## index()
index 값 반환  
  
## temp 변수 이용한 값 저장
  
