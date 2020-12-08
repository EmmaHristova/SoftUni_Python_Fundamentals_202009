# 07-02. OBJECTS AND CLASSES [Exercise]
# 10. SoftUni Exam Results

results = {}
submissions = {}

while True:
    command = input()
    if command == 'exam finished':
        break

    try:
        username, language, points = command.split('-')
        is_submission_valid = True
    except ValueError:
        username, banned = command.split('-')
        is_submission_valid = False

    if is_submission_valid:
        if username not in results or int(points) > results[username]:
            results[username] = int(points)
        if language not in submissions:
            submissions[language] = 0
        submissions[language] += 1

    else:
        results.pop(username)

results = dict(sorted(results.items(), key=lambda x: (-x[1], x[0])))
submissions = dict(sorted(submissions.items(), key=lambda x: (-x[1], x[0])))

print('Results:')
[print(f'{username} | {points}') for (username, points) in results.items()]

print('Submissions:')
[print(f'{language} - {submissions[language]}') for language in submissions]
