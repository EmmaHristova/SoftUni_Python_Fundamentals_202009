# 08-04. TEXT PROCESSING [More Exercises]
# 05. HTML

title = input()
content = input()
comments = []

while True:
    line = input()
    if line == 'end of comments':
        break

    comments.append(line)

print(f'<h1>\n    {title}\n</h1>')
print(f'<article>\n    {content}\n</article>')
for comment in comments:
    print(f'<div>\n    {comment}\n</div>')
