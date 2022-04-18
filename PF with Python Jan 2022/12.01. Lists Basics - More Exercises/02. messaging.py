# 2.Messaging
# On the first line, you will receive a sequence of numbers separated by a single space. On the second line, you will receive a string.
# Your task is to write a program that sends a message only using chars from the given string. Each char the program adds to the message should be found by its index. The index you are looking for is the sum of a number's digits from the sequence. If the index is greater than the length of the text, continue counting from the beginning (so that you always have a valid index). When you find a char, you should add it to the message and remove it from the string. It means that for the following index, the text will be with one character less.
# Print the final message.
#
# Input
# 9992 562 8933
# This is some message for you
#
# Output
# Hey

num_seq = input().split(" ")
string = input()

int_num_seq = list(map(int, num_seq))

num_sum_list = []
message = []

for i in int_num_seq:
    num = i
    num_sum = 0
    while num / 10 > 0:
        num_sum += num % 10
        num = int(num / 10)
    num_sum_list.append(num_sum)

for i in num_sum_list:
    if i < len(string):
        message.append(string[i])
        string = string[:i] + string[i+1:]
    else:
        j = i % len(string)
        message.append(string[j])
        string = string[:j] + string[j+1:]

print("".join(message))
