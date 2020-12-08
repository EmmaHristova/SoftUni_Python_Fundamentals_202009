# 07-01. OBJECTS AND CLASSES [Lab]
# 03 Statistics

bakery = {}

while True:
    command = input()
    if command == 'statistics':
        break
    key, value = command.split(': ')
    if key in bakery:
        bakery[key] += int(value)
    else:
        bakery[key] = int(value)

print('Products in stock:')
for (key, value) in bakery.items():
    print(f'- {key}: {value}')
print(f'Total Products: {len(bakery.keys())}')
print(f'Total Quantity: {sum(bakery.values())}')
