# Bombs
#
# Ezio is still learning how to make bombs. With their help, he will save civilization. We should help Ezio to make his perfect bombs.
#
# You will be given two sequences of integers, representing bomb effects and bomb casings.
# You need to start from the first bomb effect and try to mix it with the last bomb casing. If the sum of their values is equal to any of the materials in the table below – create the bomb corresponding to the value and remove both bomb materials. Otherwise, just decrease the value of the bomb casing by 5. You need to stop combining when you have no more bomb effects or bomb casings, or you successfully filled the bombs pouch.
# Bombs:
# Datura Bombs: 40
# Cherry Bombs: 60
# Smoke Decoy Bombs: 120
# To fill the bomb pouch, Ezio needs three of each of the bomb types.
# Input
# On the first line, you will receive the integers representing the bomb effects, separated by ", ".
# On the second line, you will receive the integers representing the bomb casings, separated by ", ".
# Output
# On the first line, print:
# oif Ezio succeeded to fulfill the bomb pouch: "Bene! You have successfully filled the bomb pouch!"
# oif Ezio didn't succeed to fulfill the bomb pouch: "You don't have enough materials to fill the bomb pouch."
# On the second line, print all bomb effects left:
# oIf there are no bomb effects: "Bomb Effects: empty"
# oIf there are effects: "Bomb Effects: {bombEffect1}, {bombEffect2}, (…)"
# On the third line, print all bomb casings left:
# oIf there are no bomb casings: "Bomb Casings: empty"
# oIf there are casings: "Bomb Casings: {bombCasing1}, {bombCasing2}, (…)"
# Then, you need to print all bombs and the count you have of them, ordered alphabetically:
# o"Cherry Bombs: {count}"
# o"Datura Bombs: {count}"
# o"Smoke Decoy Bombs: {count}"
# Constraints
# All of the given numbers will be valid integers in the range [0, 120].
# There will be no cases with negative material.
#
# Input
# 5, 25, 25, 115
# 5, 15, 25, 35
#
# Output
# You don't have enough materials to fill the bomb pouch.
# Bomb Effects: empty
# Bomb Casings: empty
# Cherry Bombs: 0
# Datura Bombs: 3
# Smoke Decoy Bombs: 1

from collections import deque

bombs_effects = deque([int(x) for x in input().split(", ")])
bombs_casings = [int(x) for x in input().split(", ")]

bombs_dict = {
    "Datura Bombs": 40,
    "Cherry Bombs": 60,
    "Smoke Decoy Bombs": 120
}

crafted_bombs = {
    "Datura Bombs": 0,
    "Cherry Bombs": 0,
    "Smoke Decoy Bombs": 0
}
bombs_are_crafted = False

while bombs_effects and bombs_casings:
    bomb_effect = bombs_effects.popleft()
    bomb_casing = bombs_casings.pop()
    total_sum = bomb_effect + bomb_casing

    if total_sum == 40:
        crafted_bombs["Datura Bombs"] += 1
    elif total_sum == 60:
        crafted_bombs["Cherry Bombs"] += 1
    elif total_sum == 120:
        crafted_bombs["Smoke Decoy Bombs"] += 1
    else:
        bomb_casing -= 5
        bombs_effects.appendleft(bomb_effect)
        bombs_casings.append(bomb_casing)

    if crafted_bombs["Datura Bombs"] >= 3 \
            and crafted_bombs["Cherry Bombs"] >= 3 \
            and crafted_bombs["Smoke Decoy Bombs"] >= 3:
        bombs_are_crafted = True
        break

if bombs_are_crafted:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")
if bombs_effects:
    print(f"Bomb Effects: {', '.join([str(x) for x in bombs_effects])}")
else:
    print("Bomb Effects: empty")
if bombs_casings:
    print(f"Bomb Casings: {', '.join([str(x) for x in bombs_casings])}")
else:
    print("Bomb Casings: empty")

print(f'Cherry Bombs: {crafted_bombs["Cherry Bombs"]}')
print(f'Datura Bombs: {crafted_bombs["Datura Bombs"]}')
print(f'Smoke Decoy Bombs: {crafted_bombs["Smoke Decoy Bombs"]}')
