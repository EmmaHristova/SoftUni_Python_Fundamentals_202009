# 07-03. OBJECTS AND CLASSES [More Exercises]
# 02. Judge

contests = {}
usernames = {}

while True:
    command = input()
    if command == 'no more time':
        break

    username, contest, points = command.split(' -> ')
    if contest not in contests:
        contests[contest] = {}
    if username not in contests[contest]:
        contests[contest][username] = int(points)
    elif int(points) > contests[contest][username]:
        contests[contest][username] = int(points)

for contest in contests:
    contests[contest] = dict(sorted(contests[contest].items(), key=lambda x: (-x[1], x[0])))

for contest in contests:
    for username, points in contests[contest].items():
        if username not in usernames:
            usernames[username] = 0
        usernames[username] += points

usernames = dict(sorted(usernames.items(), key=lambda x: (-x[1], x[0])))

for contest in contests:
    print(f'{contest}: {len(contests[contest])} participants')
    rank = 0
    for username, points in contests[contest].items():
        rank += 1
        print(f'{rank}. {username} <::> {points}')

print('Individual standings:')
rank = 0
for username, points in usernames.items():
    rank += 1
    print(f'{rank}. {username} -> {points}')
