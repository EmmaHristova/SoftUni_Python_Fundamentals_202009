# 05-02. LISTS ADVANCED [Exercise]
# 05. Electron Distribution

electrons = int(input())

distribution = []
n = 0

while electrons > 0:
    n += 1
    capacity = 2 * n ** 2
    if capacity <= electrons:
        distribution.append(capacity)
        electrons -= capacity
    else:
        distribution.append(electrons)
        electrons = 0

print(distribution)
