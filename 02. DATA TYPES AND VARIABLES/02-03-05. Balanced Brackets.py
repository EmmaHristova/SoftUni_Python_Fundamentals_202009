# 02-03. DATA TYPES AND VARIABLES [More Exercises]
# 05. Balanced Brackets

lines = int(input())
open_brackets = 0
close_brackets = 0
consecutive = False
prev_char = char = ''

for i in range(lines):
    char = input()
    if char in ("(", ")"):
        if char == "(":
            open_brackets += 1
            if char == prev_char:
                consecutive = True
        if char == ")":
            close_brackets += 1
        prev_char = char

if consecutive or not open_brackets == close_brackets:
    print("UNBALANCED")
else:
    print("BALANCED")
