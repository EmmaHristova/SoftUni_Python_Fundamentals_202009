# 03-02. LISTS BASICS [Exercise]
# 03. Football Cards

team_A = []
team_B = []

for i in range(1, 11+1):
    team_A.append(f"A-{i}")
    team_B.append(f"B-{i}")

cards = list(input().split(' '))

for i in cards:
    if i in team_A:
        team_A.remove(i)
    if i in team_B:
        team_B.remove(i)
    if len(team_A) < 7 or len(team_B) < 7:
        break

print(f'Team A - {len(team_A)}; Team B - {len(team_B)}')

if len(team_A) < 7 or len(team_B) < 7:
    print('Game was terminated')
