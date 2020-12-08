# 01-03. BASIC SYNTAX, CONDITIONAL STATEMENTS AND LOOPS [More Exercises]
# 02. Find The Capitals

string = input()
capital_letters = []

for i in range(len(string)):
   if string[i].isupper():
       capital_letters.append(i)

print(capital_letters)
