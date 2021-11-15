str01 = "My name is {}".format("Dami")
int01 = "{1} X {0} = {2}".format(10, 20, (10*20))

print(str01)
print(int01)

str02 = "My name is {}".format("Dami")
int02 = "{idx1} X {idx2} = {idx3}".format(idx2=10, idx1=20, idx3=(10*20))

print(str02)
print(int02)