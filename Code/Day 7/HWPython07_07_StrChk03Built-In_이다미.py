# Modify Strings

# Upper Case
a = "Hello, World!"
print(a.upper())  # HELLO, WORLD!


# Lower Case
a = "Hello, World!"
print(a.lower())  # hello, world!


# Remove Whitespace
# removes any whitespace from the beginning or the end
a = " Hello, World! "
print(f'WooSong{a}WooSong')
print(f'WooSong{a.strip()}WooSong') 


# Replace String
# replaces a string with another string
a = "Hello, World!"
print(a.replace("H", "J"))  # Jello, World!


# Split String
# returns a list where the text between the specified separator becomes the list items
a = "Hello, World!"
b = a.split(",")
print(type(b))  # list
print(b)  # ['Hello', ' World!']