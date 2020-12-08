# 08-03. TEXT PROCESSING [More Exercises]
# 03. Treasure Finder

key = input().split()
key = list(map(int, key))

while True:
    line = input()
    if line == 'find':
        break

    hidden_message = ''

    while True:
        key_idx = 0
        for char in line:
            hidden_message += chr(ord(char) - key[key_idx])
            if key_idx < len(key) - 1:
                key_idx += 1
            else:
                key_idx = 0
        break

    treasure_start = hidden_message.find('&')
    treasure_end = hidden_message.rfind('&')
    treasure = hidden_message[treasure_start+1:treasure_end]

    coordinates_start = hidden_message.find('<')
    coordinates_end = hidden_message.rfind('>')
    coordinates = hidden_message[coordinates_start+1:coordinates_end]

    print(f'Found {treasure} at {coordinates}')
