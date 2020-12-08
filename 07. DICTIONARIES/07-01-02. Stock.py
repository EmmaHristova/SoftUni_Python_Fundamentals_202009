# 07-01. OBJECTS AND CLASSES [Lab]
# 02. Stock

stock = {}

items = input().split(' ')
for i in range(0, len(items), 2):
    key = items[i]
    value = items[i+1]
    stock[key] = int(value)

search = input().split(' ')
for i in search:
    if i in stock.keys():
        print(f'We have {stock[i]} of {i} left')
    else:
        print(f'Sorry, we don\'t have {i}')
