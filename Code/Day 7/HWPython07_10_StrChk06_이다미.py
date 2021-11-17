a = "Life is too short, You need Python"
b = a[0] + a[1] + a[2] + a[3]  # a[0] = L, a[1] = i, a[2] = f, a[3] = e
print(b)


a[0:4]  # a[0:4] = Life
a[0:2], a[5:7], a[12:17]  # a[0:2] = Li, a[5:7] = is, a[12:17] = short
a[19:]  # a[19:] = You need Python
a[:5]  # a[:5] = Life 
a[:]  # a[:] = Life is too short, You need Python
a[19:-7]  # a[19:-7] = You need

print(a[0:4])
print(a[0:2], a[5:7], a[12:17])
print(a[19:])
print(a[:5])
print(a[:])
print(a[19:-7])
