# 08-01. TEXT PROCESSING [Lab]
# 01. Reverse Strings

while True:
    string = input()
    if string == 'end':
        break
    print(f'{string} = {string[::-1]}')
