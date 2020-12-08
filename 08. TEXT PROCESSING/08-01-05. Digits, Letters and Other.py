# 08-01. TEXT PROCESSING [Lab]
# 05. Digits, Letters and Other

string = input()
digits = ''
letters = ''
symbols = ''

for char in string:
    if char.isdigit():
        digits += char
    elif char.isalpha():
        letters += char
    else:
        symbols += char

print(digits)
print(letters)
print(symbols)
