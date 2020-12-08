# 05-01. LISTS ADVANCED [Lab]
# 02. ToDo List

todo_list = []

while True:
    command = input()
    if command == 'End':
        break
    importance, task = command.split('-')
    todo_list.append([int(importance), task])

todo_list.sort()

tasks = []

for i in todo_list:
    tasks.append(i[1])

print(tasks)
