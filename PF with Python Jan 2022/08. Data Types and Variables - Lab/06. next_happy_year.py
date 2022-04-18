# 6.Next Happy Year
# You are saying goodbye to your best friend: "See you next happy year". Happy Year is the year with only distinct digits, for example, 2018. Write a program that receives an integer number and finds the next happy year.
#
# Input
# 8989
#
# Output
# 9012

year = int(input())

is_happy_year = False

while not is_happy_year:
    year += 1
    str_year = str(year)

    set_year = set(str_year)

    # set_year = set()
    # for i in range(len(str_year)):
    #     set_year.add(str_year[i])

    is_happy_year = len(str_year) == len(set_year)

print(year)
