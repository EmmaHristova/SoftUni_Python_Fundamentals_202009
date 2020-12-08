# 05-02. LISTS ADVANCED [Exercise]
# 02. Big Numbers Lover

numbers = input().split(' ')
numbers.sort()
numbers.reverse()

for num in numbers:
    print(num, end='')
