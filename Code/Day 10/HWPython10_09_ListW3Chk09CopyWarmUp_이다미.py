# Copy Lists

"""
cannot copy a list simply by typing list2 = list1,
because: list2 will only be a reference to list1, 
and changes made in list1 will automatically also be made in list2
"""

# call by value

list1 = [1, 2, 3]
list2 = [1, 2, 3]

print(list1)
print(list2)

list1[2] = "Three"

print(list1)
print(list2)

print("="*10)

# call by reference

list3 = [4, 5, 6]
list4 = [7, 8, 9]

print(list3)
print(list4)

list3 = list4

print(list3)
print(list4)