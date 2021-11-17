# Slicing
# start index and the end index, separated by a colon, to return a part of the string
# Get the characters from position 2 to position 5 (not included)
# The first character has index 0
b = "Hello, World!"
print(b[2:5])  # llo


# Slice From the Start
# By leaving out the start index, the range will start at the first character
b = "Hello, World!"
print(b[:5])  # Hello


# Slice To the End
# By leaving out the end index, the range will go to the end
b = "Hello, World!"
print(b[2:])  # llo, World!


# Negative Indexing
# start the slice from the end of the string
b = "Hello, World!"
print(b[-5:-2])  # orl