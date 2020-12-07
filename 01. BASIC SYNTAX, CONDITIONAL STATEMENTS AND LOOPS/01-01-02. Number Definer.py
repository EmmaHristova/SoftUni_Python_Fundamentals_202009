# 02. Number Definer

num = float(input())

if num > 0:
    if num > 1000000:
        print("large positive")
    elif num < 1:
        print("small positive")
    else:
        print("positive")
elif num < 0:
    if num < -1000000:
        print("large negative")
    elif num > -1:
        print("small negative")
    else:
        print("negative")
else:
    print("zero")
