# 6.Reverse string
# Create a generator function called reverse_text that receives a string and yields all string characters on one line in reversed order.
# Note: Submit only the function in the judge system
#
# Test Code
# for char in reverse_text("step"):
#     print(char, end='')
#
# Output
# pets

def reverse_text(string):
    i = -1
    while i > -(len(string) + 1):
        yield string[i]
        i -= 1


for char in reverse_text("step"):
    print(char, end='')
