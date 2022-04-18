# 4.Palindrome Strings
# On the first line, you will receive words separated by a single space. On the second line, you will receive a palindrome. First, you should print a list containing all the found palindromes in the sequence. Then, you should print the number of occurrences of the given palindrome in the format: "Found palindrome {number} times".
#
# Input
# wow father mom wow shirt stats
# wow
#
# Output
# ['wow', 'mom', 'wow', 'stats']
# Found palindrome 2 times

words = input().split(" ")
palindrome = input()

palindrome_count = 0
palindrome_list = []

for word in words:
    temp_list = []
    for ch in word:
        temp_list.append(ch)
    temp_list.reverse()
    if word == "".join(temp_list):
        palindrome_list.append(word)

palindrome_count = words.count(palindrome)

print(palindrome_list)
print(f"Found palindrome {palindrome_count} times")
