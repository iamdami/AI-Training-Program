# Access Set Items
"""
cannot access items in a set by referring to an index or a key
But can loop through the set items using a for loop,
or ask if a specified value is present in a set, by using the in keyword
"""

# Loop through the set, and print the values
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)


# Check if "banana" is present in the set
thisset1 = {"apple", "banana", "cherry"}
print("banana" in thisset1)  # true or false


# Change Items
# Once a set is created, cannot change its items, but can add new items


# Add Set Items
# add() method
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")

print(thisset)


# Add Sets
# update() method
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)

print(thisset)


# Add Any Iterable
# Add elements of a list to at set
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)

print(thisset)


# Remove Set Items
# use the remove(), or the discard() method
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
# If the item to remove does not exist, remove() will raise an error

print(thisset)


# Remove "banana" by using the discard()
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
# If the item to remove does not exist, discard() will NOT raise an error

print(thisset)


"""
pop() method to remove an item, but this method will remove the last item
sets are unordered, so you will not know what item that gets removed
The return value of the pop() method is the removed item
"""

# Remove the last item by using the pop()
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()

print(x)
print(thisset)


# clear() method empties the set
thisset = {"apple", "banana", "cherry"}
thisset.clear()

print(thisset)


# del keyword will delete the set completely
thisset = {"apple", "banana", "cherry"}
del thisset

print(thisset)