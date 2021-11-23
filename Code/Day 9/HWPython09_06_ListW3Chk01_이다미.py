# Python Lists
mylist = ["apple", "banana", "cherry"]



# store multiple items in a single variable
# using square brackets
thislist = ["apple", "banana", "cherry"]
print(thislist)
# ['apple', 'banana', 'cherry']



# Allow Duplicates
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
# ['apple', 'banana', 'cherry', 'apple', 'cherry']
#value 중복 가능(index가 내부적으로 지정돼 있기 때문)



# List Length
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
# 3



# List Items - Data Types
# String, int and boolean data types
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
"""
['apple', 'banana', 'cherry']
[1, 5, 7, 9, 3]
[True, False, False]
"""



# A list can contain different data types
list1 = ["abc", 34, True, 40, "male"]
# ['abc', 34, True, 40, 'male']



# type()
# lists are defined as objects with the data type 'list'
mylist = ["apple", "banana", "cherry"]
print(type(mylist))
# <class 'list'>



# The list() Constructor
# Using the list() constructor to make a List
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
# ['apple', 'banana', 'cherry']