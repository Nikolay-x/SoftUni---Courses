# 4.Directory Traversal
# Write a program that traverses a given directory for all files. Search through the first level of the directory only and write information about each found file in report.txt. The files should be grouped by their extension. Extensions should be ordered by name alphabetically. The files with extensions should also be sorted by name. report.txt should be saved in the chosen directory.
#
# Example Directory View
# index.html
# index.js
# python.py
# demo.pptx
# log.txt
# notes.txt
# program.py
#
# report.txt
# .html
# - - - index.html
# .js
# - - - index.js
# .pptx
# - - - demo.pptx
# .py
# - - - program.py
# - - - python.py
# .txt
# - - - log.txt
# - - - notes.txt

from os import listdir, walk
from os.path import isfile, join

dir_path = "./"
report_path = "./report_task4.txt"

only_files = [f for f in listdir(dir_path) if isfile((join(dir_path, f)))]
files_dict = {}
for file in only_files:
    key = file.split(".")[-1]
    if key not in files_dict:
        files_dict[key] = []
    files_dict[key].append(file)

# files_dict = {}
# for _, _, files in walk('.'):
#     for file in files:
#         ext = file.split('.')[-1]
#         if ext not in files_dict:
#             files_dict[ext] = []
#         files_dict[ext].append(file)

sorted_files_dict = sorted(files_dict.items(), key=lambda x: x[0])

with open(report_path, "w") as report:
    for extension, files in sorted_files_dict:
        report.write(f".{extension}\n")
        for file in sorted(files):
            report.write(f"- - - {file}\n")

# from os import listdir
# from os.path import isdir, join
#
#
# def directory_traversal(path, files_by_ext):
#     for element in listdir(path):
#         if isdir(join(path, element)):
#             directory_traversal(join(path, element), files_by_ext)
#         else:
#             extension = element.split('.')[-1]
#             if extension not in files_by_ext:
#                 files_by_ext[extension] = []
#             files_by_ext[extension].append(element)
#
#
# result = {}
# directory_traversal('./', result)
#
# # for key, value in result.items():
# #     print(key, value)
#
# with open('./result_task4.txt', 'w') as output_file:
#     for ext, files in result.items():
#         output_file.write(ext + '\n')
#         for file in files:
#             output_file.write(f'- - - {file}\n')
