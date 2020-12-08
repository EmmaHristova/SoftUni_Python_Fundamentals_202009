# 05-02. LISTS ADVANCED [Exercise]
# 08. Moving Target

def shoot(idx, power):
    if 0 <= idx < len(targets):
        targets[idx] = targets[idx] - power
        if targets[idx] <= 0:
            targets.pop(idx)


def add(idx, value):
    if 0 <= idx < len(targets):
        targets.insert(idx, value)
    else:
        print('Invalid placement!')


def strike(idx, radius):
    lower_idx = idx - radius
    upper_idx = idx + radius
    if 0 <= lower_idx < len(targets) and 0 <= upper_idx < len(targets):
        del targets[lower_idx:upper_idx+1]
    else:
        print('Strike missed!')


targets = input().split(' ')
targets = list(map(int, targets))

while True:
    command = input(). split(' ')

    if command[0] == 'Shoot':
        shoot(int(command[1]), int(command[2]))
    if command[0] == 'Add':
        add(int(command[1]), int(command[2]))
    if command[0] == 'Strike':
        strike(int(command[1]), int(command[2]))

    if command[0] == 'End':
        break

targets = list(map(str, targets))
print('|'.join(targets))
