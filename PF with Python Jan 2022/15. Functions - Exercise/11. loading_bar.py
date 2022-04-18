# 11.* Loading Bar
# You will receive a single integer number between 0 and 100 (inclusive) divisible by 10 without remainder (0, 10, 20, 30...). Your task is to create a function that returns a loading bar depending on the number you have received in the input. Print the result on the console. For more clarification, see the examples below.
#
# Input
# 30
#
# Output
# 30% [%%%.......]
# Still loading...

def loading_bar(n):
    percent_string = (n // 10) * "%"
    dots_string = ((100 - n) // 10) * "."
    if n == 100:
        print(f"{n}% Complete!")
        print(f"[{percent_string}{dots_string}]")
    else:
        print(f"{n}% [{percent_string}{dots_string}]")
        print("Still loading...")

num = int(input())

loading_bar(num)
