# 1.Even Lines
# Write a program that reads a text file and prints on the console its even lines. Line numbers start from 0. Before you print the result, replace {"-", ",", ".", "!", "?"} with "@" and reverse the order of the words.
#
# text.txt
# -I was quick to judge him, but it wasn't his fault.
# -Is this some kind of joke?! Is it?
# -Quick, hide here. It is safer.
#
# output
# fault@ his wasn't it but him@ judge to quick was @I
# safer@ is It here@ hide @Quick@

text_path = './text.txt'
symbols_to_be_changed = {"-", ",", ".", "!", "?"}

with open(text_path, 'r') as file:
    for idx, line in enumerate(file):
        if idx % 2 == 0:
            line = " ".join(line.split()[::-1])

            for symbol in symbols_to_be_changed:
                line = line.replace(symbol, "@")
            print(line)

            # for ch in line:
            #     if ch in symbols_to_be_changed:
            #         line = line.replace(ch, "@")
            # print(line)

            # result = ""
            # for ch in line:
            #     if ch in symbols_to_be_changed:
            #         ch = "@"
            #     result += ch
            # print(result)
