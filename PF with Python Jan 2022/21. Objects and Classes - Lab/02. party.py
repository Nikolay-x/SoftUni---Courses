# 2.Party
# Create a class Party that only has an attribute people – empty list. The __init__ method should not accept any parameters. You will be given names of people (on separate lines) until you receive the command "End". Use the created class to solve this problem. After you receive the "End" command, print 2 lines:
# "Going: {people}" - the people should be separated by comma and space ", ".
# "Total: {total_people_going}"
# Note: submit all of your code, including the class
#
# Input
# Peter
# John
# Katy
# End
#
# Output
# Going: Peter, John, Katy
# Total: 3

class Party:
    def __init__(self):
        self.people = []


party = Party()
line = input()
while line != "End":
    party.people.append(line)
    line = input()

print(f'Going: {", ".join(party.people)}')
print(f"Total: {len(party.people)}")
