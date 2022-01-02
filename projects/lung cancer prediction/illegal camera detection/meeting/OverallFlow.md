Hidden camera detection
===

모바일폰 장치로 불법카메라 있을 만한 곳에서 카메라 탐지
-> bbox 나타나면 촬영 버튼 클릭 -> 사진 저장 -> 사진 업로드(위치 정보 저장)

- input: 촬영된 영상  
- ourput: 촬영된 영상에 카메라 위치 탐지해 bbox 올린 영상  



## To Do  

1.크롤링
  
2.데이터 전처리  
-> 필요없는 데이터 값들에 대해 동그라미 추출해 저장  
  
3. 학습  
**머신러닝 - 지도 - 분류 - 이진분류**  
1) training data / testing data 분리  
2) training data를 training data / validation data로 분리  
3) training data로 모델 만들고 validation data로 검증  
만족시 해당 모델을 [training data + validation data]로 학습 시킨 후 testing data 넣어 확인  
  
### train sets
**Lbl: 0, 1  
no lens(abnormal state) / lens(normal state)**  
#no lens로 학습시킬 영상 -> [lens와 아예 상관없는 영상] + [동물 눈처럼 비슷하게 생긴 영상]으로 구성  
  
### validation data

### testing data
  
  
## 이용할 머신러닝 모델
- Logistic Regression  
- Support Vector Machines  
=> 각 모델 수행 결과 값(정확도) 시각화(plotly)  
정확도 높은 모델 사용  
  
4. 서버 호스팅(netlify 등)  
모바일폰 장치로 촬영 위함  
  
5. 불법카메라 탐지  
  
  
6. 탐지 후 영상에 bbox 생성  
  
7.촬영된 영상에 bbox 올린 영상을 폴더(CamResult)에 저장  
  
8. 촬영된 영상에서 bbox만 자른 사진을 폴더(CamBbox)에 저장  #추후 학습에 사용될 데이터 수집  
  
+) 9. 촬영 위치 저장(추후 불법카메라 위치 신고 기능 구현시 유용)  
