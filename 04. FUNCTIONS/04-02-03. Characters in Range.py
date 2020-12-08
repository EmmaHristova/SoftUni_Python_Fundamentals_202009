# 04-02. FUNCTIONS [Exercise]
# 03. Characters in Range

def ascii_range(char1, char2):
    for char in range(ord(char1)+1, ord(char2)):
        print(chr(char), end=' ')


string1 = input()
string2 = input()

ascii_range(string1, string2)
