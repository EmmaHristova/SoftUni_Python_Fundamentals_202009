# 03-01. LISTS BASICS [Lab]
# 03. List Statistics

lines = int(input())
positives = []
negatives = []

for i in range(lines):
    number = int(input())
    if number >= 0:
        positives.append(number)
    else:
        negatives.append(number)

count_positives = len(positives)
sum_negatives = sum(negatives)

print(positives)
print(negatives)
print(f"Count of positives: {count_positives}. Sum of negatives: {sum_negatives}")
