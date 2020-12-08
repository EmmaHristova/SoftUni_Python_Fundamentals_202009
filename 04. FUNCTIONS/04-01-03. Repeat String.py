# 04-01. LISTS BASICS [Lab]
# 03. Repeat String

def repeat(string, n):
    return string * n


string_input = input()
n_input = int(input())

result = repeat(string_input, n_input)
print(result)
