# 08-02. TEXT PROCESSING [Exercise]
# 05. Emoticon Finder

text = input()

positions = [i for i, symbol in enumerate(text) if symbol == ':']

for position in positions:
    print(text[position:position+2])
