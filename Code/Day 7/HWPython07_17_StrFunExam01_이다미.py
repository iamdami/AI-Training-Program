strEx = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=server"

urlHttps = strEx.split('?', 1)[0]
urlWhere = strEx.split('?', 1)[1]
print("URL: ", urlHttps)
print()

print("Query String")
splitUrl = urlWhere.split('&')

for i in splitUrl:
	print(f'{i}')
print()

print(len(splitUrl))