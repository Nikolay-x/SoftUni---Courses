# 8. Обедна почивка
# По време на обедната почивка искате да изгледате епизод от своя любим сериал. Вашата задача е да напишете програма, с която ще разберете дали имате достатъчно време да изгледате епизода. По време на почивката отделяте време за обяд и време за отдих. Времето за обяд ще бъде 1/8 от времето за почивка, а времето за отдих ще бъде 1/4 от времето за почивка.
# Вход
# От конзолата се четат 3 реда:
# 1.Име на сериал – текст
# 2.Продължителност на епизод  – цяло число в диапазона [10… 90]
# 3.Продължителност на почивката  – цяло число в диапазона [10… 120]
# Изход
# На конзолата да се изпише един ред:
# Ако времето е достатъчно да изгледате епизода:
# "You have enough time to watch {име на сериал} and left with {останало време} minutes free time."
# Ако времето не Ви е достатъчно:
# "You don't have enough time to watch {име на сериал}, you need {нужно време} more minutes."
# Времето да се закръгли до най-близкото цяло число нагоре.
#
# Вход
# Game of Thrones
# 60
# 96
#
# Изход
# You have enough time to watch Game of Thrones and left with 0 minutes free time.

from math import ceil

film_name = str(input())
film_duration = int(input())
break_duration = int(input())

lunch_time = break_duration * 1 / 8
rest_time = break_duration * 1 / 4
break_left = break_duration - lunch_time - rest_time

if break_left >= film_duration:
    print(f"You have enough time to watch {film_name} and left with "
          f"{ceil(break_left - film_duration)} minutes free time.")
else:
    print(f"You don't have enough time to watch {film_name}, you "
          f"need {ceil(film_duration - break_left)} more minutes.")
