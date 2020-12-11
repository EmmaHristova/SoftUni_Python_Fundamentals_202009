# 09-01. REGEX [Lab]
# 01. Match Full Name

import re

pattern = r'\b[A-Z][a-z]+ [A-Z][a-z]+\b'
string = input()

names = re.findall(pattern, string)
print(' '.join(names))
