# 03-02. LISTS BASICS [Exercise]
# 04. Number Beggars

numbers = list(input().split(','))
beggars = int(input())

beggars_sum = []
for i in range(beggars):
    beggars_sum.append(0)

while len(numbers) > 0:
    for j in range(beggars):
        if len(numbers) == 0:
            break
        beggars_sum[j] = beggars_sum[j] + int(numbers[0])
        numbers.pop(0)

print(beggars_sum)
