import os
import sys
import urllib.request
import json
import requests
import time

client_id = " "
client_secret = " "

n=1

keyword=input("검색어를 입력하세요: ") 
encText = urllib.parse.quote(keyword)

for i in range(1, 3): 

    url = f'https://openapi.naver.com/v1/search/image?query={encText}&start={i}&display=100'
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        response_dict =json.loads(response_body.decode('utf-8'))
        items = response_dict['items']
        for j in range(0, len(items)):
            img_url = items[j]['link']
            print(img_url)
            img_file = requests.get(img_url).content 
            with open (f'./img/{n}.{keyword}.jpg', 'wb') as h:     #img 폴더에 저장   
                h.write(img_file)
                print(n, '번째 사진 다운로드')
                n+=1
                time.sleep(0.5)
    else:
        print("Error Code:" + rescode)
