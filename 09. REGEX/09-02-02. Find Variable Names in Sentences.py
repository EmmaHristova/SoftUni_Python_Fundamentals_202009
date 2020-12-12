# 09-02. REGEX [Exercise]
# 02. Find Variable Names in Sentences

import re

pattern = r'((?<=^_)|(?<=\s_))([A-Z|a-z|0-9]+)\b'
string = input()

variables = [var.group() for var in re.finditer(pattern, string)]
print(','.join(variables))
