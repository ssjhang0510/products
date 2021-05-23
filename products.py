import os #operating system

#讀取檔案
products = []
if os.path.isfile('products.csv'): #檢查檔案在不在
	print('找到檔案了') 
	with open('products.csv', 'r') as f:
		for line in f:
			if '商品,價格' in line:
				continue #繼續
			name, price = line.strip().split(',')
			products.append([name, price]) #split 切割完的結果是清單
	print(products)

else:
	print('找不到檔案...')

#讓使用者輸入
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

#印出所有購買紀錄
for p in products:
	print(p[0], '的價格是', p[1])

#寫入檔案
with open('products.csv', 'w') as f: #utf-8是最通用的編碼
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')