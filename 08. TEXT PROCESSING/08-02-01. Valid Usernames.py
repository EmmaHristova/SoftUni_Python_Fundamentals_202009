# 08-02. TEXT PROCESSING [Exercise]
# 01. Valid Usernames

usernames = input().split(', ')

for username in usernames:
    is_valid = True
    if 3 <= len(username) <= 16:
        if len(username) == len(username.strip()):
            for char in username:
                if char.isalpha() or char.isdigit() or char in ('-', '_'):
                    is_valid = True
                else:
                    is_valid = False
                    break
        else:
            is_valid = False
    else:
        is_valid = False

    if is_valid:
        print(username)
