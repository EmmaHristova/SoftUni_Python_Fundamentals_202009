# 04-02. LISTS BASICS [Exercise]
# 06. Password Validator

def valid_pass(string):
    valid_password = True
    if not 6 <= len(string) <= 10:
        valid_password = False
        print('Password must be between 6 and 10 characters')
    for char in string:
        if not (char.isalpha() or char.isnumeric()):
            valid_password = False
            print('Password must consist only of letters and digits')
            break
    count_numeric = 0
    for char in string:
        if char.isnumeric():
            count_numeric += 1
    if not count_numeric >= 2:
        valid_password = False
        print('Password must have at least 2 digits')
    if valid_password:
        print('Password is valid')


valid_pass(input())
