# 2.Line Numbers
# Write a program that reads a text file, inserts line numbers in front of each line, and counts all the letters and punctuation marks. The result should be written to another text file.
#
# text.txt
# -I was quick to judge him, but it wasn't his fault.
# -Is this some kind of joke?! Is it?
# -Quick, hide here. It is safer.
#
# output.txt
# Line 1: -I was quick to judge him, but it wasn't his fault. (37)(4)
# Line 2: -Is this some kind of joke?! Is it? (24)(4)
# Line 3: -Quick, hide here. It is safer. (22)(4)

file_path = './text.txt'
output_path = './output_task2.txt'
punctuation_marks_list = ["!", "," ,"\'" ,";" ,"\"", ".", "-" ,"?"]

with open(file_path, "r+") as file, open(output_path, "w") as output_file:
    for idx, line in enumerate(file):
        letters_count = 0
        punctuation_marks = 0

        for ch in line:
            if ch.isalpha():
                letters_count += 1
            if ch in punctuation_marks_list:
                punctuation_marks += 1

        result = f'Line {idx+1}: {line.strip()} ({letters_count})({punctuation_marks})\n'
        output_file.write(result)
