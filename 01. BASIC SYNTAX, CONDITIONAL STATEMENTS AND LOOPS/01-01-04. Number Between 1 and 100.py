# 01-01. BASIC SYNTAX, CONDITIONAL STATEMENTS AND LOOPS [Lab]
# 04. Number Between 1 and 100

while True:
    number = float(input())
    if 1 <= number <= 100:
        break

print(f"The number {number} is between 1 and 100")
