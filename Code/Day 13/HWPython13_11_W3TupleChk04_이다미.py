# Unpack Tuples

# Packing a tuple
fruits = ("apple", "banana", "cherry")
print(fruits)


# Unpacking a tuple
fruits1 = ("apple", "banana", "cherry")

(green, yellow, red) = fruits1

print(green)
print(yellow)
print(red)


# Using Asterisk
"""
If the number of variables is less than the number of values,
you can add an * to the variable name and the values will be assigned to the variable as a list
"""
fruits2 = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green1, yellow1, *red1) = fruits2

print(green1)
print(yellow1)
print(red1)


"""
If the asterisk is added to another variable name than the last, 
Python will assign values to the variable until the number of values left matches the number of variables left
"""
fruits3 = ("apple", "mango", "papaya", "pineapple", "cherry")

(green2, *tropic2, red2) = fruits3

print(green2)
print(tropic2)
print(red2)