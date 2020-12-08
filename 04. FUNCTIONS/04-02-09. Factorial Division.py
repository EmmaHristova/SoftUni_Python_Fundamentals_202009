# 04-02. LISTS BASICS [Exercise]
# 09. Factorial Division

import math


def factorial_division(num1, num2):
    factorial1 = math.factorial(num1)
    factorial2 = math.factorial(num2)
    return factorial1 / factorial2


result = factorial_division(int(input()), int(input()))
print(f'{result:.2f}')
