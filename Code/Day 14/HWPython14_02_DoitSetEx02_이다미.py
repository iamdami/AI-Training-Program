s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])


# intersection
print(s1 & s2)
print(s1.intersection(s2))  
# using intersection()
# == s2.intersection(s1)


# union
print(s1 | s2)
print(s1.union(s2))
# == s2.union(s1)


# difference
print(s1 - s2)
print(s1.difference(s2))
print(s2.difference(s1))