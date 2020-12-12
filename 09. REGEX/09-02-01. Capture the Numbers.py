# 09-02. REGEX [Exercise]
# 01. Capture the Numbers

import re

pattern = r'\d+'

while True:
    string = input()
    if string:
        numbers = re.findall(pattern, string)
        if numbers:
            print(*numbers, end=' ')
    else:
        break
