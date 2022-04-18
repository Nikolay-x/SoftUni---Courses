# 01. SoftUni Reception
# Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2474#0.
# Every day, thousands of students pass by the reception at SoftUni with different questions to ask. The employees have to help everyone by providing all the information and answering all of the questions.
# Three employees are working on the reception all day. Each of them can handle a different number of students per hour. Your task is to calculate how much time it will take to answer all the questions of a given number of students.
# First, you will receive 3 lines with integers, representing the number of students that each employee can help per hour. On the following line, you will receive students count as a single integer.
# Every fourth hour, all employees have a break, so they don't work for an hour. It is the only break for the employees, because they don't need rest, nor have a personal life. Calculate the time needed to answer all the student's questions and print it in the following format: "Time needed: {time}h."
# Input / Constraints
# On the first three lines -  each employee efficiency -  integer in the range [1 - 100]
# On the fourth line - students count – integer in the range [0 – 10000]
# Input will always be valid and in the range specified
# Output
# Print a single line: "Time needed: {time}h."
# Allowed working time / memory: 100ms / 16MB
#
# Input
# 5
# 6
# 4
# 20
#
# Output
# Time needed: 2h.

employee1_capacity = int(input())
employee2_capacity = int(input())
employee3_capacity = int(input())
total_students = int(input())

time_needed = 0

while total_students > 0:
    time_needed += 1
    if time_needed % 4 != 0:
        total_students -= employee1_capacity + employee2_capacity + employee3_capacity

print(f"Time needed: {time_needed}h.")
