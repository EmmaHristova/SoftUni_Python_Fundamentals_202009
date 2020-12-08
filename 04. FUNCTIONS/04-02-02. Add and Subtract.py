# 04-02. LISTS BASICS [Exercise]
# 02. Add and Subtract

def sum_numbers(num1, num2):
    return num1 + num2


def subtract(summed, num3):
    return summed - num3


def add_and_subtract(num1, num2, num3):
    return subtract(sum_numbers(num1, num2), num3)


a = int(input())
b = int(input())
c = int(input())

print(add_and_subtract(a, b, c))
