# 01-03. BASIC SYNTAX, CONDITIONAL STATEMENTS AND LOOPS [More Exercises]
# 05. How Much Coffee Do You Need?

coffee = 0

while True:
    command = input()
    if command.lower() in ["coding", "dog", "cat", "movie"]:
        if command.islower():
            coffee += 1
        else:
            coffee += 2
    elif command == "END":
        break

if coffee <= 5:
    print(coffee)
else:
    print("You need extra sleep")
