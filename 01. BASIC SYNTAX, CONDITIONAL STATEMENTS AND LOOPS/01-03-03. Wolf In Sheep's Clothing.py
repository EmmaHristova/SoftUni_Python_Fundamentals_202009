# 01-03. BASIC SYNTAX, CONDITIONAL STATEMENTS AND LOOPS [More Exercises]
# 03. Wolf In Sheep's Clothing

queue = input()
queue_list = queue.split(sep=", ")

for i in range(len(queue_list)):
    if queue_list[i] == "wolf":
        if i == len(queue_list)-1:
            print("Please go away and stop eating my sheep")
        else:
            print(f"Oi! Sheep number {len(queue_list)-1-i}! You are about to be eaten by a wolf!")
