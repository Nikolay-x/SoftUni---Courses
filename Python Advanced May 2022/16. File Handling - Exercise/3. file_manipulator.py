# 3.File Manipulator
# Create a program that will receive commands until the command "End". The commands can be:
# "Create-{file_name}" - Creates the given file with an empty content. If the file already exists, remove the existing text in it (as if the file is created again)
# "Add-{file_name}-{content}" - Append the content and a new line after it. If the file does not exist, create it, and add the content
# "Replace-{file_name}-{old_string}-{new_string}" - Open the file and replace all the occurrences of the old string with the new string. If the file does not exist, print: "An error occurred"
# "Delete-{file_name}" - Delete the file. If the file does not exist, print: "An error occurred"
#
# Input
# Create-file.txt
# Add-file.txt-First Line
# Add-file.txt-Second Line
# Replace-random.txt-Some-some
# Replace-file.txt-First-1st
# Replace-file.txt-Second-2nd
# Delete-random.txt
# Delete-file.txt
# End
#
# Comment
# The first command creates the empty file
# After the first and second Add command, the content is:
# First Line
# Second Line
# On the first Replace command, an error must occur
# After the next two Replace commands, the content is:
# 1st Line
# 2nd Line
# After the first Delete command, an error occurs
# Finally, the 'file.txt' file is deleted

from os import remove
from os.path import exists

while True:
    line = input()
    if line == "End":
        break

    line = line.split("-")
    command, file_name = line[0], line[1]
    file_path = f'./{file_name}'

    if command == "Create":
        with open(file_path, "w") as file:
            # pass
            file.write("")

    if command == "Add":
        content = line[2]
        with open(file_path, "a") as file:
            file.write(f'{content}\n')

    if command == "Replace":
        old_string = line[2]
        new_string = line[3]
        if exists(file_path):

            # with open(file_path, "r+") as file:
            #     file_content = file.read().replace(old_string, new_string)
            #     file.seek(0)
            #     file.truncate(0)
            #     file.write(file_content)

            result = []
            with open(file_path, "r+") as file:
                for ln in file:
                    result.append(ln.strip())

                file.truncate(0)
                file.seek(0)

                for ln1 in result:
                    file.write(f'{ln1.replace(old_string, new_string)}\n')

        else:
            print("An error occurred")

    if command == "Delete":
        if exists(file_path):
            remove(file_path)
        else:
            print("An error occurred")
