Day 8
===

## 모듈
-함수나 변수 클래스를 모아놓은 파일  
-많은 모듈을 사용하게 됨  
-이미 만들어 놓은 모듈을 사용할 수도 있고, 직접 만들어 사용할 수도 있음  
모듈 불러오기: mport 모듈이름  
  
## open()
**open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)**  
**'r'**  
open for reading (default)  
**'w'**  
open for writing, truncating the file first  
'x'  
open for exclusive creation, failing if the file already exists  
**'a'**  
open for writing, appending to the end of the file if it exist  
'b'  
binary mode  
't'  
text mode (default)  
'+'  
open a disk file for updating (reading and writing)  
'U'  
universal newlines mode (deprecated)  
  
## 경로: 절대경로/상대경로  
1.절대경로 : 디스크명:\폴더명\파일명  
2.상대경로 : 현재위치 기준 - '.' : 현재경로  
                                 -'..' : 상위경로  
  
<pre>
**절대경로 이용**
C:\Windows\test>cd C:\Windows\System
C:\Windows\System>

**상대경로 이용**
C:\Windows\test>cd ./../system
C:\Windows\System>
</pre>
   
- **csv**(쉼표로 구분된 값)  
스프레드시트와 데이터베이스에 관한 가장 일반적인 가져오기/내보내기 형식  
확장자 csv.py  
  
- csv.reader(csvfile)  
주어진 csv파일을 줄 단위로 반복할 리더오브젝트 반환  
  
  
## split()
