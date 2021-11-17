Day 7
===

## 진법 변환

10진수: 0 1 ~ 9  
2진수: 0 1  
8진수: 0 ~ 7  
16진수: 0 ... 9 A B ... F  

ex)  
51  
  
10진수: 10^1*5 + 10^0*1 = 50+1 = 51  
2진수: 2^5*1 2^4*1 2^3*0 2^2*0 2^1*1 2^0*1 = 110011  
8진수: 110/011 => 4+2=6 , 2+1=3 => 63  
16진수: 0011/0011 => 3 , 3 => 33  
  
- 8진수는 0o 또는 0O, 16진수는 0X 또는 0x로 시작하면 됨  
<pre>
a=0o34  # 8*3 + 1*4 = 28
b=0O25  # 8*2 + 1*5 = 21

print(a, b)

c=0x2a  # 16*2 + 1*10
d=0XFF  # 16*15 + 1*15

print(c, d)
</pre>
<br>  
  
## 문자열
1. **Strings**
2. **Assign String to a Variable**
3. **Multiline Strings** - the line breaks are inserted at the same position as in the code
4. **With three single quotes**
5. **Strings are Arrays**
6. **Looping Through a String** - loop through the characters in a string
7. **String Length** - get the length of a string
8. **Check String**
9. **Check String in an if statement**
10. **Check if NOT**
11. **Check if NOT in an if statement**  
<br>
  
## Slicing string
1. **Slicing** - start index and the end index, separated by a colon, to return a part of the string
2. **Slice From the Start** - By leaving out the start index, the range will start at the first character
3. **Slice To the End** - By leaving out the end index, the range will go to the end
4. **Negative Indexing** - start the slice from the end of the string
<br>
  
## Modify Strings
1. **Upper Case**
2. **Lower Case**
3. **Remove Whitespace** - removes any whitespace from the beginning or the end
4. **Replace String** - replaces a string with another string
5. **Split String** -  returns a list where the text between the specified separator becomes the list items  
[Python String Methods](https://www.w3schools.com/python/python_ref_string.asp)  
<br>
  
## String Concatenation
1. **concatenate, or combine, two strings you can use the + operator**
2. **To add a space between them, add a " "**
<br>
  
## Format - Strings
1. **Use the format() method to insert numbers into strings**
2. method takes unlimited number of arguments, and are placed into the respective placeholders
3. **use index numbers**
<br>
  
## Escape Character
1. **use '""'**
2. **use the escape character \"**
<br>
  
**Other escape characters used in Python**    
**\'**	Single Quote  
**\\**	Backslash  
**\n**	New Line  
**\r**	Carriage Return  
**\t**	Tab  
**\b**	Backspace  
**\f**	Form Feed  
**\ooo**	Octal value  
**\xhh**	Hex value  
<br>
  
## 문자열 인덱싱
파이썬은 0부터 카운팅  
a[-1]은 뒤에서부터 세어 첫 번째가 되는 문자  
0과 -0은 똑같은 것이기 때문에 a[-0]은 a[0]과 똑같은 값을 보여줌  
<br>

## 문자열 슬라이싱
a[시작 번호:끝 번호]에서 끝 번호 부분을 생략하면 시작 번호부터 그 문자열의 끝까지 출력
a[시작 번호:끝 번호]에서 시작 번호를 생략하면 문자열의 처음부터 끝 번호까지 출력
a[시작 번호:끝 번호]에서 시작 번호와 끝 번호를 생략하면 문자열의 처음부터 끝까지 출력  
슬라이싱에서도 인덱싱과 마찬가지로 마이너스(-) 기호를 사용 가능  
  
ex)  
"Pithon"이라는 문자열을 "Python"으로 바꾸려면?  
<pre>
a = "Pithon"
a[:1]  # 'P'
a[2:]  # 'thon'
print("use slicing: ", a[:1] + 'y' + a[2:])  # 'Python'
print("original: ", a)  # immutable

a = a[:1] + 'y' + a[2:]  
print("realloc: ", a)  # 'Python'
</pre>
<br>

## Python - String Methods
All string methods returns new values  
They do not change the original string  
[string methods](https://www.w3schools.com/python/python_strings_methods.asp)  
<pre>
a = "hobby"
print(a.count('b'))
print(len(a))

a = "Python is the best choice"
print(a.find('b'))
print(a.find('k'))  # 없으면 '-1' 반환

a = "Life is short"
print(a.index('f'))
print(a.index('k'))  # 없으면 에러 반환
</pre>
<br>
  
## 문자열 삽입 join()
<br>
  
## 공백 지우기 strip()
1. 왼쪽 공백 지우기(lstrip)
2. 오른쪽 공백 지우기(rstrip)
3. 양쪽 공백 지우기(strip)  
<br>
  
## 문자열 바꾸기 replace()
<pre>
a = "Life is too short"
a.replace("Life", "Your leg")
</pre>
<br>

## 문자열 나누기 split()
<pre>
a = "Life is too short"
print("a.split(): ", a.split())
print("type(a): ", type(a))
print("a: ", a)  # Life is too short

b = "a:b:c:d"
print("b.split(':'): ", b.split(':'))
print("type(b): ", type(b))
print("b: ", b)  # a:b:c:d
</pre>
<br>
  
## server와 client
server: 자료 제공  
client: 자료 제공받는 쪽  
  
**server 전송방식: get / post**  
- <GET 방식>  
-입력한 데이터를 URL에 붙여서 전송  
-보안에 취약: 데이터 다 보임  
-전송할 수 있는 데이터는 256바이트 넘을 수 없음  
-전송 속도는 POST 방식보다 빠름  
  
- <post 방식>  
-입력한 데이터를 본문 안에 포함해서 전송  
-입력한 데이터가 URL에 보이지 않으므로 GET방식보다 보안에 우수  
-전송할 데이터의 길이에 제한없음  
-복잡한 형태의 데이터 전송 시 유용함  
  
- URL  
https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=server  
