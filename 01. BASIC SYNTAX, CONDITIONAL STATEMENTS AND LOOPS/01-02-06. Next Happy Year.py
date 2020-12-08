# 01-02. BASIC SYNTAX, CONDITIONAL STATEMENTS AND LOOPS [Exercise]
# 06. Next Happy Year

year = int(input())

while True:
    year += 1
    if len(set(str(year))) == len(str(year)):
        print(year)
        break
