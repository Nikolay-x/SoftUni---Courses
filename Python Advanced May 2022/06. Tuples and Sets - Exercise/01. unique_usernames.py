# 1.Unique Usernames
# Write a program that reads from the console a sequence of N usernames and keeps a collection only of the unique ones. On the first line, you will receive an integer N. On the next N lines, you will receive a username. Print the collection on the console (the order does not matter):
#
# Input
# 6
# George
# George
# George
# Peter
# George
# NiceGuy1234
#
# Output
# George
# Peter
# NiceGuy1234

n = int(input())
usernames =  set()

for _ in range(n):
    username = input()
    usernames.add(username)

[print(username) for username in usernames]
