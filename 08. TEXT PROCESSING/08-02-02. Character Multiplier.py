# 08-02. TEXT PROCESSING [Exercise]
# 02. Character Multiplier

string_1, string_2 = input().split(' ')
length_1 = len(string_1)
length_2 = len(string_2)


result = 0

for char_1, char_2 in zip(string_1, string_2):
    result += ord(char_1) * ord(char_2)

if length_1 > length_2:
    for char in string_1[length_2:]:
        result += ord(char)
elif length_2 > length_1:
    for char in string_2[length_1:]:
        result += ord(char)

print(result)
