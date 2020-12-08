# 01-03. BASIC SYNTAX, CONDITIONAL STATEMENTS AND LOOPS [More Exercises]
# 04. Sum Of A Beach

string = input()
string_lower = string.lower()
keywords = ['sand', 'water', 'fish', 'sun']
count = 0

for keyword in keywords:
    count += string_lower.count(keyword)

print(count)
