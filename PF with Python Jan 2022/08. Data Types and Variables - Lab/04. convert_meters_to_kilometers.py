# 4.Convert Meters to Kilometers
# You will be given an integer that represents a distance in meters. Write a program that converts meters to kilometers formatted to the second decimal point.
#
# Input
# 1852
#
# Output
# 1.85

meters = int(input())

kilometers = meters / 1000

print(f"{kilometers:.2f}")
