# 07-03. OBJECTS AND CLASSES [More Exercises]
# 01. Ranking

contests = {}
submissions = {}
usernames = {}

while True:
    command = input()
    if command == 'end of contests':
        break
    contest, password = command.split(':')
    contests[contest] = password

while True:
    command = input()
    if command == 'end of submissions':
        break
    contest, password, username, points = command.split('=>')

    if contest in contests and password == contests[contest]:
        if username not in submissions:
            submissions[username] = {}
        if contest not in submissions[username]:
            submissions[username][contest] = int(points)
        elif int(points) > submissions[username][contest]:
            submissions[username][contest] = int(points)

submissions = dict(sorted(submissions.items(), key=lambda x: (x[0])))

for username in submissions:
    submissions[username] = dict(sorted(submissions[username].items(), key=lambda x: (-x[1])))

for username, data in submissions.items():
    for contest, points in submissions[username].items():
        if username not in usernames:
            usernames[username] = 0
        usernames[username] += points

best_username = max(usernames, key=usernames.get)
best_points = max(usernames.values())

print(f'Best candidate is {best_username} with total {best_points} points.')
print('Ranking:')
for username, data in submissions.items():
    print(username)
    for contest, points in submissions[username].items():
        print(f'#  {contest} -> {points}')
