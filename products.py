products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	p = [name, price]
	products.append(p) 
print(products) #二維清單

products[0][0]


for p in products:
	print(p[0], '的價格是', p[1])