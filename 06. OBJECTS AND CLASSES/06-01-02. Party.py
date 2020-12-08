# 06-01. OBJECTS AND CLASSES [Lab]
# 02. Party

class Party:
    def __init__(self):
        self.people = []


party = Party()

while True:
    command = input()
    if command == 'End':
        break
    else:
        party.people.append(command)

print(f'Going: {", ".join(party.people)}')
print(f'Total: {len(party.people)}')
