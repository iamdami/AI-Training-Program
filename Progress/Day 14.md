Day 14
===

![list tuple set dictionary](https://miro.medium.com/max/510/1*WMiNIQ9THariDSJw47uU1w.png)
  
<br>

## 집합(Set) 자료형
-중복제거  
-교집합, 합집합, 차집합 구하기  
<br>

**-store multiple items in a single variable  
-unordered, unchangeable*, and unindexed  
-Duplicates Not Allowed  
-Set items are unchangeable, but can remove items and add new items  
-curly brackets { }**  

<br>
  
list나 tuple은 순서가 있기 때문에 인덱싱을 통해 자료형의 값을 얻을 수 있지만  
**set은 순서가 없기 때문에 인덱싱으로 값을 얻을 수 없음**  
  
set은 중복을 허용하지 않기 때문에 자료형의 중복을 제거하기 위한 필터 역할로 종종 사용됨 
  
- 교집합(intersection), 합집합(union), 차집합(difference)은 반환값 있음  
  
- 집합 자료형 관련 함수들
-값 1개 추가하기(add)  
-값 여러 개 추가하기(update)  
-특정 값 제거하기(remove)  
remove와 pop의 차이점: 리턴값 유무(pop은 리턴값 있음)  
<br>

-Get the Length of a Set  
-Set Items - Data Types  
-A set with strings, integers and boolean values  
-type(): <class 'set'>  
-The set() Constructor  
  
<br>

- Access Set Items  
cannot access items in a set by referring to an index or a key  
But can loop through the set items using a for loop,  
or ask if a specified value is present in a set, by using the in keyword  
  
- Change Items  
Once a set is created, cannot change its items, but can add new items  
  
- Add Set Items  
-add() method
-update() method  
  
- Remove Set Items  
-use the remove(), or the discard() method  
**If the item to remove does not exist, remove() will raise an error  
but discard() will NOT raise an error**  
  
-Remove the last item by using the **pop()**  
pop() method to remove an item, but this method will remove the last item  
sets are unordered, so you will not know what item that gets removed  
The return value of the pop() method is the removed item  
  
-clear() method empties the set  
  
-del keyword will delete the set completely  
  
- Join Sets  
union() method that returns a new set containing all items from both sets,   
or the update() method that inserts all the items from one set into another  
  
-**union()** method returns a new set with all items from both sets  
-**update()** method inserts the items in set2 into set1  
-**union()** and update() will exclude any duplicate items  
  
-Keep ONLY the Duplicates  
**intersection_update()** method will keep only the items that are present in both sets  
<br>
  
**intersection()** method will return a new set, 
that only contains the items that are present in both sets  
  
-Keep All, But NOT the Duplicates  
**symmetric_difference_update()** method will keep only the elements that are NOT present in both sets  
Keep the items that are not present in both sets  
  
**symmetric_difference()** method will return a new set,  
that contains only the elements that are NOT present in both sets  
  
<br>
  
[Set Methods](https://www.w3schools.com/python/python_sets_methods.asp)  
