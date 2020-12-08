# 03-02. LISTS BASICS [Exercise]
# 07. Easter Gifts

gifts = list(input().split(' '))

while True:
    command = input()
    if command == "No Money":
        break
    else:
        command_ele = command.split(' ')
        if command_ele[0] == 'OutOfStock':
            for i in range(len(gifts)):
                if gifts[i] == command_ele[1]:
                    gifts[i] = 'None'
        elif command_ele[0] == 'Required':
            if 0 <= int(command_ele[2]) < len(gifts):
                gifts[int(command_ele[2])] = command_ele[1]
        elif command_ele[0] == 'JustInCase':
            gifts[-1] = command_ele[1]

for gift in gifts:
    if not gift == 'None':
        print(gift, end=' ')
