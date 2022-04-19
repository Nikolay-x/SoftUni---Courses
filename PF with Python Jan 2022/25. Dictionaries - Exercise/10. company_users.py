# 10.Company Users
# Write a program that keeps the information about companies and their employees.
# You will be receiving company names and an employees' id until you receive the command "End" command. Add each employee to the given company. Keep in mind that a company cannot have two employees with the same id.
# Print the company name and each employee's id in the following format:
# "{company_name}
# -- {id1}
# -- {id2}
# …
# -- {idN}"
# Input / Constraints
# Until you receive the "End" command, you will be receiving input in the format:
# "{company_name} -> {employee_id}".
# The input always will be valid.
#
# Input
# SoftUni -> AA12345
# SoftUni -> BB12345
# Microsoft -> CC12345
# HP -> BB12345
# End
#
# Output
# SoftUni
# -- AA12345
# -- BB12345
# Microsoft
# -- CC12345
# HP
# -- BB12345

company_dict = dict()

while True:
    command = input()
    if command == "End":
        break
    command = command.split(" -> ")
    company_name = command[0]
    employee_id = command[1]
    if company_name not in company_dict:
        company_dict[company_name] = []
    if employee_id not in company_dict[company_name]:
        company_dict[company_name].append(employee_id)

for company in company_dict:
    print(f"{company}")
    for employee in company_dict[company]:
        print(f"-- {employee}")
