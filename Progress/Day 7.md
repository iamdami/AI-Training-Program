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
  
  
