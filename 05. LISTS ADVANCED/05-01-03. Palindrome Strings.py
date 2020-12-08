# 05-01. LISTS ADVANCED [Lab]
# 03. Palindrome Strings

words = input().split(' ')
searched = input()

palindromes = []
count_searched = 0

for word in words:
    if word == ''.join(reversed(word)):
        palindromes.append(word)
    if word == searched:
        count_searched += 1

print(palindromes)
print(f'Found palindrome {count_searched} times')
