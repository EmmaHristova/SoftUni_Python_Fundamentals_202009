# 04-02. LISTS BASICS [Exercise]
# 04. Odd and Even Sum

def odd_even_sum(string):
    odd_sum = 0
    even_sum = 0
    for char in string:
        num = int(char)
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num
    print(f'Odd sum = {odd_sum}, Even sum = {even_sum}')


odd_even_sum(input())
