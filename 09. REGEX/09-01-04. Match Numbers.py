# 09-01. REGEX [Lab]
# 04. Match Numbers

import re

pattern = r'(^|(?<= ))-?\d+(\.\d+)?((?= )|$)'
string = input()

numbers = re.finditer(pattern, string)
for n in numbers:
    print(n.group(), end=' ')
