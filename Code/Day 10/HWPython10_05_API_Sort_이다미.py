## sort: 정렬

01. 오름차순  
-한글: ㄱ ~ ㅎ
-영문: A ~ Z  
-숫자: 작 ~ 큰  
  
02. 내림차순
-한글: ㅎ ~ ㄱ  
-영문: Z ~ A    
-숫자: 큰 ~ 작  
  
sort(*, key=None, reverse=False)

key specifies a function of one argument that is used to extract a comparison key from each list element (for example, key=str.lower)  
reverse is a boolean value. If set to True, then the list elements are sorted as if each comparison were reversed