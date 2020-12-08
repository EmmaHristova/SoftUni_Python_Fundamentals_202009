# 03-03. LISTS BASICS [More Exercises]
# 02. Tic-Tac-Toe

line1 = input().split(' ')
line2 = input().split(' ')
line3 = input().split(' ')

winner = 0

if line1[0] == line1[1] == line1[2] and line1[0] in ('1', '2'):
    winner = line1[0]
elif line2[0] == line2[1] == line2[2] and line2[0] in ('1', '2'):
    winner = line2[0]
elif line3[0] == line3[1] == line3[2] and line3[0] in ('1', '2'):
    winner = line3[0]
elif line1[0] == line2[0] == line3[0] and line1[0] in ('1', '2'):
    winner = line1[0]
elif line1[1] == line2[1] == line3[1] and line1[1] in ('1', '2'):
    winner = line1[1]
elif line1[2] == line2[2] == line3[2] and line1[2] in ('1', '2'):
    winner = line1[2]
elif line1[0] == line2[1] == line3[2] and line1[0] in ('1', '2'):
    winner = line1[0]
elif line1[2] == line2[1] == line3[0] and line1[2] in ('1', '2'):
    winner = line1[2]

if winner == 1:
    print('First player won')
elif winner == 2:
    print('Second player won')
else:
    print('Draw!')
