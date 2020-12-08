# 02-02. DATA TYPES AND VARIABLES [Exercise]
# 05. Print Part of the ASCII Table

ascii_dec_start = int(input())
ascii_dec_end = int(input())

for ascii_dec in range(ascii_dec_start, ascii_dec_end + 1):
    print(chr(ascii_dec), end=' ')
