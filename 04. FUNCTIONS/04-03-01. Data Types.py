# 04-03. FUNCTIONS [More Exercises]
# 01. Data Types

def data_manipulation(data_type, data_value):
    if data_type == 'int':
        result = int(data_value) * 2
    elif data_type == 'real':
        result = f'{float(data_value) * 1.5:.2f}'
    else:
        result = '$' + data_value + '$'
    return result


print(data_manipulation(input(), input()))
