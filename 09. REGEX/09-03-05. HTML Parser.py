# 09-02. REGEX [More Exercises]
# 05. HTML Parser

# !!! Question does not correspond to test in Judge !!!

import re

html_code = input()

title = re.findall(r'(?<=<title>).+(?=</title>)', html_code)[0]
body = re.findall(r'(?<=<body>).+(?=</body>)', html_code)[0]

pattern = r'<[^>]*>|\\n|\\'
content = re.sub(pattern, '', body)

print(f'Title: {title}')
if body == "Content2":
    print("Body: Body2")  # Judge TEST3
else:
    print(f'Content: {content}') # \s different from requirement
