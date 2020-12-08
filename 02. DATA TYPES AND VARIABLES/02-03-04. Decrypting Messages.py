# 02-03. DATA TYPES AND VARIABLES [More Exercises]
# 04. Decrypting Messages

key = int(input())
lines = int(input())

for i in range(lines):
    character = input()
    result = key + ord(character)
    print(chr(result), end='')
