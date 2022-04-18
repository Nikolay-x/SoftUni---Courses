# 7.Water Overflow
# You have a water tank with a capacity of 255 liters. On the first line, you will receive n – the number of lines, which will follow. On the following n lines, you will receive liters of water (integers), which you should pour into your tank. If the capacity is not enough, print "Insufficient capacity!" and continue reading the next line. On the last line, print the liters in the tank.
#
# Input
# 5
# 20
# 100
# 100
# 100
# 20
#
# Output
# Insufficient capacity!
# 240

n = int(input())

total_liters = 0

for i in range(n):
    liters = int(input())
    total_liters += liters

    if total_liters > 255:
        print(f"Insufficient capacity!")
        total_liters -= liters

print(total_liters)
