# 07-02. OBJECTS AND CLASSES [Exercise]
# 05. SoftUni Parking

n = int(input())

parking = {}

for i in range(n):
    command = input().split(' ')
    if command[0] == 'register':
        username = command[1]
        number = command[2]
        if username not in parking:
            parking[username] = number
            print(f'{username} registered {number} successfully')
        else:
            print(f'ERROR: already registered with plate number {number}')
    elif command[0] == 'unregister':
        username = command[1]
        if username not in parking:
            print(f'ERROR: user {username} not found')
        else:
            parking.pop(username)
            print(f'{username} unregistered successfully')

[print(f'{username} => {number}') for (username, number) in parking.items()]
