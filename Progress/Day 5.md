Day 5
===

## 중첩 리스트
<br>

## 문자열 formatting

- 문자열 포맷 코드  
**%s	문자열(String)  
%c	문자 1개(character)  
%d	정수(Integer)  
%f	부동소수(floating-point)**  
%o	8진수  
%x	16진수  
%%	Literal % (문자 % 자체)  
<br>

<pre>
>>> "I have %s apples" % 3
'I have 3 apples'
>>> "rate is %s" % 3.234
'rate is 3.234'
</pre>
<br>

## Format Specification Mini-Language
- curly brace({})  
- str.format()  
- 기호  
'<'	Forces the field to be **left-aligned** within the available space (this is the default for most objects).  
'>'	Forces the field to be **right-aligned** within the available space (this is the default for numbers).  
'='	Forces the padding to be placed after the sign (if any) but before the digits. This is used for printing fields in the form ‘+000000120’. This alignment option is only valid for numeric types.  
'^'	Forces the field to be **centered** within the available space.  
<br>

<pre>
alignLeft="{1:<10}".format("niceday", "hi")  # 왼쪽 정렬  
alignRight="{:>10}".format("niceday")  # 오른쪽 정렬  
alignCenter="{0:^10}".format("niceday")  # 가운데 정렬  

spaceFill01="{0:#^10}".format("hi")  # 빈 공간 #으로 채움  
</pre>
<br>

<pre>
str01 = "My name is {}".format("Dami")
int01 = "{} X {} = {}".format(10, 20, (10*20))
</pre>
<br>

인덱스 값, 변수 값 이용 가능  
<pre>
int01 = "{1} X {0} = {2}".format(10, 20, (10*20))
int02 = "{idx1} X {idx2} = {idx3}".format(idx2=10, idx1=20, idx3=(10*20))
</pre>
<br>

## f 문자열 포매팅
파이썬 3.6 버전부터는 f 문자열 포매팅 기능 사용 가능  
문자열 앞에 f 접두사 붙이면 됨  
{} 안에 변수 들어갈 수 있음  

<pre>
name = '이다미'
age = 25
result=f'내 이름은 {name}입니다. 나이는 {age}입니다.'
</pre>
<br>

딕셔너리는 f 문자열 포매팅에서 다음과 같이 사용  
딕셔너리는 이름과 값이 한 쌍  # 이름에 해당하는 게 변수  

<pre>
d = {'name':'이다미', 'age':25}
result = f'내 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.'
</pre>
<br>

## len()
return the length
<br>

