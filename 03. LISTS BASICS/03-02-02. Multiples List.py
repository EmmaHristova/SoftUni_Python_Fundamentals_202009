# 03-02. LISTS BASICS [Exercise]
# 02. Multiples List

factor = int(input())
count = int(input())

multiples = []

for i in range(1, count+1):
    multiples.append(factor * i)

print(multiples)
