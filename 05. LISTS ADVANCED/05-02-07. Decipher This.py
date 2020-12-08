# 05-02. LISTS ADVANCED [Exercise]
# 07. Decipher This!

message = input().split(' ')

for word in message:
    first_letter = ''
    next_letters = ''
    for letter in word:
        if letter.isnumeric():
            first_letter += letter
        else:
            next_letters += letter
    if len(next_letters) > 1:
        decipher_word = chr(int(first_letter)) + next_letters[-1] + next_letters[1:-1] + next_letters[0]
    else:
        decipher_word = chr(int(first_letter)) + next_letters[0]
    print(decipher_word, end=' ')
