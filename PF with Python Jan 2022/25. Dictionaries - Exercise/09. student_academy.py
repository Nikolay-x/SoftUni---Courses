# 9. Student Academy
# Write a program that keeps the information about students and their grades.
# On the first line, you will receive an integer number representing the next pair of rows. On the next lines, you will be receiving each student's name and their grade.
# Keep track of all grades for each student and keep only the students with an average grade higher than or equal to 4.50.
# Print the final dictionary with students and their average grade in the following format:
# "{name} -> {averageGrade}"
# Format the average grade to the 2nd decimal place.
#
# Input
# 5
# John
# 5.5
# John
# 4.5
# Alice
# 6
# Alice
# 3
# George
# 5
#
# Output
# John -> 5.00
# Alice -> 4.50
# George -> 5.00

data_lines = int(input())
students_result = dict()

for i in range(data_lines):
    student_name = input()
    student_grade = float(input())

    if student_name not in students_result:
        students_result[student_name] = []
    students_result[student_name].append(student_grade)

for student_name in students_result:
    avg_grade = sum(students_result[student_name]) / len(students_result[student_name])
    if avg_grade >= 4.5:
        print(f"{student_name} -> {avg_grade:.2f}")
