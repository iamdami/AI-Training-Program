# Sort Lists

# Sort List Alphanumerically
# List objects have a sort() method that will sort the list alphanumerically, ascending, by default
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()

print(thislist)
# ['banana', 'kiwi', 'mango', 'orange', 'pineapple']



# Sort the list numerically
thislist = [100, 50, 65, 82, 23]
thislist.sort()

print(thislist)
# [23, 50, 65, 82, 100]



# Sort Descending
# To sort descending, use the keyword argument reverse = True
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)

print(thislist)
# ['pineapple', 'orange', 'mango', 'kiwi', 'banana']



# Sort the list descending
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)

print(thislist)
# [100, 82, 65, 50, 23]



# Customize Sort Function
# using the keyword argument key = function
# Sort the list based on how close the number is to 50
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
"""
01.
100 - 50 = 50
50 - 50 = 0
65 - 50 = 15
82 - 50 = 32
23 - 50 = 27
"""
thislist.sort(key = myfunc)
"""
02.
[0, 15, 27, 32, 50]
"""
print(thislist)
# [50, 65, 23, 82, 100]