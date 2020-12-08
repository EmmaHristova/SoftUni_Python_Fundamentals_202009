# 05-02. LISTS ADVANCED [Exercise]
# 01. Which Are In?

list1 = input().split(', ')
list2 = input().split(', ')

substring = []

for i in list1:
    for j in list2:
        if i in j:
            if not i in substring:
                substring.append(i)

print(substring)
