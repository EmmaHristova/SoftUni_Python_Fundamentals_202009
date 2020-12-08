# 04-01. FUNCTIONS [Lab]
# 05. Calculate Rectangle Area

def rectangle_area(side_a, side_b):
    return side_a * side_b


rec_side_a = int(input())
rec_side_b = int(input())
print(rectangle_area(rec_side_a, rec_side_b))
