# 9. *Rage Quit
# Every gamer knows what rage-quitting means. It's when you're just not good enough, and you blame everybody else for losing a game - you press the CAPS LOCK key on the keyboard and flood the chat with gibberish to show your frustration.
# Peter is a gamer, a bad one. When he rage-quits, he wants to be the most annoying kid on his team; he wants something truly spectacular. He asks for your help.
# He'll give you a series of strings (containing only non-numerical characters) followed by non-negative numbers (N), e.g., "a3". You need to convert the letters to uppercase for each string and print it repeatedly N times on the console. In the example, you need to write back "AAA".
# First, on the output, you should print a statistic of the number of unique symbols used (case-insensitive) in the format: "Unique symbols used {0}".
# Next, print the rage message itself.
# The strings and numbers will not be separated by anything. The input will always start with a non-numeric symbol, and for each string, there will be a corresponding number. The input will be given on a single line.
# Input
# The input data should be read from the console.
# It consists of a single line holding a series of string-number sequences.
# The input data will always be valid. There is no need to check it explicitly.
# Output
# The output should be printed on the console. It should consist of exactly two lines:
# oOn the first line, print the number of unique symbols used in the message in the format described above.
# oOn the second line, print the rage message.
# Constraints
# The count of string-number pairs will be in the range [1 … 20 000].
# Each string will contain any character except digits. The length of each string will be in the range [1 … 20].
# The repeat count for each string will be an integer in the range [0 … 20].
# Allowed working time for your program: 0.3 seconds. Allowed memory: 64 MB.
#
# Input
# a3
#
# Output
# Unique symbols used: 1
# AAA

line = input()
ch_line = ""
num_line = ""

for i in range(len(line)):
    if line[i].isnumeric():
        ch_line += " "
    else:
        ch_line += line[i]
for i in range(len(line)):
    if not line[i].isnumeric():
        num_line += " "
    else:
        num_line += line[i]

ch_list = ch_line.split()
num_list = num_line.split()
ch_list_upper = list()

for group in ch_list:
    temp_group = ""
    for ch in group:
        temp_group += ch.upper()
    ch_list_upper.append(temp_group)

unique_symbols = len(set("".join(ch_list_upper)))
print(f"Unique symbols used: {unique_symbols}")

for i in range(len(ch_list_upper)):
    print(ch_list_upper[i]*int(num_list[i]), end="")
