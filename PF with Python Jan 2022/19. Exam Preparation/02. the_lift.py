# Problem 2 - The Lift
# Problem for exam preparation for the Programming Fundamentals Course @SoftUni.
# Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2517#1.
#
# Write a program that finds a place for the tourist on a lift. 
# Every wagon should have a maximum of 4 people on it. If a wagon is full, you should direct the people to the next one with space available.
# Input
# On the first line, you will receive how many people are waiting to get on the lift
# On the second line, you will receive the current state of the lift separated by a single space: " ".
# Output
# When there is no more available space left on the lift, or there are no more people in the queue, you should print on the console the final state of the lift's wagons separated by " " and one of the following messages:
# If there are no more people and the lift have empty spots, you should print:
# "The lift has empty spots!
# {wagons separated by ' '}"
# If there are still people in the queue and no more available space, you should print:
# "There isn't enough space! {people} people in a queue!
# {wagons separated by ' '}"
# If the lift is full and there are no more people in the queue, you should print only the wagons separated by " "
#
# Input
# 15
# 0 0 0 0
#
# Output
# The lift has empty spots!
# 4 4 4 3

people_count = int(input())
str_lift_status = input().split(" ")

lift_status = list(map(int, str_lift_status))
final_lift_status = []
add_part = []
lift_full = False

for current_wagon in lift_status:
    if current_wagon < 4:
        if people_count > 0:
            if people_count < 4 - current_wagon:
                final_lift_status.append(current_wagon + people_count)
                people_count = 0
            elif people_count >= 4 - current_wagon:
                final_lift_status.append(4)
                people_count -= 4 - current_wagon
        elif people_count == 0:
            break
    elif current_wagon == 4:
        final_lift_status.append(4)

    if len(final_lift_status) == len(lift_status) and list(set(final_lift_status)) == [4]:
        lift_full = True
        break

if len(final_lift_status) < len(lift_status):
    for i in range(len(lift_status) - len(final_lift_status)):
        add_part.append(lift_status[-1-i])

add_part.reverse()
final_lift_status += add_part

final_lift_status = list(map(str, final_lift_status))

if lift_full == True and people_count > 0:
    print(f"There isn't enough space! {people_count} people in a queue!")
    print(" ".join(final_lift_status))
if lift_full == False and people_count == 0:
    print("The lift has empty spots!")
    print(" ".join(final_lift_status))
if lift_full == True and people_count == 0:
    print(" ".join(final_lift_status))
