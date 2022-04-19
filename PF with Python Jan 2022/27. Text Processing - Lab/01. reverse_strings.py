# 1.Reverse Strings
# You will be given strings on separate lines until you receive an "end" command. Write a program that reverses strings and prints each pair on a separate line in the format "{word} = {reversed_word}".
#
# Input
# helLo
# Softuni
# bottle
# end
#
# Output
# helLo = oLleh
# Softuni = inutfoS
# bottle = elttob

# while True:
#     text = input()
#     if text == "end":
#         break
#     text_reversed = ""
#     for ch in reversed(text):
#         text_reversed += ch
#     print(text + " = " + text_reversed)

text = input()

# while text != "end":
#     rev = reversed(text)
#     reversed_text = "".join(rev)
#     print(f"{text} = {reversed_text}")
#     text = input()

while text != "end":
    reversed_text = ""
    for i in range(len(text)-1, -1, -1):
        reversed_text += text[i]
    print(f"{text} = {reversed_text}")
    text = input()
