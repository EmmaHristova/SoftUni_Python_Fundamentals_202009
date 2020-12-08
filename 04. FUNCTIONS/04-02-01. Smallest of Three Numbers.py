# 04-02. LISTS BASICS [Exercise]
# 01. Smallest of Three Numbers

def min_of_three(num1, num2, num3):
    return min(num1, num2, num3)


a = int(input())
b = int(input())
c = int(input())

print(min_of_three(a, b, c))
