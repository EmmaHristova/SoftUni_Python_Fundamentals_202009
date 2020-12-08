# 02-01. DATA TYPES AND VARIABLES [Lab]
# 02. Centuries to Minutes

c = int(input())
y = c * 100
d = int(y * 365.2422)
h = d * 24
m = h * 60

print(f"{c} centuries = {y} years = {d} days = {h} hours = {m} minutes")
