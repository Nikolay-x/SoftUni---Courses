# 10.* Gladiator Expenses
# As a gladiator, Peter needs to repair his broken equipment when he loses a fight. His equipment consists of a helmet, a sword, a shield, and an armor.
# You will receive Peter's lost fights count.
# Every second lost game, his helmet is broken.
# Every third lost game, his sword is broken.
# When both his sword and helmet are broken in the same lost fight, his shield also breaks.
# Every second time his shield brakes, his armor also needs to be repaired.
# You will receive the price of each item in his equipment. Calculate his expenses for the year for renewing his equipment.
# Input / Constraints
# The input will consist of 5 lines:
# On the first line, you will receive the lost fights count – an integer in the range [0, 1000].
# On the second line, you will receive the helmet price - a floating-point number in the range [0, 1000].
# On the third line, you will receive the sword price - a floating-point number in the range [0, 1000].
# On the fourth line, you will receive the shield price - a floating-point number in the range [0, 1000].
# On the fifth line, you will receive the armor price - a floating-point number in the range [0, 1000].
# Output
# As output, you must print Peter`s total expenses for new equipment: "Gladiator expenses: {expenses} aureus"
#
# Input
# 7
# 2
# 3
# 4
# 5
#
# Output
# Gladiator expenses: 16.00 aureus

lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

expenses = 0
shield_repairs_count = 0

for i in range(1, lost_fights +1):
    if i % 2 == 0:
        expenses += helmet_price
    if i % 3 == 0:
        expenses += sword_price
    if i % 2 == 0 and i % 3 == 0:
        expenses += shield_price
        shield_repairs_count += 1
        if shield_repairs_count == 2:
            expenses += armor_price
            shield_repairs_count = 0

print(f"Gladiator expenses: {expenses:.2f} aureus")
