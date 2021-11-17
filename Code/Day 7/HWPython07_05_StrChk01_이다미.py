# 1. Strings
print("Hello")
print('Hello')


# 2. Assign String to a Variable
a = "Hello"
print(a)


# 3. Multiline Strings
# the line breaks are inserted at the same position as in the code
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)


# 4. With three single quotes
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)


# 5. Strings are Arrays
a = "Hello, World!"
print(a[1])  # e


# 6. Looping Through a String
for x in "banana":
  print(x)  # loop through the characters in a string


# 7. String Length
a = "Hello, World!"
print(len(a))  # get the length of a string


# 8. Check String
txt = "The best things in life are free!"
print("free" in txt)  # return True


# 9. Check String in an if statement
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")


# 10. Check if NOT
#Check if "expensive" is NOT present in the following text
txt = "The best things in life are free!"
print("expensive" not in txt)


# Check if NOT in an if statement
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")