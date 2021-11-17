a = "Pithon"
a[:1]  # 'P'
a[2:]  # 'thon'
print("use slicing: ", a[:1] + 'y' + a[2:])  # 'Python'
print("original: ", a)  # immutable

a = a[:1] + 'y' + a[2:]  
print("realloc: ", a)  # 'Python'