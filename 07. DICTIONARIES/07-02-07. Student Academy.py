# 07-02. OBJECTS AND CLASSES [Exercise]
# 07. Student Academy

n = int(input())

academy = {}

for i in range(n):
    name = input()
    grade = float(input())
    if name not in academy:
        academy[name] = []
    academy[name].append(grade)

for name in academy:
    academy[name] = sum(academy[name])/len(academy[name])

academy_best = dict((name, grade) for (name, grade) in academy.items() if grade >= 4.5)

academy_best = dict(sorted(academy_best.items(), key=lambda x: (-x[1])))

[print(f'{name} -> {grade:.2f}') for (name, grade) in academy_best.items()]
