### 함수
- 특정 작업을 수행하는 명령문의 그룹
- 프로그램의 기능 단위로 모듈을 구성하는데 사용됨
- 프로그램이 복잡해지고 커질 때 함수를 사용하면 체계적이고 관리도 쉬워짐
- 코드의 **반복을 피할 수 있고, 코드의 재사용**이 가능
- 용어
    - argument : 인수, 함수에 전달하는 객체, 실체(instance, object)
    - parameter : 매개변수, 인수를 가리킬 이름 (인수를 저장할 변수)
    - return : 반환

- 함수 정의
- `def 함수이름(매개변수): `
    - `실행문`    
    - `return`  

~~~~
# 매개변수도 return도 없는 함수
def iam():
  print("I am dami")
  print("I major CS")
~~~~
  
### Class

- 클래스란 객체(존재하는 모든 것)가 가져야할 정보를 담은 코드
- 클래스는 속성(변수)과 메서드(함수)로 구성
  
### 모듈, 패키지
- 모듈 : 파이썬 파일(.py)
- 패키지 : 모듈을 모아 놓은 폴더/디렉토리 * 라이브러리와 비슷한 의미
- import하는 방법

   - `import 모듈이름`
   - `import 모듈이름 as 모듈닉네임` 
   - `from 모듈이름 import 클래스, 함수 등`
   - ` from 모듈이름 import * `
   - `import 패키지이름.모듈이름 as 모듈닉네임`
   - `from 패키지이름 import 모듈이름 as 모듈닉네임`
   - `from 패키지이름.모듈이름 import 클래스, 함수 등`
  
[파이썬 표준 라이브러리](https://docs.python.org/ko/3/library/index.html)  
  
### 경로 구분자 (Windows와 Linux)
- \ (```\```) : Windows 에서 역슬래시를 경로 구분에 사용함
- / : Linux, Colab에서 슬래시를 경로 구분자에 사용
- Python에서는 \ (```\```), / 모두 사용 가능하며, \ (```\```)의 경우 ```\\```와 같이 사용함
  - Windows 예시: `'C:\\Users\\Jay\\Downloads\\파일입출력.ipynb'` 또는 `r'C:\Users\Jay\Downloads\파일입출력.ipynb'`
  - Linux(Colab) 예시 : `'/content/drive/MyDrive/test.txt'`
  
### 절대 경로와 상대 경로
  - 절대 경로 : 리눅스인 경우 '/' 부터, Windows인 경우 'C:/'와 같은 드라이브 이름부터 시작하는 경로
  - 상대 경로 : 현재 디렉터리를 기준으로 상위, 하위 디렉터리를 이동하며 표현되는 경로
    - . : 현재 디렉터리
    - .. : 상위 디렉터리
    - 이름 : 하위 디렉터리

  
