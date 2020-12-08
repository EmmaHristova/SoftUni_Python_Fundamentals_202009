# 03-03. LISTS BASICS [More Exercises]
# 04. Battle Ships

ships_down = 0

battle_field = {}
keys = range(int(input()))

for i in keys:
    values = input().split(' ')
    values = [int(i) for i in values]
    battle_field[i] = values

attacks = input().split(' ')

for attack in attacks:
    attack_row, attack_col = attack.split('-')
    attack_row = int(attack_row)
    attack_col = int(attack_col)

    sqr = battle_field[attack_row][attack_col]

    if sqr > 0:
        battle_field[attack_row][attack_col] = sqr - 1
        if battle_field[attack_row][attack_col] == 0:
            ships_down += 1

print(ships_down)
