# 03-01. LISTS BASICS [Lab]
# 05. Numbers Filter

lines = int(input())
numbers = []
result = []

for i in range(lines):
    numbers.append(int(input()))

command = input()

if command == 'even':
    for i in numbers:
        if i % 2 == 0 or i == 0:
            result.append(i)
elif command == 'odd':
    for i in numbers:
        if i % 2 == 1:
            result.append(i)
elif command == 'negative':
    for i in numbers:
        if i < 0:
            result.append(i)
elif command == 'positive':
    for i in numbers:
        if i >= 0:
            result.append(i)

print(result)
