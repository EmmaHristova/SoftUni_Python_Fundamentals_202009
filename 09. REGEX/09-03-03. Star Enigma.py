# 09-02. REGEX [More Exercises]
# 03. Star Enigma

import re

pattern = r'@(?P<planet>[A-Za-z]+)[^@!:>-]*:(?P<population>\d+)[^@!:>-]*!(?P<type>[DA])![^@!:>-]*->(?P<soldiers>\d+)'

num = int(input())
planets_attacked = []
planets_destroyed = []

for n in range(num):
    encrypted = input()
    decrypted = ''

    count = len(re.findall('[star]', encrypted, re.IGNORECASE))

    for char in encrypted:
        decrypted += chr(ord(char) - count)

    match = re.finditer(pattern, decrypted)
    for m in match:
        obj = m.groupdict()
        if obj['type'] == 'A':
            planets_attacked.append(obj['planet'])
        elif obj['type'] == 'D':
            planets_destroyed.append(obj['planet'])

print(f'Attacked planets: {len(planets_attacked)}')
for a in sorted(planets_attacked):
    print(f'-> {a}')

print(f'Destroyed planets: {len(planets_destroyed)}')
for d in sorted(planets_destroyed):
    print(f'-> {d}')
