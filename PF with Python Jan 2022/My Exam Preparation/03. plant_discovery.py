# Problem 3 - Plant Discovery
# Problem for exam preparation for the Programming Fundamentals Course @SoftUni.
# Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2518#2.
#
# You have now returned from your world tour. On your way, you have discovered some new plants, and you want to gather some information about them and create an exhibition to see which plant is highest rated.
# On the first line, you will receive a number n. On the next n lines, you will be given some information about the plants that you have discovered in the format: "{plant}<->{rarity}". Store that information because you will need it later. If you receive a plant more than once, update its rarity.
# After that, until you receive the command "Exhibition", you will be given some of these commands:
# "Rate: {plant} - {rating}" – add the given rating to the plant (store all ratings)
# "Update: {plant} - {new_rarity}" – update the rarity of the plant with the new one
# "Reset: {plant}" – remove all the ratings of the given plant
# Note: If any given plant name is invalid, print "error"
# After the command "Exhibition", print the information that you have about the plants in the following format:
# "Plants for the exhibition:
# - {plant_name1}; Rarity: {rarity}; Rating: {average_rating}
# - {plant_name2}; Rarity: {rarity}; Rating: {average_rating}
# …
# - {plant_nameN}; Rarity: {rarity}; Rating: {average_rating}"
# The average rating should be formatted to the second decimal place.
# Input / Constraints
# You will receive the input as described above
# JavaScript: you will receive a list of strings
# Output
# Print the information about all plants as described above
#
# Input
# 3
# Arnoldii<->4
# Woodii<->7
# Welwitschia<->2
# Rate: Woodii - 10
# Rate: Welwitschia - 7
# Rate: Arnoldii - 3
# Rate: Woodii - 5
# Update: Woodii - 5
# Reset: Arnoldii
# Exhibition
#
# Output
# Plants for the exhibition:
# - Arnoldii; Rarity: 4; Rating: 0.00
# - Woodii; Rarity: 5; Rating: 7.50
# - Welwitschia; Rarity: 2; Rating: 7.00

# n = int(input())
# plant_dict = {}
#
# for i in range(n):
#     line = input().split("<->")
#     plant = line[0]
#     rarity = int(line[1])
#
#     if plant not in plant_dict:
#         plant_dict[plant] = {"Rarity": rarity, "Rating": []}
#     else:
#         plant_dict[plant]["Rarity"] = rarity
#
# while True:
#     command = input()
#
#     if command == "Exhibition":
#         break
#
#     command = command.split(": ")
#     line = command[1].split(" - ")
#     plant = line[0]
#
#     if plant not in plant_dict:
#         print("error")
#
#     else:
#         if command[0] == "Rate":
#             rating = int(line[1])
#             plant_dict[plant]["Rating"].append(rating)
#         if command[0] == "Update":
#             new_rarity = int(line[1])
#             plant_dict[plant]["Rarity"] = new_rarity
#         if command[0] == "Reset":
#             for i in range(1, len(plant_dict[plant])):
#                 plant_dict[plant]["Rating"] = []
#
# print("Plants for the exhibition:")
# for plant in plant_dict:
#     avg_rating = 0
#
#     for i in range(len(plant_dict[plant]["Rating"])):
#         avg_rating += plant_dict[plant]["Rating"][i]
#
#     if avg_rating > 0:
#         final_rating = avg_rating / (len(plant_dict[plant]["Rating"]))
#     else:
#         final_rating = 0
#
#     print(f"- {plant}; Rarity: {plant_dict[plant]['Rarity']}; Rating: {final_rating:.2f}")


n = int(input())
plant_dict = {}

for i in range(n):
    line = input().split("<->")
    plant = line[0]
    rarity = int(line[1])

    if plant not in plant_dict:
        plant_dict[plant] = [rarity]
    else:
        plant_dict[plant][0] = rarity

while True:
    command = input()

    if command == "Exhibition":
        break

    command = command.split(": ")
    line = command[1].split(" - ")
    plant = line[0]

    if plant not in plant_dict:
        print("error")

    else:
        if command[0] == "Rate":
            rating = int(line[1])
            plant_dict[plant].append(rating)
        if command[0] == "Update":
            new_rarity = int(line[1])
            plant_dict[plant][0] = new_rarity
        if command[0] == "Reset":
            plant_dict[plant] = [plant_dict[plant][0]]

print("Plants for the exhibition:")
for plant in plant_dict:
    avg_rating = 0

    for i in range(1, len(plant_dict[plant])):
        avg_rating += plant_dict[plant][i]

    if avg_rating > 0:
        final_rating = avg_rating / (len(plant_dict[plant]) - 1)
    else:
        final_rating = 0

    print(f"- {plant}; Rarity: {plant_dict[plant][0]}; Rating: {final_rating:.2f}")
