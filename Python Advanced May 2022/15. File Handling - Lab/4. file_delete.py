# 4.File Delete
# Create a program that deletes the file you created in the previous task. If you try to delete the file multiple times, print the message: 'File already deleted!'.

from os import remove

file_path = './my_first_file.txt'

try:
    remove(file_path)
except FileNotFoundError:
    print('File already deleted!')
