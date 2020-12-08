# 04-02. LISTS BASICS [Exercise]
# 05. Palindrome Integers

def palindrome(string):
    integers = string.split(', ')
    for i in integers:
        palindrome_integer = True
        i_half_len = len(i) / 2
        for j in range(int(i_half_len)):
            if not i[j] == i[-1-j]:
                palindrome_integer = False
                break
        print(palindrome_integer)


palindrome(input())
