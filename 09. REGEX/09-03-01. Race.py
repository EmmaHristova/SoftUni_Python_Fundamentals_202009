# 09-03. REGEX [More Exercises]
# 01. Race

import re

participants = input().split(', ')
race = {}
for p in participants:
    race[p] = 0

while True:
    string = input()
    if string == 'end of race':
        break

    name = ''
    letters = re.findall('[A-Za-z]', string)
    for l in letters:
        name += l

    distance = 0
    digits = re.findall('\\d', string)
    for d in digits:
        distance += int(d)

    if name in race:
        race[name] += distance

race = dict(sorted(race.items(), key=lambda x: -x[1]))
top_3 = [p for p in list(race)[:3]]

print(f'1st place: {top_3[0]}')
print(f'2nd place: {top_3[1]}')
print(f'3rd place: {top_3[2]}')
