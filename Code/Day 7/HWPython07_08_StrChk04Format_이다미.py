# String Concatenation

# concatenate, or combine, two strings you can use the + operator
a = "Hello"
b = "World"
c = a + b
print(c)  # HelloWorld


# To add a space between them, add a " "
a = "Hello"
b = "World"
c = a + " " + b
print(c)  # Hello World


# Format - Strings

#String Format
# Use the format() method to insert numbers into strings
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))  # My name is John, and I am 36


# method takes unlimited number of arguments, and are placed into the respective placeholders
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
# I want 3 pieces of item 567 for 49.95 dollars.


# use index numbers
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
# I want to pay 49.95 dollars for 3 pieces of item 567


# Escape Character
txt = 'We are the so-called "Vikings" from the north.'
print(txt)


# use the escape character \"
txt = "We are the so-called \"Vikings\" from the north."