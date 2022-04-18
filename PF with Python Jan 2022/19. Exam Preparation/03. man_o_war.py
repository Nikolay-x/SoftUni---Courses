# Problem 3 - Man-O-War
# Problem for exam preparation for the Programming Fundamentals Course @SoftUni.
# Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/1773#2.
#
# The pirates encounter a huge Man-O-War at sea.
# Create a program that tracks the battle and either chooses a winner or prints a stalemate. On the first line, you will receive the status of the pirate ship, which is a string representing integer sections separated by ">". On the second line, you will receive the same type of status, but for the warship:
# "{section1}>{section2}>{section3}… {sectionn}"
# On the third line, you will receive the maximum health capacity a section of the ship can reach.
# The following lines represent commands until "Retire":
# "Fire {index} {damage}" - the pirate ship attacks the warship with the given damage at that section. Check if the index is valid and if not, skip the command. If the section breaks (health <= 0) the warship sinks, print the following and stop the program: "You won! The enemy ship has sunken."
# "Defend {startIndex} {endIndex} {damage}" - the warship attacks the pirate ship with the given damage at that range (indexes are inclusive). Check if both indexes are valid and if not, skip the command. If the section breaks (health <= 0) the pirate ship sinks, print the following and stop the program:
# "You lost! The pirate ship has sunken."
# "Repair {index} {health}" - the crew repairs a section of the pirate ship with the given health. Check if the index is valid and if not, skip the command. The health of the section cannot exceed the maximum health capacity.
# "Status" - prints the count of all sections of the pirate ship that need repair soon, which are all sections that are lower than 20% of the maximum health capacity. Print the following:
# "{count} sections need repair."
# In the end, if a stalemate occurs, print the status of both ships, which is the sum of their individual sections, in the following format:
# "Pirate ship status: {pirateShipSum}
# Warship status: {warshipSum}"
# Input
# On the 1st line, you are going to receive the status of the pirate ship (integers separated by '>')
# On the 2nd line, you are going to receive the status of the warship
# On the 3rd line, you will receive the maximum health a section of a ship can reach.
# On the following lines, until "Retire", you will be receiving commands.
# Output
# Print the output in the format described above.
# Constraints
# The section numbers will be integers in the range [1….1000]
# The indexes will be integers [-200….200]
# The damage will be an integer in the range [1….1000]
# The health will be an integer in the range [1….1000]
#
# Input
# 12>13>11>20>66
# 12>22>33>44>55>32>18
# 70
# Fire 2 11
# Fire 8 100
# Defend 3 6 11
# Defend 0 3 5
# Repair 1 33
# Status
# Retire
#
# Output
# 2 sections need repair.
# Pirate ship status: 135
# Warship status: 205

pirate_ship = list(map(int, input().split(">")))
man_o_war = list(map(int, input().split(">")))
maximum_health = int(input())

line = input()
stalemate = True
pirate_ship_sum = 0
man_o_war_sum = 0

while line != "Retire":
    if "Fire" in line:
        l = line.split(" ")
        index = int(l[1])
        damage = int(l[2])
        if 0 <= index < len(man_o_war):
            man_o_war[index] -= damage
            if man_o_war[index] <= 0:
                print(f"You won! The enemy ship has sunken.")
                stalemate = False
                break
    if "Defend" in line:
        l = line.split(" ")
        startindex = int(l[1])
        endindex = int(l[2])
        damage = int(l[3])
        if 0 <= startindex < len(pirate_ship) and 0 <= endindex < len(pirate_ship):
            for i in range(startindex, endindex +1):
                pirate_ship[i] -= damage
                if pirate_ship[i] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    stalemate = False
                    break
    if "Repair" in line:
        l = line.split(" ")
        index = int(l[1])
        health = int(l[2])
        if 0 <= index < len(pirate_ship):
            pirate_ship[index] += health
            if pirate_ship[index] > maximum_health:
                pirate_ship[index] = maximum_health
    if "Status" in line:
        count = 0
        for section in pirate_ship:
            if section < maximum_health * 0.2:
                count += 1
        print(f"{count} sections need repair.")

    line = input()
    if not stalemate:
        break

if stalemate:
    for section in pirate_ship:
        pirate_ship_sum += section
    for section in man_o_war:
        man_o_war_sum += section
    print(f"Pirate ship status: {pirate_ship_sum}")
    print(f"Warship status: {man_o_war_sum}")
