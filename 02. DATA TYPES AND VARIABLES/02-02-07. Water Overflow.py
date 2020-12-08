# 02-02. DATA TYPES AND VARIABLES [Exercise]
# 07. Water Overflow

capacity = 255
in_tank = 0
lines = int(input())
line = 1

while line <= lines:
    pour = int(input())
    if in_tank + pour > capacity:
        print("Insufficient capacity!")
    else:
        in_tank += pour
    line += 1

print(in_tank)
