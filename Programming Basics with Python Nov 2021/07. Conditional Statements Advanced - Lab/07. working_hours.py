# 7.Работно време
# Да се напише програма, която чете час от денонощието(цяло число) и ден от седмицата(текст) - въведени от потребителя и проверява дали офисът на фирма е отворен, като работното време на офисът е от 10-18 часа, от понеделник до събота включително
#
# вход
# 11
# Monday
#
# изход
# open

time = int(input())
day_of_the_week = input()

if 10 <= time <= 18:
    if day_of_the_week == 'Monday' \
        or day_of_the_week == 'Tuesday' \
        or day_of_the_week == 'Wednesday' \
        or day_of_the_week == 'Thursday' \
        or day_of_the_week == 'Friday' \
        or day_of_the_week == 'Saturday':
        print('open')
    elif day_of_the_week == 'Sunday':
        print('closed')
else:
    print('closed')
