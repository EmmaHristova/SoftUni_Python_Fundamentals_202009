# 08-02. TEXT PROCESSING [Exercise]
# 10. Winning Ticket

# Accepted code
def is_valid(string):
    if len(string) == 20:
        return True
    else:
        return False


def is_jackpot(string):
    for symbol in winning_symbols:
        if symbol * 20 == string:
            return True
    return False


def is_winner(string):
    left_side = string[0:10]
    right_side = string[10:20]

    winner = False
    count = 0
    winning_symbol = ''

    for symbol in winning_symbols:
        if symbol * 6 in left_side and symbol * 6 in right_side:
            winner = True
            count = min(left_side.count(symbol), right_side.count(symbol))
            winning_symbol = symbol

    return winner, count, winning_symbol


winning_symbols = ['@', '#', '$', '^']
tickets = input().split(',')

for t in tickets:
    ticket = t.strip()

    if not is_valid(ticket):
        print('invalid ticket')
        continue

    if is_jackpot(ticket):
        print(f'ticket "{ticket}" - 10{ticket[0]} Jackpot!')
        continue

    winner, count, winning_symbol = is_winner(ticket)

    if winner:
        print(f'ticket "{ticket}" - {count}{winning_symbol}')
    else:
        print(f'ticket "{ticket}" - no match')


# Correct code
def is_valid(string):
    if len(string) == 20:
        return True
    else:
        return False


def is_jackpot(string):
    for symbol in winning_symbols:
        if symbol * 20 == string:
            return True
    return False


def is_winner(string):
    winning_symbols_only = ''
    for char in string:
        if char in winning_symbols:
            winning_symbols_only += char
        else:
            winning_symbols_only += ' '

    left_side = [x for x in winning_symbols_only[0:10].split() if len(x) >= 6]
    right_side = [x for x in winning_symbols_only[10:20].split() if len(x) >= 6]

    winner = False
    count = 0
    winning_symbol = ''

    if not left_side == [] and not right_side == []:
        if left_side[0] in right_side[0] or right_side[0] in right_side[0]:
            winner = True
            count = min(len(left_side[0]), len(right_side[0]))
            winning_symbol = list(set(left_side[0]))[0]

    return winner, count, winning_symbol


winning_symbols = ['@', '#', '$', '^']
tickets = input().split(',')

for t in tickets:
    ticket = t.strip()

    if not is_valid(ticket):
        print('invalid ticket')
        continue

    if is_jackpot(ticket):
        print(f'ticket "{ticket}" - 10{ticket[0]} Jackpot!')
        continue

    winner, count, winning_symbol = is_winner(ticket)

    if winner:
        print(f'ticket "{ticket}" - {count}{winning_symbol}')
    else:
        print(f'ticket "{ticket}" - no match')
