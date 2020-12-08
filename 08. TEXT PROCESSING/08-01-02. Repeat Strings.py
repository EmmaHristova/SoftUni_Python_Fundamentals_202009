# 08-01. TEXT PROCESSING [Lab]
# 02. Repeat Strings

strings = input().split(' ')

for string in strings:
    print(f'{string*len(string)}', end='')
