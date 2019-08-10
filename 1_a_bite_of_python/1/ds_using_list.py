# this is my shopping list
shoplist = ['apple', 'mango', 'carrot', 'banana']

print(f'I have {len(shoplist)} items to purchase')

print('These items are: ', end=' ')

for item in shoplist:
    print(item, end='')

print('I also have to buy rice')
shoplist.append('rice')
print(f'My shopping list is now: {shoplist}')

print('I will sort my list now')
shoplist.sort()
print(f'My shopping list is now: {shoplist}')

print(f'The first item I will buy is {shoplist[0]}')
olditem = shoplist[0]
del shoplist[0]
print(f'I bought the {olditem}')
print(f'My shopping list is now: {shoplist}')