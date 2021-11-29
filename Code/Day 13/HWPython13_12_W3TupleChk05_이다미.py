# Loop Tuples

# Loop Through a Tuple
# Iterate through the items and print the values
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)


# Loop Through the Index Numbers
# You can also loop through the tuple items by referring to their index number
# Use the range() and len() functions
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])
 

# Using a While Loop
# Print all items, using a while loop to go through all the index numbers
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1



# Join Tuples
# Join Two Tuples(+)
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)


# Multiply Tuples(*)
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)



# Tuple Methods
# count(): Returns the number of times a specified value occurs in a tuple
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5)

print(x)

# index(): Searches the tuple for a specified value and returns the position of where it was found
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(8)

print(x)
