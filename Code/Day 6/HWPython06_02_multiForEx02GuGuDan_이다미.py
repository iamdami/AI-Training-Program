i=0
j=0

print("="*100)
for dan in range(2, 10): 
	print(dan, "단", end="         ")
print("\n")
print("="*100)

for i in range(2, 10):
	for j in range(2, 10):
		print("{} X {} = {}".format(j, i, (j*i)), end="  ")
	print("\n")