# 05-01. LISTS ADVANCED [Lab]
# 04. Even Numbers

integers = input().split(', ')
integers = list(map(int, integers))

integers_even = []

for i, val in enumerate(integers):
    if val % 2 == 0:
        integers_even.append(i)

print(integers_even)
