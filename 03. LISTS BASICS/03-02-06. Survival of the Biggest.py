# 03-02. LISTS BASICS [Exercise]
# 06. Survival of the Biggest

integers = list(input().split(' '))
remove = int(input())

integers = [int(i) for i in integers]

for i in range(remove):
    integers.remove(min(integers))

print(integers)
