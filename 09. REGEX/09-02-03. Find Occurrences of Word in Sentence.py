# 09-02. REGEX [Exercise]
# 03. Find Occurrences of Word in Sentence

import re

sentence = input()
word = input()

matches = re.findall(f'\\b{word}\\b', sentence, re.IGNORECASE)
print(len(matches))
