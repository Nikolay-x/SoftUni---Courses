# 5. Emoticon Finder
# Find all emoticons in the text. An emoticon always starts with ":" and is followed by a symbol.
# The input will be provided as a single string.
#
# Input
# There are so many emoticons nowadays :P. I have many ideas :O what input to place here :)
#
# Output
# :P
# :O
# :)

# def emoticon_finder(text):
#     result = [text[i] + text[i + 1] for i in range(len(text)) if text[i] == ":"]
#     print("\n".join(result))
#
#
# input_text = input()
# emoticon_finder(input_text)

text = input()
for i, ch in enumerate(text):
    if ch == ":":
        print(text[i] + text[i+1])
