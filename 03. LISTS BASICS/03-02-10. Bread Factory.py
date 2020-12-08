# 03-02. LISTS BASICS [Exercise]
# 10. Bread Factory

energy = 100
coins = 100
managed = True

events = input().split('|')

for event in events:
    event_type, number = event.split('-')
    number = int(number)
    if event_type == 'rest':
        if energy < 100:
            gain = min(number, 100 - energy)
            energy += gain
        else:
            gain = 0
        print(f'You gained {gain} energy.')
        print(f'Current energy: {energy}.')
    elif event_type == 'order':
        if energy >= 30:
            coins += number
            energy -= 30
            print(f'You earned {number} coins.')
        else:
            energy += 50
            print('You had to rest!')
    else:
        if coins > number:
            coins -= number
            print(f'You bought {event_type}.')
        else:
            print(f'Closed! Cannot afford {event_type}.')
            managed = False
            break

if managed:
    print('Day completed!')
    print(f'Coins: {coins}')
    print(f'Energy: {energy}')
