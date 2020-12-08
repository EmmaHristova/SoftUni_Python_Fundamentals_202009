# 07-02. OBJECTS AND CLASSES [Exercise]
# 01. Count Chars in a String

string = input()

occurrences = {}

for char in string:
    if char is not ' ':
        if char not in occurrences:
            occurrences[char] = 0
        occurrences[char] += 1

[print(f'{char} -> {occurrences[char]}') for char in occurrences]
