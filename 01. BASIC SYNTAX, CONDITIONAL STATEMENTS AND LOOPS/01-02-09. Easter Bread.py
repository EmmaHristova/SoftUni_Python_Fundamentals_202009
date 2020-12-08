# 01-02. BASIC SYNTAX, CONDITIONAL STATEMENTS AND LOOPS [Exercise]
# 09. Easter Bread

budget = float(input())
flour_price = float(input())
eggs_price = flour_price * 0.75
milk_price = flour_price * (1 + 0.25) / 4
easter_cake_price = flour_price + eggs_price + milk_price
easter_cakes = 0
colored_eggs = 0

while budget >= 0:
    if easter_cake_price <= budget:
        easter_cakes += 1
        colored_eggs += 3
        budget -= easter_cake_price
        if easter_cakes % 3 == 0:
            colored_eggs -= (easter_cakes - 2)
    else:
        break

print(f"You made {easter_cakes} cozonacs! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
