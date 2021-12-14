Day 37
===
<h3>JavaScript</h3>  

- substring  

-요약: 문자열에서 특정한 구간의 문자열 추출  
-문법: **string.substring(from, to)**  
-인자  

|인자명|데이터형|필수/옵션| 설명 |  
|------|---|---|------|  
|from|number|필수|탐색구간의 시작점(index)|  
|to|number|옵션|탐색구간이 끝나는 점, 0 index부터 시작|  
  
-반환값: string, from과 to 사이의 문자열  
-설명  
<pre>
from과 to 모두 index 0부터 시작하는 위치 값 가짐  
from이 to 보다 작으면 from부터 to 사이의 문자열 리턴  
from이 to 보다 크면 to부터 from 사이의 문자열 리턴  
from과 to가 같으면 빈문자열 리턴  
</pre>
  
[Substring](https://opentutorials.org/course/50/98)  
<br>
  
<h3>Algorithm & Data Structure</h3>  

- Binary Search(half-interval search)  
An efficient algorithm for finding an item from a sorted list of items  
데이터가 정렬돼 있는 배열에서 특정한 값 찾아내는 알고리즘  
<pre>
배열의 중간에 있는 임의 값을 선택해 찾고자 하는 값X와 비교  
-> X가 중간 값보다 작으면 중간 값을 기준으로 좌측 데이터들을 대상으로,  
X가 중간 값보다 크면 중간 값을 기준으로 우측 데이터들을 대상으로 다시 탐색  
동일한 방법으로 해당 값을 찾을 때까지 과정 반복  
</pre>
**이진 탐색의 시간 복잡도: O(logN)**  
[Binary Search_wikipedia](https://en.wikipedia.org/wiki/Binary_search_algorithm)  

- KMP Algorithm  
-**문자열 검색?**  
![StringSearchingEX](./../images/StringSearchingEX)  

[KMP Algorithm](https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm)  
<br>
- Boyer-Moore Algorithm  
[Boyer-Moore Algorithm_naver blog](https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=cestlavie_01&logNo=221055516242)  
[Boyer-Moore Algorithm_pdf](http://www.cs.jhu.edu/~langmea/resources/lecture_notes/boyer_moore.pdf)  
<br>
- Sequential Search  
<br>
- String Algorithm  
<br>
