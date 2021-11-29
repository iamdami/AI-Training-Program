"""
Tuple
1. round brackets
2. store multiple items in a single variable
3. unchangeable
4. ordered, allow duplicate values
"""

thistuple1 = ("apple", "banana", "cherry")
print(thistuple1)


# Allow Duplicates
thistuple2 = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple2)


# Tuple Length
thistuple3 = ("apple", "banana", "cherry")
print(len(thistuple3))


# Create Tuple With One Item
thistuple4 = ("apple",)
print(type(thistuple4))

# you have to add a comma after the item, otherwise Python will not recognize it as a tuple
thistuple5 = ("apple")  # NOT a tuple
print(type(thistuple5))


# Tuple Items - Data Types
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
print(tuple1, tuple2, tuple3)


# A tuple can contain different data types
tuple4 = ("abc", 34, True, 40, "male")
print(tuple4)


# The tuple() Constructor
thistuple6 = tuple(("apple", "banana", "cherry")) 
# note the double round-brackets(inner-tuple, outer-method())
print(thistuple6)