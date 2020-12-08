# 05-02. LISTS ADVANCED [Exercise]
# 04. Office Chairs

rooms = int(input())
chairs_free = 0
sufficient = True

for r in range(1, rooms+1):
    chairs, people = input().split(' ')
    if len(chairs) < int(people):
        sufficient = False
        chairs_needed = int(people) - len(chairs)
        print(f'{chairs_needed} more chairs needed in room {r}')
    else:
        chairs_free += len(chairs) - int(people)

if sufficient:
    print(f'Game On, {chairs_free} free chairs left')
