# 03-02. LISTS BASICS [Exercise]
# 09. Hello, France

items = input().split('|')
budget = int(input())
income = 0
profit = 0

for item in items:
    item_type, item_price = item.split('->')
    item_price = float(item_price)
    if item_type == 'Clothes' and item_price > 50.00:
        continue
    elif item_type == 'Shoes' and item_price > 35.00:
        continue
    elif item_type == 'Accessories' and item_price > 20.50:
        continue
    if item_price <= budget:
        budget -= item_price
        income += item_price * 1.40
        profit += item_price * 0.40
        print(f'{item_price * 1.40:.2f}', end=' ')

print()
print(f'Profit: {profit:.2f}')

if income + budget >= 150:
    print('Hello, France!')
else:
    print('Time to go.')
