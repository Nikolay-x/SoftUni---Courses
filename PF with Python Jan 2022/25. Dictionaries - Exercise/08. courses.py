# 8.Courses
# Write a program that keeps the information about courses. Each course has a name and registered students.
# You will be receiving a course name and a student name until you receive the command "end".
# You should register each user into the corresponding course. If the given course does not exist, add it.
# When you receive the command "end", print the courses with their names and total registered users. For each course, print the registered users.
# Input
# Until the "end" command is received, you will be receiving input lines in the format:
# "{course_name} : {student_name}"
# The product data is always delimited by " : "
# Output
# Print the information about each course in the following format:
# "{course_name}: {registered_students}"
# Print the information about each student in the following format:
# "-- {student_name}"
#
# Input
# Programming Fundamentals : John Smith
# Programming Fundamentals : Linda Johnson
# JS Core : Will Wilson
# Java Advanced : Harrison White
# end
#
# Output
# Programming Fundamentals: 2
# -- John Smith
# -- Linda Johnson
# JS Core: 1
# -- Will Wilson
# Java Advanced: 1
# -- Harrison White

courses_dict = dict()

while True:
    line = input()
    if line == "end":
        break
    line = line.split(" : ")
    course = line[0]
    student_name = line[1]
    if course not in courses_dict:
        courses_dict[course] = []
    courses_dict[course].append(student_name)

for course in courses_dict:
    print(f"{course}: {len(courses_dict[course])}")
    for name in courses_dict[course]:
        print(f"-- {name}")
