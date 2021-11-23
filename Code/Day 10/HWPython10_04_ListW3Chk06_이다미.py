# Loop Lists

# Loop Through a List
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
"""
apple
banana
cherry
"""



# Loop Through the Index Numbers
# Use the range() and len() functions to create a suitable iterable
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
"""
apple
 banana
 cherry
"""



# Using a While Loop
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
"""
apple
 banana
 cherry
 """



# Looping Using List Comprehension
# shortest syntax(표현식)
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
"""
apple
 banana
 cherry
"""
# 저장하고 싶으면 변수에 담아 저장해야 함



# --------------------------------------------------------------------------------



# List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
# ['apple', 'banana', 'mango']



# With list comprehension you can do all that with only one line of code
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]

print(newlist)
# ['apple', 'banana', 'mango']



# The Syntax
# newlist = [expression for item in iterable if condition == True]



# Only accept items that are not "apple"
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]

print(newlist)
# ['banana', 'cherry', 'kiwi', 'mango']



# With no if statement
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits]

print(newlist)
# ['apple', 'banana', 'cherry', 'kiwi', 'mango']



# Iterable
# use the range() function to create an iterable
newlist = [x for x in range(10)]

print(newlist)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]



# Accept only numbers lower than 5
newlist = [x for x in range(10) if x < 5]

print(newlist)
# [0, 1, 2, 3, 4]



# Expression
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]

print(newlist)
# ['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']



# Set all values in the new list to 'hello'
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = ['hello' for x in fruits]

print(newlist)
# ['hello', 'hello', 'hello', 'hello', 'hello']



# Return the item if it is not banana, if it is banana return orange
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]

print(newlist)
# ['apple', 'orange', 'cherry', 'kiwi', 'mango']