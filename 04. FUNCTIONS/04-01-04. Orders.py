# 04-01. FUNCTIONS [Lab]
# 04. Orders

def total(product, quantity):
    if product == 'coffee':
        return 1.50 * quantity
    elif product == 'water':
        return 1.00 * quantity
    elif product == 'coke':
        return 1.40 * quantity
    elif product == 'snacks':
        return 2.00 * quantity


order_product = input()
order_quantity = int(input())

print(f'{total(order_product, order_quantity):.2f}')
