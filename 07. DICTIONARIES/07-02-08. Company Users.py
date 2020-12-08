# 07-02. OBJECTS AND CLASSES [Exercise]
# 08. Company Users

company_users = {}

while True:
    command = input()
    if command == 'End':
        break
    company, employee = command.split(' -> ')
    if company not in company_users:
        company_users[company] = []
    if employee not in company_users[company]:
        company_users[company].append(employee)

company_users = dict(sorted(company_users.items(), key=lambda x: (x[0])))

for company in company_users:
    print(company)
    for user in company_users[company]:
        print(f'-- {user}')
