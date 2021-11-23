# Access List Items

# List items are indexed and you can access them by referring to the index number
# The first item has index 0
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
# banana



# Negative Indexing
# Negative indexing means start from the end
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])



# Range of Indexes
# You can specify a range of indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
# ['cherry', 'orange', 'kiwi']



# Leaving out the start value
# By leaving out the start value, the range will start at the first item
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
# ['apple', 'banana', 'cherry', 'orange']



# By leaving out the end value, the range will go on to the end of the list
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])
# ['cherry', 'orange', 'kiwi', 'melon', 'mango']



# Range of Negative Indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])
# ['cherry', 'orange', 'kiwi', 'melon', 'mango']



# Check if Item Exists
# To determine if a specified item is present in a list use the in keyword
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
 # Yes, 'apple' is in the fruits list