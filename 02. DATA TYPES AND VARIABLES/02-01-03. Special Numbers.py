# 02-01. DATA TYPES AND VARIABLES [Lab]
# 03. Special Numbers

# version 1
number = int(input())

for n in range(1, number + 1):
    string = str(n)
    sum = 0
    for i in range(len(string)):
        sum += int(string[i])
    if sum in (5, 7, 11):
        print(f"{n} -> True")
    else:
        print(f"{n} -> False")

# version 2
number = int(input())

for n in range(1, number + 1):
    digits = str(n)
    sum = 0
    for d in digits:
        sum += int(d)
    if sum in (5, 7, 11):
        print(f"{n} -> True")
    else:
        print(f"{n} -> False")
