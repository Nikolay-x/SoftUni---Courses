# 3.Leonardo DiCaprio Oscars
# Write a program that receives a single integer number and prints different messages depending on the number:
# -If the number is 88 - "Leo finally won the Oscar! Leo is happy".
# -If the number is 86 - "Not even for Wolf of Wall Street?!"
# -If the number is not 88 nor 86 (and below 88) - "When will you give Leo an Oscar?"
# -If the number is over 88 - "Leo got one already!"
#
# Input
# 88
#
# Output
# Leo finally won the Oscar! Leo is happy

number = int(input())

if number == 88:
    print(f"Leo finally won the Oscar! Leo is happy")
elif number == 86:
    print(f"Not even for Wolf of Wall Street?!")
elif number != 88 and number != 86 and number < 88:
    print(f"When will you give Leo an Oscar?")
elif number > 88:
    print(f"Leo got one already!")
