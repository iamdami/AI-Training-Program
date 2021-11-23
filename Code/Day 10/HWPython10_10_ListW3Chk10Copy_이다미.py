list1 = ["apple", "banana", "cherry"]
list2 = ["apple", "banana", "cherry"] 
# 주소 값 다름
print(id(list1))
print(id(list2))

print("="*15)

list3 = list1  
# 주소 값 같음
print(id(list1))
print(id(list3))

print("="*15)

# copy()
list4 = list1.copy()  
# 주소 값 다름
print(id(list1))
print(id(list4))

print("="*15)

list5 = list(["apple", "banana", "cherry"])
list6 = list(["apple", "banana", "cherry"])  
# 주소 값 다름
print(id(list5))
print(id(list6))