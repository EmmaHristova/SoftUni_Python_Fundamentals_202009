# 05-02. LISTS ADVANCED [Exercise]
# 10. Inventory

def collect(item):
    if item not in items:
        items.append(item)


def drop(item):
    if item in items:
        items.remove(item)


def combine(item_old, item_new):
    if item_old in items:
        idx_old = items.index(item_old)
        idx_new = idx_old + 1
        items.insert(idx_new, item_new)


def renew(item):
    if item in items:
        items.remove(item)
        items.append(item)


items = input().split(', ')

while True:
    command = input().split(' - ')
    if command[0] == 'Craft!':
        break
    elif command[0] == 'Collect':
        collect(command[1])
    elif command[0] == 'Drop':
        drop(command[1])
    elif command[0] == 'Combine Items':
        old, new = command[1].split(':')
        combine(old, new)
    elif command[0] == 'Renew':
        renew(command[1])

print(', '.join(items))
