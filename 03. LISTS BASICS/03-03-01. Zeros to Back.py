# 03-03. LISTS BASICS [More Exercises]
# 01. Zeros to Back
integers = input().split(',')
integers = [int(i) for i in integers]

count = integers.count(0)

while 0 in integers:
    integers.remove(0)

for i in range(count):
    integers.append(0)

print(integers)
