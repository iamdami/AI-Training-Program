# Remove List Items

# remove
# Remove Specified Item
# has no return value
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
# ['apple', 'cherry']



#pop
# Remove Specified Index
# has return value
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
# ['apple', 'cherry']



# If you do not specify the index, the pop() method removes the last item
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
# ['apple', 'banana']



# del
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)



# del keyword can also delete the list completely
thislist = ["apple", "banana", "cherry"]
del thislist
print(thislist) 
# this will cause an error because you have succsesfully deleted "thislist"
# 구조 자체를 지웠기 때문!



# Clear the List
#The clear() method empties the list
#The list still remains, but it has no content
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
# []