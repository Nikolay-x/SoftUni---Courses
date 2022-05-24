# 4.Water Dispenser
# Write a program that keeps track of people getting water from a dispenser and the amount of water left at the end.
# On the first line, you will receive the starting quantity of water (integer) in a dispenser. Then, on the following lines, you will be given the names of some people who want to get water (each on a separate line) until you receive the command "Start". Add those people in a queue. Finally, you will receive some commands until the command "End":
# -"{liters}" - litters (integer) that the current person in the queue wants to get. Check if there is enough water in the dispenser for that person.
# oIf there is enough water, print "{person_name} got water" and remove him/her from the queue.
# oOtherwise, print "{person_name} must wait" and remove the person from the queue without reducing the water in the dispenser.
# -"refill {liters}" - add the given litters in the dispenser.
# In the end, print how many liters of water have left in the format: "{left_liters} liters left".
#
# Input
# 2
# Peter
# Amy
# Start
# 2
# refill 1
# 1
# End
#
# Output
# Peter got water
# Amy got water
# 0 liters left

from collections import deque

water_quantity = int(input())
q = deque()

while True:
    name = input()
    if name == "Start":
        break
    q.append(name)

while True:
    command = input()
    if command == "End":
        break
    if "refill" in command:
        command = command.split(" ")
        liters = int(command[1])
        water_quantity += liters
    else:
        liters = int(command)
        name = q.popleft()
        if liters <= water_quantity:
            water_quantity -= liters
            print(f"{name} got water")
        else:
            print(f"{name} must wait")

print(f"{water_quantity} liters left")
