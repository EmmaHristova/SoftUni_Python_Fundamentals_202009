# 02-02. DATA TYPES AND VARIABLES [Exercise]
# 03. Elevator

from math import ceil

people = int(input())
capacity = int(input())

courses = ceil(people / capacity)
print(courses)
