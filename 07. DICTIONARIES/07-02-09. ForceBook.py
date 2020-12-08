# 07-02. OBJECTS AND CLASSES [Exercise]
# 09. ForceBook

forcebook = {}

while True:
    command = input()
    if command == 'Lumpawaroo':
        break
    if ' | ' in command:
        side, user = command.split(' | ')
        all_users = []
        for users in forcebook.values():
            all_users += users
        if user not in all_users:
            if side not in forcebook:
                forcebook[side] = []
            forcebook[side].append(user)
    elif ' -> ' in command:
        user, side = command.split(' -> ')
        if side not in forcebook:
            forcebook[side] = []
        for key in forcebook:
            if user in forcebook[key]:
                forcebook[key].remove(user)
        forcebook[side].append(user)
        print(f'{user} joins the {side} side!')

forcebook = dict(sorted(forcebook.items(), key=lambda x: (-len(x[1]), x[0])))

for side in forcebook:
    if len(forcebook[side]) == 0:
        continue
    print(f'Side: {side}, Members: {len(forcebook[side])}')
    for user in sorted(forcebook[side]):
        print(f'! {user}')
