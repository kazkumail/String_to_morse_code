MORSE_CODE_LIST = []

CODE = {'A': '.-', 'B': '-...', 'C': '-.-.',
        'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..',
        'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-',
        'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',

        '0': '-----', '1': '.----', '2': '..---',
        '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..',
        '9': '----.'
        }

print('Hello, Welcome to the Morse code encoder program. ')
TO_ENCODE = input('To begin, please enter the words you would like to encode: ')
TO_ENCODE = TO_ENCODE.upper()
TO_ENCODE = TO_ENCODE.replace(" ", "")

SPLIT_TO_ENCODE = list(TO_ENCODE)

for letter in SPLIT_TO_ENCODE:
    letter_str = str(letter)
    CODED_LETTER = CODE[letter_str]
    MORSE_CODE_LIST.append(CODED_LETTER)

print(MORSE_CODE_LIST)
