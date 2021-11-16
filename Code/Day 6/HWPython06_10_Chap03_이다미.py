"""
a = "Life is too short, you need python"
if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")
"""

"""
n = 1
result = 0
while n <= 1000:
    if n % 3 == 0:
        result += n
    n += 1
print(result)
"""

"""
i = 1
while i <= 5:
    j = 1
    while j <= i:
        print('*', end=" ")
        j += 1
    print()
    i += 1
"""

"""
i=0
for i in range(1, 101):
	print(i, end=" ")
"""

"""
a = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
print(sum(a)/len(a))
"""


n=0
numbers = [1, 2, 3, 4, 5]
result = [n*2 for n in numbers if n % 2 == 1]
print(result)
