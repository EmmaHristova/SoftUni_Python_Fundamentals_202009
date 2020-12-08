# 03-02. LISTS BASICS [Exercise]
# 05. Faro Shuffle

string = list(input().split(' '))
shuffles = int(input())

half = int(len(string) / 2)

for i in range(shuffles):
    string1 = string[0:half]
    string2 = string[half:]
    string = []
    for j in range(half):
        string.extend([string1[j], string2[j]])

print(string)
