# Set
"""
-store multiple items in a single variable
-unordered, unchangeable*, and unindexed
-Duplicates Not Allowed
-Set items are unchangeable, but can remove items and add new items
-curly brackets { }
"""

thisset = {"apple", "banana", "cherry"}
print(thisset)


# Get the Length of a Set
thisset = {"apple", "banana", "cherry"}
print(len(thisset))


# Set Items - Data Types
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
print(set1)
print(set2)
print(set3)


# A set with strings, integers and boolean values
set1 = {"abc", 34, True, 40, "male"}
print(set1)


# type()
# <class 'set'>
myset = {"apple", "banana", "cherry"}
print(type(myset))


# The set() Constructor
# Using the set() constructor to make a set
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)