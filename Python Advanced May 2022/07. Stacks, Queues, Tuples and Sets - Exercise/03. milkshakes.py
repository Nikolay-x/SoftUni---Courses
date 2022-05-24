# 3.Milkshakes
# You are learning how to make milkshakes.
# First, you will be given two sequences of integers representing chocolates and cups of milk.
# You have to start from the last chocolate and try to match it with the first cup of milk. If their values are equal, you should make a milkshake and remove both ingredients. Otherwise, you should move the cup of milk at the end of the sequence and decrease the value of the chocolate by 5 without moving it from its position.
# If any of the values are equal to or below 0, you should remove them from the records right before mixing them with the other ingredient.
# When you successfully prepare 5 chocolate milkshakes, or you have no more chocolate or cups of milk left, you need to stop making chocolate milkshakes.
# Input
# On the first line of input, you will receive the integers representing the chocolate, separated by  ", ".
# On the second line of input, you will receive the integers representing the cups of milk, separated by ", ".
# Output
# On the first line, print:
# oIf you successfully made 5 milkshakes: "Great! You made all the chocolate milkshakes needed!"
# oOtherwise: "Not enough milkshakes."
# On the second line - print:
# oIf there are chocolates left: "Chocolate: {chocolate1}, {chocolate2}, (…)"
# oOtherwise: "Chocolate: empty"
# On the third line - print:
# oIf there are cups of milk left: "Milk: {milk1}, {milk2}, {milk3}, (…)"
# oOtherwise: "Milk: empty"
# Constraints
# All given numbers will be valid integers in the range [-100 … 100].
#
# Input
# 20, 24, -5, 17, 22, 60, 26
# 26, 60, 22, 17, 24, 10, 55
#
# Output
# Great! You made all the chocolate milkshakes needed!
# Chocolate: 20
# Milk: 10, 55

from collections import deque

chocolates = [int(x) for x in input().split(", ")]
milk_cups = deque(int(x) for x in input().split(", "))

milkshakes = 0

while chocolates and milk_cups and milkshakes < 5:
    current_chocolate = chocolates.pop()
    current_milk_cup = milk_cups.popleft()

    if current_chocolate <= 0 and current_milk_cup <= 0:
        continue

    if current_chocolate <= 0:
        milk_cups.appendleft(current_milk_cup)
        continue

    if current_milk_cup <= 0:
        chocolates.append(current_chocolate)
        continue

    if current_chocolate == current_milk_cup:
        milkshakes += 1
    elif current_chocolate != current_milk_cup:
        milk_cups.append(current_milk_cup)
        chocolates.append(current_chocolate - 5)

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if chocolates:
    print(f"Chocolate: {', '.join(str(x) for x in chocolates)}")
else:
    print("Chocolate: empty")
if milk_cups:
    print(f"Milk: {', '.join(str(x) for x in milk_cups)}")
else:
    print("Milk: empty")
