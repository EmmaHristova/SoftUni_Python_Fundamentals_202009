# 02-03. DATA TYPES AND VARIABLES [More Exercises]
# 03. Prime Number Checker

num = int(input())

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print("False")
            break
    else:
        print("True")
else:
    print("False")
