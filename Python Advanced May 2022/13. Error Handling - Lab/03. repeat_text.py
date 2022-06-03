# 3.Repeat Text
# Write a program that receives a text on the first line and times (to repeat the text) that must be an integer. If the user passes non-integer type for the times variable, handle the exception and print a message
# "Variable times must be an integer".
#
# Input
# Hello
# Bye
# Hello
# 2
#
# Output
# Variable times must be an integer
# HelloHello

# import sys
# from io import StringIO
#
# test_input1 = '''Hello
# Bye
# '''
#
# test_input2 = '''Hello
# 2
# '''
#
# # sys.stdin = StringIO(test_input1)
# sys.stdin = StringIO(test_input2)
#
# text = input()
#
# try:
#     times = int(input())
#     print(text * times)
# except ValueError:
#     print('Variable times must be an integer')

text = input()

try:
    number = int(input())
    print(text * number)
except ValueError:
    print("Variable times must be an integer")
