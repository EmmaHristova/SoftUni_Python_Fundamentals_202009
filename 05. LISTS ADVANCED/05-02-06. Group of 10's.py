# 05-02. LISTS ADVANCED [Exercise]
# 06. Group of 10's

numbers = input().split(', ')
numbers = list(map(int, numbers))

bound = 0

while sum(numbers) > 0:
    bound += 10
    group = []
    for i, num in enumerate(numbers):
        if 0 < num <= bound:
            group.append(num)
            numbers[i] = 0
    print(f'Group of {bound}\'s: {group}')
