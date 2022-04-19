# 4.Students
# You will be receiving names of students, their ID, and a course of programming they have taken in the format "{name}:{ID}:{course}". On the last line, you will receive a name of a course in snake case lowercase letters. You should print only the information of the students who have taken the corresponding course in the format: "{name} - {ID}" on separate lines.
# Note: each student's ID will always be unique
#
# Input
# Peter:123:programming basics
# John:5622:fundamentals
# Maya:89:fundamentals
# Lilly:633:fundamentals
# fundamentals
#
# Output
# John - 5622
# Maya - 89
# Lilly - 633

data = input()
students = dict()

while ":" in data:

    data = data.split(":")
    name = data[0]
    student_id = data[1]
    course = data[2]

    # (name, student_id, course) = data.split(":")

    if course not in students:
        students[course] = dict()
    students[course][student_id] = name
    data = input()

searched_course = data
if "_" in searched_course:
    searched_course_list = searched_course.split("_")
    searched_course = " ".join(searched_course_list)

# searched_course = data.replace("_", " ")

if searched_course in students:
    for student_id in students[searched_course]:
        print(f"{students[searched_course][student_id]} - {student_id}")
