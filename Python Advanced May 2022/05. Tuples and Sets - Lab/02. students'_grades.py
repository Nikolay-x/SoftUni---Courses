# 2.Students' Grades
# Write a program that reads students' names and their grades and adds them to the student record.
# On the first line, you will receive the number of students – N. On the following N lines, you will be receiving a student's name and their grade.
# For each student print all his/her grades and finally his/her average grade, formatted to the second decimal point in the format: "{student's name} -> {grade1} {grade2} ... {gradeN} (avg: {average_grade})".
# The order in which we print the result does not matter.
#
# Input
# 7
# Peter 5.20
# Mark 5.50
# Peter 3.20
# Mark 2.50
# Alex 2.00
# Mark 3.46
# Alex 3.00
#
# Output
# Mark -> 5.50 2.50 3.46 (avg: 3.82)
# Peter -> 5.20 3.20 (avg: 4.20)
# Alex -> 2.00 3.00 (avg: 2.50)

def avg_grade(marks):
    return f"{(sum(marks) / len(marks)):.2f}"


students_number = int(input())
students_book = dict()

for _ in range(students_number):
    line = tuple(input(). split(" "))
    student, grade = line
    if student not in students_book:
        students_book[student] = []
    students_book[student].append(float(grade))

for student, grades in students_book.items():
    output_grades = " ".join(f'{grade:.2f}' for grade in grades)
    print(f"{student} -> {output_grades} (avg: {avg_grade(grades)})")
