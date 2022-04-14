# 2.Подготовка за изпит
# Напишете програма, в която Марин решава задачи от изпити, докато не получи съобщение "Enough" от лектора си. При всяка решена задача той получава оценка. Програмата трябва да приключи прочитането на данни при команда "Enough" или ако Марин получи определения брой незадоволителни оценки. Незадоволителна е всяка оценка, която е по-малка или равна на 4.
# Вход
# На първи ред - брой незадоволителни оценки - цяло число;
# След това многократно се четат по два реда:
# oИме на задача – текст;
# oОценка - цяло число в интервала [2…6]
# Изход
# Ако Марин стигне до командата "Enough", отпечатайте на 3 реда:
# o"Average score: {средна оценка}"
# o"Number of problems: {броя на всички задачи}"
# o"Last problem: {името на последната задача}"
# Ако получи определеният брой незадоволителни оценки:
# o"You need a break, {брой незадоволителни оценки} poor grades."
# Средната оценка да бъде форматирана до втория знак след десетичната запетая.
#
# Вход
# 3
# Money
# 6
# Story
# 4
# Spring Time
# 5
# Bus
# 6
# Enough
#
# Изход
# Average score: 5.25
# Number of problems: 4
# Last problem: Bus

bad_marks = int(input())

task_name = input()

last_task = ""
current_bad_marks = 0
mark_sum = 0
task_count = 0

while task_name != "Enough":
    if task_name != "Enough":
        last_task = task_name
    mark = int(input())
    if mark <= 4:
        current_bad_marks += 1
        task_count +=1
        mark_sum += mark
    else:
        task_count += 1
        mark_sum += mark
    if current_bad_marks == bad_marks:
        print(f"You need a break, {current_bad_marks} poor grades.")
        break
    task_name = input()

avg_marks = mark_sum / task_count

if task_name == "Enough":
    print(f"Average score: {avg_marks:.2f}")
    print(f"Number of problems: {task_count}")
    print(f"Last problem: {last_task}")
