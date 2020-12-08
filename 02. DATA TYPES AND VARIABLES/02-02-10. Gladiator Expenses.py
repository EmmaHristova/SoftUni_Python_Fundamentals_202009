# 02-02. DATA TYPES AND VARIABLES [Exercise]
# 10. Gladiator Expenses

lost_fights = int(input())
helmet = float(input())
sword = float(input())
shield = float(input())
armor = float(input())
expenses = 0

for f in range(1, lost_fights+1):
    if f % 2 == 0:
        expenses += helmet
    if f % 3 == 0:
        expenses += sword
    if f % 6 == 0:
        expenses += shield
    if f % 12 == 0:
        expenses += armor

print(f"Gladiator expenses: {expenses:.2f} aureus")
