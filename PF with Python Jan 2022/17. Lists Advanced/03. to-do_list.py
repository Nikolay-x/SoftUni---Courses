# 3.To-do List
# You will be receiving to-do notes until you get the command "End". The notes will be in the format: "{importance}-{note}".
# Return a list containing all to-do notes sorted by importance in ascending order.
# The importance value will always be an integer between 1 and 10 (inclusive).
# Hint
# Use the pop() and insert() methods.
#
# Input
# 2-Walk the dog
# 1-Drink coffee
# 6-Dinner
# 5-Work
# End
#
# Output
# ['Drink coffee', 'Walk the dog', 'Work', 'Dinner']

to_do_list = [0 for i in range(11)]
command = input()

to_do_list_notes = []

while command != "End":
    current_command = command.split("-")
    for i in range(len(to_do_list)):
        if i == int(current_command[0]):
            to_do_list[i] = current_command[1]
    command = input()

for note in to_do_list:
    if note != 0:
        to_do_list_notes.append(note)

print(to_do_list_notes)

# command = input()
#
# while command != "End":
#     explode = command.split("-")
#     priority = int(explode[0])
#     task = explode[1]
#     to_do_list[priority] = task
#     command = input()
#
# final_to_do = [task for task in to_do_list if task != 0]
#
# print(final_to_do)
