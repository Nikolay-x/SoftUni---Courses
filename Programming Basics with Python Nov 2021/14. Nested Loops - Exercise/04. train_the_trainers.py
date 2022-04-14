# 4.Train the Trainers
# Курсът "Train the trainers" е към края си и финалното оценяване наближава. Вашата задача е да помогнете на журито, което ще оценява презентациите, като напишете програма, в която да изчислява средната оценка от представянето на всяка една презентация от даден студент, а накрая - средния успех от всички тях.
# От конзолата на първият ред се прочита броят на хората в журито n - цяло число.
# След това на отделен ред се прочита името на презентацията – текст.
# За всяка една презентация на нов ред се четат n - на брой оценки - реално число.
# След изчисляване на средната оценка за конкретна презентация, на конзолата се печата:
#  "{името на презентацията} - {средна оценка}."
# След получаване на команда "Finish", на конзолата се печата "Student's final assessment is {среден успех от всички презентации}." и програмата приключва.
# Всички оценки трябва да бъдат форматирани до втория знак след десетичната запетая.
#
# Вход
# 2
# While-Loop
# 6.00
# 5.50
# For-Loop
# 5.84
# 5.66
# Finish
#
# Изход
# While-Loop - 5.75.
# For-Loop - 5.75.
# Student's final assessment is 5.75.

jury_count = int(input())

total_mark_sum = 0
presentation_count = 0
command = input()

while command != "Finish":
    presentation = command
    mark_sum = 0

    for i in range(1, jury_count +1):
        presentation_mark = float(input())
        mark_sum += presentation_mark

    avg_mark = mark_sum / jury_count
    print(f"{presentation} - {(avg_mark):.2f}.")
    total_mark_sum += avg_mark
    presentation_count += 1

    command = input()

print(f"Student's final assessment is {(total_mark_sum / presentation_count):.2f}.")
