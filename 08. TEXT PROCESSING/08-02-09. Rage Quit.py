# 08-02. TEXT PROCESSING [Exercise]
# 09. Rage Quit

string = input().lower()
rage = ''
multiplier = ''
rage_list = []
multiplier_list = []
message = ''

for char in string:
    if not char.isdigit():
        if multiplier != '':
            multiplier_list.append(multiplier)
            multiplier = ''
        rage += char.upper()
    else:
        if rage != '':
            rage_list.append(rage)
            rage = ''
        multiplier += char

multiplier_list.append(multiplier)
multiplier_list = list(map(int, multiplier_list))

for rage, multiplier in zip(rage_list, multiplier_list):
    message += rage * multiplier

print(f'Unique symbols used: {len(set(message))}')
print(message)
