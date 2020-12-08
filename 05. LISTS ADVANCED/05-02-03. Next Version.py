# 05-02. LISTS ADVANCED [Exercise]
# 03. Next Version

version = input().split('.')
version = list(map(int, version))

if version[2] < 9:
    version[2] += 1
else:
    version[2] = 0
    if version[1] < 9:
        version[1] += 1
    else:
        version[1] = 0
        version[0] += 1

for i, val in enumerate(version):
    if i < len(version) - 1:
        print(val, end='.')
    else:
        print(val)
