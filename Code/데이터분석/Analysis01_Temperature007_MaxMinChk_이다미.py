vList = ['100', '90', '80', '30', '95', '20']

vMax = -9999999999999

vMin = 999999999999

for idx in vList:
	if vMax < int(idx):
		vMax = int(idx)
print('가장 큰 수는'+str(vMax))

for idx in vList:
	if vMin > int(idx):
		vMin = int(idx)
print('가장 작은 수는'+str(vMin))
