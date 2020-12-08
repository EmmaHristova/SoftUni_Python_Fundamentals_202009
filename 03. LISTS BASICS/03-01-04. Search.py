# 03-01. LISTS BASICS [Lab]
# 04. Search

lines = int(input())
keyword = input()
list_words = []

for i in range(lines):
    list_words.append(input())

print(list_words)

for string in reversed(list_words):
    if keyword not in string:
        list_words.remove(string)

print(list_words)
