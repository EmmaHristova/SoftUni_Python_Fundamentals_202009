# 01-03. BASIC SYNTAX, CONDITIONAL STATEMENTS AND LOOPS [More Exercises]
# 01. Find The Largest
number = input()

digits = [int(x) for x in number]
digits.sort(reverse=True)

result = ""

for i in range(len(digits)):
    result += str(digits[i])

print(result)
