# 4.Morse Code Translator
# Write a program that translates messages from Morse code to English (capital letters). Use this page to help you (without the numbers). The words will be separated by a space (' '). Each word is separated by a ' | '.
# Print the found words on one line, separated by a space.
#
# Input
# .. | -- .- -.. . |  -.-- --- ..- | .-- .-. .. - . | .- | .-.. --- -. --. | -.-. --- -.. .
#
# Output
# I MADE YOU WRITE A LONG CODE

morse_code_l_c = {'A': '.-', 'B': '-...', 'C': '-.-.',
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

morse_code_c_l = {value: key for key, value in morse_code_l_c.items()}


def to_morse(s):
    return ' '.join(morse_code_l_c.get(i.upper()) for i in s)


def from_morse(s):
    return ''.join(morse_code_c_l.get(i) for i in s.split())


def input_line(line):
    line = line.split(" | ")
    result_line = []
    for word in line:
        result_word = ""
        word = word.split(" ")
        for code in word:
            result_word += from_morse(code)
        result_line.append(result_word)
    return " ".join(result_line)


input_code = input()
print(input_line(input_code))
