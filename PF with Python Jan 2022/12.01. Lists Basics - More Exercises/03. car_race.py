# 3.Car Race
# Write a program that announces the winner of a car race.
# You will receive a sequence of numbers. Each number represents the time needed for the car to pass through that step (the index). There will be two cars. The first one starts from the left side, and the other one starts from the right side. The middle index of the sequence is the finish line.
# Calculate the total time each racer needs to reach the finish line and print the winner with his total time (the racer with less time). If you have a zero in the list, you should reduce the racer's time that reached it by 20% (from his current time).
# The number of elements in the sequence will always be odd.
# Print the result in the following format "The winner is {left/right} with total time: {total_time}".
# The time should be formatted to the first decimal point.
#
# Input
# 29 13 9 0 13 0 21 0 14 82 12
#
# Output
# The winner is left with total time: 53.8

string_check_points = input().split(" ")

check_points = list(map(int, string_check_points))
left_racer = 0
right_racer = 0

for t in range(len(check_points) // 2):
    if check_points[t] != 0:
        left_racer += check_points[t]
    else:
        left_racer = left_racer * 0.8

for t1 in range(len(check_points) - 1, len(check_points) // 2, -1):
    if check_points[t1] != 0:
        right_racer += check_points[t1]
    else:
        right_racer = right_racer * 0.8

if left_racer < right_racer:
    print(f"The winner is left with total time: {left_racer:.1f}")
else:
    print(f"The winner is right with total time: {right_racer:.1f}")
