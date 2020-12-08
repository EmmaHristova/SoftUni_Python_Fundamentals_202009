# 05-03. LISTS ADVANCED [More Exercises]
# 02. Car Race

def race_time(car):
    current_time = 0
    for t in car:
        if t > 0:
            current_time += t
        else:
            current_time = round(current_time * 0.80, 2)

    return current_time


car_race = input().split(' ')
car_race = list(map(int, car_race))

race_left = car_race[:len(car_race)//2]
race_right = car_race[len(car_race)//2+1:]
race_right.reverse()

time_left = race_time(race_left)
time_right = race_time(race_right)

if time_left < time_right:
    print(f'The winner is left with total time: {time_left:.1f}')
else:
    print(f'The winner is right with total time: {time_right:.1f}')
