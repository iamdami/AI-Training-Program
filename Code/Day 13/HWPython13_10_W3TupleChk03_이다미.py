"""
Update Tuples  
unchangeable, meaning that you cannot change, add, or remove items once the tuple is created

But there is a workaround  
You can convert the tuple into a list, change the list, and convert the list back into a tuple
"""

# Change Tuple Values
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)


# Add Items
# Convert into a list, Add tuple to a tuple
thistuple = ("apple", "banana", "cherry")
y1 = list(thistuple)
y1.append("orange")
thistuple = tuple(y1)
print(thistuple)


# You are allowed to add tuples to tuples, 
# so if you want to add one item, (or many), create a new tuple with the item(s), and add it to the existing tuple
thistuple1 = ("apple", "banana", "cherry")
y2 = ("orange",)
thistuple1 += y2
print(thistuple1)


# Remove Items
# Tuples are unchangeable, so convert the tuple into a list, remove "apple", and convert it back into a tuple
thistuple2 = ("apple", "banana", "cherry")
y3 = list(thistuple2)
y3.remove("apple")
thistuple2 = tuple(y3)
print(thistuple2)


# del keyword can delete the tuple completely
thistuple4 = ("apple", "banana", "cherry")
del thistuple4
print(thistuple4) 
#this will raise an error because the tuple no longer exists