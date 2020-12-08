# 08-02. TEXT PROCESSING [Exercise]
# 06. Replace Repeating Chars

string = input()
prev_char = ''
result = ''

for char in string:
    if char != prev_char:
        result += char
    prev_char = char

print(result)
