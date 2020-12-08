# 07-01. OBJECTS AND CLASSES [Lab]
# 04. Odd Occurrences

strings = input().split(' ')
dictionary = {}

for string in strings:
    string_lower = string.lower()
    if string_lower not in dictionary:
        dictionary[string_lower] = 0
    dictionary[string_lower] += 1

for (key, value) in dictionary.items():
    if value % 2 != 0:
        print(key, end=' ')
