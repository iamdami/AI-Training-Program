"""
Access Tuple Items
1. index number_ square brackets
"""

thistuple1 = ("apple", "banana", "cherry")
print(thistuple1[1])


# Negative Indexing
# Negative indexing means start from the end
thistuple2 = ("apple", "banana", "cherry")
print(thistuple2[-1])


# Range of Indexes
# When specifying a range, the return value will be a new tuple with the specified items
thistuple3 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple3[2:5])


# By leaving out the start value, the range will start at the first item
thistuple4 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple4[:4])


# By leaving out the end value, the range will go on to the end of the list
thistuple5 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple5[2:])


# Range of Negative Indexes
thistuple6 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple6[-4:-1])


# Check if Item Exists
# in keyword
thistuple7 = ("apple", "banana", "cherry")
if "apple" in thistuple7:
  print("Yes, 'apple' is in the fruits tuple")