# 07-02. OBJECTS AND CLASSES [Exercise]
# 04. Orders

orders = {}

while True:
    command = input()
    if command == 'buy':
        break
    product, price, quantity = command.split(' ')
    if product not in orders:
        orders[product] = [float(price), int(quantity)]
    else:
        orders[product][0] = float(price)
        orders[product][1] += int(quantity)

[print(f'{item} -> {orders[item][0] * orders[item][1]:.2f}') for item in orders]
