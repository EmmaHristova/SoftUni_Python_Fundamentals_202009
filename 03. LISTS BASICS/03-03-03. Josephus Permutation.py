# 03-03. LISTS BASICS [More Exercises]
# 03. Josephus Permutation

circle = input().split(' ')
circle = [int(i) for i in circle]

k = int(input())
kill_prev = 0
killed = []

while len(circle) > 0:
    kill = (kill_prev + k-1) % len(circle)
    killed.append(circle[kill])
    circle.pop(kill)
    kill_prev = kill

print(repr(killed).replace(" ", ""))
