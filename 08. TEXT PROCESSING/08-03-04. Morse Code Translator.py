# 08-04. TEXT PROCESSING [More Exercises]
# 04. Morse Code Translator

morse_code = {'.-': 'A',
              '-...': 'B',
              '-.-.': 'C',
              '-..': 'D',
              '.': 'E',
              '..-.': 'F',
              '--.': 'G',
              '....': 'H',
              '..': 'I',
              '.---': 'J',
              '-.-': 'K',
              '.-..': 'L',
              '--': 'M',
              '-.': 'N',
              '---': 'O',
              '.--.': 'P',
              '--.-': 'Q',
              '.-.': 'R',
              '...': 'S',
              '-': 'T',
              '..-': 'U',
              '...-': 'V',
              '.--': 'W',
              '-..-': 'X',
              '-.--': 'Y',
              '--..': 'Z'}

morse_words = input().split(' | ')

for morse_word in morse_words:
    word = ''
    morse_letters = morse_word.split()
    for morse_letter in morse_letters:
        word += morse_code[morse_letter]
    print(word, end=' ')
