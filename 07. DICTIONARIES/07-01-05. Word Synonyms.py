# 07-01. OBJECTS AND CLASSES [Lab]
# 05. Word Synonyms

n = int(input())

synonyms = {}

for i in range(n):
    word = input()
    synonym = input()
    if word not in synonyms:
        synonyms[word] = []
    synonyms[word].append(synonym)

[print(f'{word} - {", ".join(synonym)}') for (word, synonym) in synonyms.items()]
