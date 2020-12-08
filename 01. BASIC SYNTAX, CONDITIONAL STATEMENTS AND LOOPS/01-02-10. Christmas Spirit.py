# 01-02. BASIC SYNTAX, CONDITIONAL STATEMENTS AND LOOPS [Exercise]
# 10. Christmas Spirit

quantity = int(input())
days_left = int(input())

ornament_set_price = 2
tree_skirt_price = 5
tree_garlands_price = 3
tree_lights_price = 15

christmas_spirit = 0
total_expenses = 0

for i in range(2, days_left+1):

    if i % 11 == 0:
        quantity += 2

    if i % 2 == 0:
        total_expenses += quantity * ornament_set_price
        christmas_spirit += 5
    if i % 3 == 0:
        total_expenses += quantity * tree_skirt_price + quantity * tree_garlands_price
        christmas_spirit += 13
    if i % 5 == 0:
        total_expenses += quantity * tree_lights_price
        christmas_spirit += 17
    if i % 10 == 0:
        christmas_spirit -= 20
        total_expenses += tree_skirt_price + tree_garlands_price + tree_lights_price
        if i == days_left:
            christmas_spirit -= 30
    if i % 15 == 0:
        christmas_spirit += 30

print(f"Total cost: {total_expenses}")
print(f"Total spirit: {christmas_spirit}")
