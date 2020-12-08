# 07-02. OBJECTS AND CLASSES [Exercise]
# 06. Courses

courses = {}

while True:
    command = input()
    if command == 'end':
        break
    course, student = command.split(' : ')
    if course not in courses:
        courses[course] = []
    courses[course].append(student)

courses = dict(sorted(courses.items(), key=lambda x: (len(x[1])), reverse=True))

for course in courses:
    print(f'{course}: {len(courses[course])}')
    courses[course] = sorted(courses[course])
    for student in courses[course]:
        print(f'-- {student}')
