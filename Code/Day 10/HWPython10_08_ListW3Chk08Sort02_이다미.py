# Case Insensitive Sort
# By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters
# Case sensitive sorting can give an unexpected result
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()

print(thislist)
# ['Kiwi', 'Orange', 'banana', 'cherry']



# case-insensitive sort of the list
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)

print(thislist)
# ['banana', 'cherry', 'Kiwi', 'Orange']



# Reverse Order
# reverse()
# 위치만 뒤바꿔주기
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()

print(thislist) 
# ['cherry', 'Kiwi', 'Orange', 'banana']