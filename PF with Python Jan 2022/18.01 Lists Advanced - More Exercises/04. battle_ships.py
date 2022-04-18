# 4.Battle Ships
# You will be given a number n representing the number of rows of the field. On the following n lines, you will receive each field row as a string with numbers separated by a space. Each number greater than zero represents a ship with health equal to the number value.
# After that, you will receive the squares that are being attacked in the format: "{row}-{col} {row}-{col}". Each time a square is being attacked, if there is a ship (number greater than 0), you should reduce its value by 1. If a ship's health reaches zero, it is destroyed. After the attacks have ended, print how many ships were destroyed.
#
# Input
# 3
# 1
# 0
# 0
# 1
# 2
# 0
# 0
# 0
# 0
# 3
# 0
# 1
# 0 - 0
# 1 - 0
# 2 - 1
# 2 - 1
# 2 - 1
# 1 - 1
# 2 - 1
#
# Output
# 2

n = int(input())

battlefield = []
destroyed_ships = 0

for i in range(n):
    temp_list = list(map(int, input().split(" ")))
    battlefield.append(temp_list)

attacks = list(map(str, input().split(" ")))

for attack in attacks:
    current_attack = list(map(int, attack.split("-")))
    row = current_attack[0]
    col = current_attack[1]
    battlefield[row][col] -= 1
    if battlefield[row][col] == 0:
        destroyed_ships += 1

print(destroyed_ships)
