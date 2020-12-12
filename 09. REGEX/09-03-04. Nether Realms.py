# 09-02. REGEX [More Exercises]
# 04. Nether Realms

import re

demons = sorted(re.split('[, ]+', input()))

for demon in demons:
    health = 0
    match = re.findall(r'[^0-9\.\*/\+-]', demon)
    for m in match:
        health += ord(m)

    damage = 0.00
    numbers = re.finditer(r'-?\d+(\.\d+)?', demon)
    operators = re.findall(r'[\*/]', demon)
    for n in numbers:
        damage += float(n.group())
    for o in operators:
        if o == '*':
            damage *= 2
        elif o == '/':
            damage /= 2

    print(f'{demon} - {health} health, {damage:.2f} damage')
