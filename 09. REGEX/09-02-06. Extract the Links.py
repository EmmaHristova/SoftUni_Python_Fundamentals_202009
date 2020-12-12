# 09-02. REGEX [Exercise]
# 06. Extract the Links

import re

pattern = r'www\.[A-Za-z0-9-]+(\.[a-z]+)+'

while True:
    string = input()
    if string:
        links = re.finditer(pattern, string)
        for link in links:
            print(link.group())
    else:
        break
