# 05-02. LISTS ADVANCED [Exercise]
# 09. Heart Delivery

neighborhood = input().split('@')
neighborhood = list(map(int, neighborhood))
house = 0

while True:
    command = input().split(' ')
    if command[0] == 'Jump':

        house += int(command[1])
        if house >= len(neighborhood):
            house = 0

        if neighborhood[house] == 0:
            print(f'Place {house} already had Valentine\'s day.')
        else:
            neighborhood[house] = max(neighborhood[house] - 2, 0)
            if neighborhood[house] == 0:
                print(f'Place {house} has Valentine\'s day.')

    else:
        break

print(f'Cupid\'s last position was {house}.')

failed = 0

for house in neighborhood:
    if house > 0:
        failed += 1

if failed == 0:
    print('Mission was successful.')
else:
    print(f'Cupid has failed {failed} places.')
