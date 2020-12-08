# 03-02. LISTS BASICS [Exercise]
# 01. Invert Values

string = input()
numbers = list(string.split(' '))
numbers_opp = [int(i) * -1 for i in numbers]
print(numbers_opp)
