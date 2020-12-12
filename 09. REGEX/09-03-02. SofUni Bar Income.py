# 09-03. REGEX [More Exercises]
# 02. SoftUni Bar Income

import re

pattern = r'%(?P<name>[A-Z][a-z]+)%[^%\|\.\$]*<(?P<product>\w+)>[^%\|\.\$]*\|(?P<count>\d+)\|[^%\|\.\$]*(?P<price>(?<=\D)\d+(\.\d+)?)\$'

total_income = 0.00

while True:
    string = input()
    if string == 'end of shift':
        break
    match = re.match(pattern, string)
    if match:
        order = match.groupdict()
        income = float(order['price']) * int(order['count'])
        total_income += income
        print(f"{order['name']}: {order['product']} - {income:.2f}")

print(f'Total income: {total_income:.2f}')
