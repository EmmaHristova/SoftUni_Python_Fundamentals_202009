# 05-03. LISTS ADVANCED [More Exercises]
# 04. Social Distribution

population = input().split(', ')
population = list(map(int, population))
min_wealth = int(input())

if sum(population) / len(population) >= min_wealth:
    possible = True
else:
    possible = False

if possible:
    exchange = 0
    for i, val in enumerate(population):
        idx = population.index(max(population))
        if val < min_wealth:
            exchange = min_wealth - val
            if population[idx] - exchange >= min_wealth:
                population[i] += exchange
                population[idx] -= exchange
    print(population)
else:
    print('No equal distribution possible')
