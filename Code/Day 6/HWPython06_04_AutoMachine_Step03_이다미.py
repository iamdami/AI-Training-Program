i=0
num=0

fruit = ["orange", "strawberry", "peach", "mango", "grape"]
price = ["1000원", "2500원", "1500원", "2000원", "2000원"]

print('*'*6,'과일 판매머신 V01', '*'*6)

for i in range(len(fruit)):
	print("%d . %s  :  %s" % (i+1, fruit[i], price[i]))
print((len(fruit)+1), ".", "종료")
print('='*35)

num=int(input("번호를 입력하세요 (1~6): "))
if num < len(fruit) :
	print("%s는 %s입니다." % (fruit[num-1], price[num-1]))
else:
	pass
if num == 6:
	print("종료합니다")