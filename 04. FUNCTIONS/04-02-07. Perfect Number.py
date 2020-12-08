# 04-02. FUNCTIONS [Exercise]
# 07. Perfect Number

def perfect_number(number):
    perfect = False
    sum_divisors = 0
    if number > 0:
        for i in range(1, number):
            if number % i == 0:
                sum_divisors += i
        if sum_divisors == number:
            perfect = True
    return perfect


if perfect_number(int(input())):
    print('We have a perfect number!')
else:
    print('It\'s not so perfect.')
