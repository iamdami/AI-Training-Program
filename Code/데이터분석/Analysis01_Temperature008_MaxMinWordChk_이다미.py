word = ['winter', 'cold', 'positive', 'negative', 'positive']

wordSet = list(set(word))

print(word)

count={}
for i in word:
    try: count[i] += 1
    except: count[i]=1

vMax = -9999999999999

vMin = 999999999999

for idx in wordSet:
	if vMax < len(idx):
		vMax = len(idx)
		maxWord = idx
print('가장 긴 글자 수는'+ maxWord +str(vMax))

for idx in wordSet:
	if vMin > len(idx):
		vMin = len(idx)
		minWord = idx
print('가장 짧은 수는'+ minWord +str(vMin))
