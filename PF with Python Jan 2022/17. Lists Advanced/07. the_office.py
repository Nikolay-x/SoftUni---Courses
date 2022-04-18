# 7.The Office
# You will receive two lines of input:
# a list of employees' happiness as a string of numbers separated by a single space
# a happiness improvement factor (single number).
# Your task is to find out if the employees are generally happy in their office.
# First, multiply each employee's happiness by the factor.
# Then, print one of the following lines:
# If half or more of the employees have happiness greater than or equal to the average:
# "Score: {happy_count}/{total_count}. Employees are happy!"
# Otherwise:
# "Score: {happy_count}/{total_count}. Employees are not happy!"
#
# Input
# 1 2 3 4 2 1
# 3
#
# Output
# Score: 2/6. Employees are not happy!

employees_happiness = list(map(int, input().split(" ")))
happiness_factor = int(input())

factored_employees_happiness = list()
employee_count = 0

for employee_happiness in employees_happiness:
    factored_employees_happiness.append(employee_happiness * happiness_factor)

average_happiness = sum(factored_employees_happiness) / len(factored_employees_happiness)

for current_happiness in factored_employees_happiness:
    if current_happiness >= average_happiness:
        employee_count += 1

if employee_count >= len(factored_employees_happiness) / 2:
    print(f"Score: {employee_count}/{len(factored_employees_happiness)}. Employees are happy!")
else:
    print(f"Score: {employee_count}/{len(factored_employees_happiness)}. Employees are not happy!")
