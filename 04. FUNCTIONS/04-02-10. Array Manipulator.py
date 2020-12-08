# 04-02. FUNCTIONS [Exercise]
# 10. Array Manipulator

def odd_even(manipulated):
    even = []
    odd = []
    for val in manipulated:
        if val % 2 == 0:
            even.append(val)
        else:
            odd.append(val)
    return even, odd


def exchange(manipulated, split_idx):
    if 0 <= split_idx < len(manipulated):
        array1 = manipulated[:split_idx + 1]
        array2 = manipulated[split_idx + 1:]
        manipulated = array2 + array1
        even, odd = odd_even(manipulated)
        return manipulated, even, odd
    else:
        even, odd = list_even, list_odd
        print('Invalid index')
        return manipulated, even, odd


def min_max(manipulated, operator, num_type):
    idx = None
    for i in range(len(manipulated)):
        if len(list_even) > 0 and num_type == 'even':
            if operator == 'min' and manipulated[i] == min(list_even):
                idx = i
            elif operator == 'max' and manipulated[i] == max(list_even):
                idx = i
        elif len(list_odd) > 0 and num_type == 'odd':
            if operator == 'min' and manipulated[i] == min(list_odd):
                idx = i
            elif num_type == 'odd' and operator == 'max' and manipulated[i] == max(list_odd):
                idx = i
    if idx is not None:
        print(idx)
    else:
        print('No matches')


def first_last(manipulated, operator, count, num_type):
    if count <= len(manipulated):
        if num_type == 'even':
            if operator == 'first' and count < len(list_even):
                print(list_even[:count])
            elif operator == 'last' and count < len(list_even):
                print(list_even[-count:])
            else:
                print(list_even)
        if num_type == 'odd':
            if operator == 'first' and count < len(list_odd):
                print(list_odd[:count])
            elif operator == 'last' and count < len(list_odd):
                print(list_odd[-count:])
            else:
                print(list_odd)
    else:
        print('Invalid count')


array = input().split(' ')
array = list(map(int, array))
list_even, list_odd = odd_even(array)

while True:
    command = input().split()

    if command[0] == 'exchange':
        array, list_even, list_odd = exchange(array, int(command[1]))
    if command[0] == 'min' or command[0] == 'max':
        min_max(array, command[0], command[1])
    if command[0] == 'first' or command[0] == 'last':
        first_last(array, command[0], int(command[1]), command[2])
    if command[0] == 'end':
        break

print(array)
