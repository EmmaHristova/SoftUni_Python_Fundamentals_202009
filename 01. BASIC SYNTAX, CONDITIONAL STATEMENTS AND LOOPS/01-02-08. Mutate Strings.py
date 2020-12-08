# 01-02. BASIC SYNTAX, CONDITIONAL STATEMENTS AND LOOPS [Exercise]
# 08. Mutate Strings

string_1 = input()
string_2 = input()

string_prev = string_1

for i in range(1, len(string_1)+1):
    string_new = string_2[:i] + string_1[i:]
    if string_new != string_prev:
        print(string_new)
        string_prev = string_new
