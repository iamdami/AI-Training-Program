# 리스트 요소 추가
# append(x): 리스트 맨 마지막에 x 추가
a = [1, 2, 3]
a.append(4)
print(a)  # [1, 2, 3, 4]
print('-'*15)


# 리스트 정렬
# sort(): 리스트 요소를 순서대로 정렬
a = [1, 4, 3, 2]
a.sort()
print(a)  # [1, 2, 3, 4]

# 문자 정렬 - 알파벳 순
a = ['a', 'c', 'b']
a.sort()
print(a)  # ['a', 'b', 'c']
print('-'*15)


# 리스트 뒤집기
# reverse(): 리스트 역순으로 뒤집어줌
# sort와는 상관 없음 - 정렬 후 뒤집는 게 아니라 현재 리스트를 그대로 거꾸로 뒤집음
a = ['a', 'c', 'b']
a.reverse()
print(a )  #['b', 'c', 'a']
print('-'*15)


# 위치 반환
# index(x): 리스트에 x 값이 있다면 x의 위치 값 돌려줌
a = [1,2,3]
print(a.index(3))  # 2
print(a.index(1))  # 0
print('-'*15)


# 리스트 요소 삽입
# insert(a, b): 리스트의 a번째 위치에 b 삽입
a = [1, 2, 3]
a.insert(0, 4)
print(a)  # [4, 1, 2, 3]
print('-'*15)


# 리스트 요소 제거
# remove(x): 리스트에서 첫 번째로 나오는 x 삭제
a = [1, 2, 3, 1, 2, 3]
a.remove(3)
print(a )  # [1, 2, 1, 2, 3]
print('-'*15)


# 리스트 요소 끄집어내기
# pop(): 리스트의 맨 마지막 요소 돌려주고 그 요소는 삭제
a = [1,2,3]
print(a.pop())  # 3
print(a)  # [1, 2]
print('-'*15)


# 리스트에 포함된 요소 x의 개수 세기
# count(x): 리스트 안에 x가 몇 개 있는지 조사해 그 개수를 돌려줌
a = [1,2,3,1]
print(a.count(1))  # 2
print('-'*15)


# 리스트 확장
# extend(x): x에는 리스트만 올 수 있으며 원래의 a 리스트에 x 리스트 더하게 됨
a = [1,2,3]
a.extend([4,5])
print(a)  # [1, 2, 3, 4, 5]

b = [6, 7]
a.extend(b)
print(a)  # [1, 2, 3, 4, 5, 6, 7]