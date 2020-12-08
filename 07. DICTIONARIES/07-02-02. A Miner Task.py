# 07-02. OBJECTS AND CLASSES [Exercise]
# 02. A Miner Task

miner = {}

while True:
    command = input()
    if command == 'stop':
        break
    resource = command
    quantity = int(input())
    if resource not in miner:
        miner[resource] = 0
    miner[resource] += quantity

[print(f'{resource} -> {quantity}') for (resource, quantity) in miner.items()]
