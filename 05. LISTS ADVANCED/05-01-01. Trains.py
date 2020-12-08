# 05-01. LISTS ADVANCED [Lab]
# 01. Trains

train = []

wagons = int(input())
for i in range(wagons):
    train.append(0)

while True:
    command = input().split(' ')
    if command[0] == 'add':
        train[-1] = train[-1] + int(command[1])
    if command[0] == 'insert':
        train[int(command[1])] = train[int(command[1])] + int(command[2])
    if command[0] == 'leave':
        train[int(command[1])] = train[int(command[1])] - int(command[2])
    if command[0] == 'End':
        break

print(train)
