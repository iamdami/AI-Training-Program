Python
===

1. 창시자: 귀도 반 로섬  
2. 철학과 스타일: PEP(Python Enhancement Proposal)  
3. PEP8 : Style Guide for Python Code https://www.python.org/dev/peps/pep-0008/  
PEP20 : The Zen of Python https://www.python.org/dev/peps/pep-0020/  
  
## Built-in Function
[Built-in Function](https://docs.python.org/3/library/functions.html)  
- 입출력 : print(), input()  
- Data Type : type(), int(), float(), str(),bool(),list(), tuple(), dict(), set()  
- 수학 관련 : min(), max(),abs(), sum(), round(), pow(), divmod()  
- Unicode : chr(), ord()  

## Bool Type의 이해
- True와 False  
  - 1은 True, 0은 False  
  - 존재하는 것은 True, 존재하지 않는 것은 False  
  - 맞으면 True, 틀리면 False  
  
## 변수 : 객체의 이름
Everything is **object** in Python  
  
### 파이썬 이름짓기 방식
1. snake 방식
    - 한 단어마다 _ (underscore)를 붙여 이어나가는 표기법
    - ex) hello_world

2. camel 
    - 첫 문자는 소문자로 표기하고, 그 다음 단어의 첫 시작은 대문자로 표기
    - ex) helloWorld

3. pascal(caps word)
    - 첫 문자를 대문자로 표기하고, 그 다음 단어의 첫 시작도 대문자로 표기 
    - 클래스명은 이 표기법을 권장한다. 단, 이미 만들어져 있는 클래스는 소문자로 시작 
    - ex) HelloWorld
  
### keyword
~~~~
import keyword
print (keyword.kwlist)
print(len(keyword.kwlist))
~~~~
~~~~
['False', 'None', 'True', '__peg_parser__', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

# len(keyword.kwlist)
36
~~~~
  
#### 함수를 값으로, 변수이름으로 사용시 에러뜨는 경우
del 키워드 사용해 네임스페이스에서 삭제하면 다시 사용 가능  
~~~~
sum = 10
sum([1,2,3,4,5])
del sum
sum([1,2,3,4,5])
~~~~
  
## container type
Container (container이면 전부다 iterable하다 즉, 순서대로 하나씩 뽑아 낼 수 있는 데이터 타입)  
  - Homogeneous   ex) ndarray  
  안에 들어가는 자료형이 모두 같은 자료형  
  - Heterogeneous ex) list  
  - sequence      ex) list  
  순서 있는  
  - non sequence  ex) set  
  순서 없는  
  - mutable       ex) list  
  바꿀 수 있는  
  - immutable     ex) tuple  
  바꿀 수 없는  
  
~~~~
list_ex = ["dami", 157, '서울', 'aespa']
tuple_ex = ("dami", 157, '서울', 'aespa')
set_ex = {"dami", 157, '서울', 'aespa'}
dict_ex = {'name':"dami", 'height':157, 'born':"서울", 'favorite':'aespa'}
~~~~

### type 확인
type()  
  
### 인덱싱: 0부터 시작  
~~~~
list_ex[0]  # 'dami'
tuple_ex[0]  # 'dami'
set_ex[0]  # 집합은 중복X, 순서X
dict_ex[0]  # 사전 인덱싱은 key로 함

dict_ex['name']  # 'dami'
~~~~
  
### 슬라이싱: 콜론 앞의 숫자부터 콜론 뒤의 숫자 전까지 / 맨 뒤의 숫자는 -1, 왼쪽으로 -2,-3, -4....
~~~~
list_ex[0:3]  # ['dami', 157, '서울']
len(list_ex)  # 4
~~~~
  
## method
~~~~
# dir()함수로 객체별 사용할 수 있는 함수(메소드) 확인
dir(list) # dir(list_ex)
~~~~
~~~~
['__add__',
 '__class__',
 '__class_getitem__',
 '__contains__',
 '__delattr__',
 '__delitem__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__getitem__',
 '__gt__',
 '__hash__',
 '__iadd__',
 '__imul__',
 '__init__',
 '__init_subclass__',
 '__iter__',
 '__le__',
 '__len__',
 '__lt__',
 '__mul__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__reversed__',
 '__rmul__',
 '__setattr__',
 '__setitem__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 'append',
 'clear',
 'copy',
 'count',
 'extend',
 'index',
 'insert',
 'pop',
 'remove',
 'reverse',
 'sort']  
~~~~
  
~~~~
dir(tuple)
~~~~
~~~~
['__add__',
 '__class__',
 '__class_getitem__',
 '__contains__',
 '__delattr__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__getitem__',
 '__getnewargs__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__iter__',
 '__le__',
 '__len__',
 '__lt__',
 '__mul__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__rmul__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 'count',
 'index']
~~~~
  
### 리스트 메소드 실습
~~~~
favorite = [] #빈 리스트를 만들 수 있다. 

# append()로 순서대로 추가하기 
favorite.append("손흥민")
favorite.append("우지호")
favorite.append("최석배")
favorite.append("담담")

print(favorite)  # ['손흥민', '우지호', '최석배', '담담']
~~~~
~~~~
# remove()로 "최석배"를 제거
favorite.remove("최석배")

print(favorite)  # ['손흥민', '우지호', '담담']
~~~~
  
~~~~
# insert()로 인덱스 2 자리에 "블루파프리카"를 추가
favorite[2] = "블루파프리카"

print(favorite)  # ['손흥민', '우지호', '블루파프리카']
~~~~
  
~~~~
favorite.insert(2,"버나드박")

print(favorite)  # ['손흥민', '우지호', '버나드박', '블루파프리카']
~~~~
    
### 응용
- 문장 수정  
  - s1 = "수없는 씨박"  
~~~~
s1 = "수없는 씨박"
s1.replace("수", "씨")  # '씨없는 씨박'

s1 = "수없는 씨박"
s1 = list(s1)
s1[0], s1[4] = s1[4], s1[0]

print(s1)  # ['씨', '없', '는', ' ', '수', '박']
s1 = "".join(s1)
print(s1)  # 씨없는 수박
~~~~
  
### for 반복문

- `for 임시변수 in (iterable한 객체) : `   
    - `반복할 실행문`

  
~~~~
# 리스트와 반복문
blackpink = ["제니", "지수", "로제", "리사"]
for member in blackpink :
    print(member)
"""
제니
지수
로제
리사
"""
~~~~
  
~~~~
#문자열과 반복문
blackpink = 'Black Pink'
for i in blackpink:
    print(i.upper(), end='')
# 대문자로 바꿔서 줄바꿈 없이 출력
# BLACK PINK
~~~~ 
  
~~~~
#딕셔너리와 반복문
for i in dict_ex:
    print(i, end=' ')  # name height born favorite 
~~~~
  
~~~~
for i in dict_ex:
    print(dict_ex[i], end=' ')  # dami 156.9 서울 aespa
~~~~
  
### 오징어 게임 실습
