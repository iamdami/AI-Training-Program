word = ['winter', 'cold', 'positive', 'negative', 'positive']

x=word.count('positive')

count={}
for i in word:
    try: count[i] += 1
    except: count[i]=1

for key in count:
	print(key,'단어의 갯수 : ', count[key])