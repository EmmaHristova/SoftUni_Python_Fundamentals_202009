# 05-01. LISTS ADVANCED [Lab]
# 05. The Office

empl_happiness = input().split(' ')
empl_happiness = list(map(int, empl_happiness))

factor = int(input())

for i, val in enumerate(empl_happiness):
    empl_happiness[i] = val * factor

avg_hapiness = sum(empl_happiness) / len(empl_happiness)

empl_happiest = []

for val in empl_happiness:
    if val >= avg_hapiness:
        empl_happiest.append(val)

idx = len(empl_happiest) / len(empl_happiness)

if idx >= 0.5:
    print(f'Score: {len(empl_happiest)}/{len(empl_happiness)}. Employees are happy!')
else:
    print(f'Score: {len(empl_happiest)}/{len(empl_happiness)}. Employees are not happy!')
