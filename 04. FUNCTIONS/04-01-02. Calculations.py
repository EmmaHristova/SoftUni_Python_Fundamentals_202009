# 04-01. LISTS BASICS [Lab]
# 02. Calculations

def calculator(a, b, operator):
    if operator == 'multiply':
        return a * b
    elif operator == 'divide':
        return a / b
    elif operator == 'add':
        return a + b
    elif operator == 'subtract':
        return a - b


result = int(calculator(operator = input(), a = int(input()), b = int(input())))
print(result)
