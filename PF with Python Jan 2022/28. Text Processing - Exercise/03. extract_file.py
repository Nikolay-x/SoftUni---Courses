# 3. Extract File
# Write a program that reads the path to a file and subtracts the file name and its extension.
#
# Input
# C:\Internal\training-internal\Template.pptx
#
# Output
# File name: Template
# File extension: pptx

path = input().split("\\")
result = path[-1].split(".")

print(f"File name: {result[0]}")
print(f"File extension: {result[1]}")
