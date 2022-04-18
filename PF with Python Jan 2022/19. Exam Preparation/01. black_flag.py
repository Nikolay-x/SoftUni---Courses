# Problem 1 - Black Flag
# Problem for exam preparation for the Programming Fundamentals Course @SoftUni.
# Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/1773#0.
#
# Pirates are invading the sea, and you're tasked to help them plunder
# Create a program that checks if target plunder is reached. First, you will receive how many days the pirating lasts. Then you will receive how much the pirates plunder for a day. Last you will receive the expected plunder at the end.
# Calculate how much plunder the pirates manage to gather. Each day they gather the plunder. Keep in mind that they attack more ships every third day and add additional plunder to their total gain, which is 50% of the daily plunder. Every fifth day the pirates encounter a warship, and after the battle, they lose 30% of their total plunder.
# If the gained plunder is more or equal to the target, print the following:
# "Ahoy! {totalPlunder} plunder gained."
# If the gained plunder is less than the target. Calculate the percentage left and print the following:
# "Collected only {percentage}% of the plunder."
# Both numbers should be formatted to the 2nd decimal place.
# Input
# On the 1st line, you will receive the days of the plunder – an integer number in the range [0…100000]
# On the 2nd line, you will receive the daily plunder – an integer number in the range [0…50]
# On the 3rd line, you will receive the expected plunder – a real number in the range [0.0…10000.0]
# Output
#  In the end, print whether the plunder was successful or not, following the format described above.
#
# Input
# 5
# 40
# 100
#
# Output
# Ahoy! 154.00 plunder gained.

days_to_plunder = int(input())
daily_plunder = int(input())
expected_plunder = float(input())

total_plunder = 0

for i in range(1, days_to_plunder +1):
    total_plunder += daily_plunder
    if i % 3 == 0:
        total_plunder += daily_plunder * 0.5
    if i % 5 == 0:
        total_plunder -= total_plunder * 0.3

if total_plunder >= expected_plunder:
    print(f"Ahoy! {total_plunder:.2f} plunder gained.")
else:
    print(f"Collected only {((total_plunder / expected_plunder) * 100):.2f}% of the plunder.")
