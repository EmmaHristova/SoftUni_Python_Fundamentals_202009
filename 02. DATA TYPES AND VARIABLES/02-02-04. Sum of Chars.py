# 02-02. DATA TYPES AND VARIABLES [Exercise]
# 04. Sum of Chars

num_lines = int(input())
line = 1
sum = 0

while line <= num_lines:
    letter = input()
    sum += ord(letter)
    line += 1

print(f"The sum equals: {sum}")
