# 01-02. BASIC SYNTAX, CONDITIONAL STATEMENTS AND LOOPS [Exercise]
# 07. Maximum Multiple

# version 1
divisor = int(input())
bound = int(input())

for n in range(bound, divisor+1, -1):
    if n % divisor == 0:
        print(n)
        break

# version 2
divisor = int(input())
bound = int(input())

print(bound // divisor * divisor)
