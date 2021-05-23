products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	price = int(price)
	p = [name, price]
	products.append(p) 
print(products) #二維清單

products[0][0]


for p in products:
	print(p[0], '的價格是', p[1])


with open('product.csv', 'w') as f: #utf-8是最通用的編碼
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')