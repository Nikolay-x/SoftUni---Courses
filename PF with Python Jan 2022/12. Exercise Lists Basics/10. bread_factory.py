# 10.* Bread Factory
# As a young baker, you are baking the bread out of the bakery.
# You have initial energy 100 and initial coins 100. You will be given a string representing the working day events. Each event is separated with '|' (vertical bar): "event1|event2| … eventN"
# Each event contains an event name or an ingredient and a number, separated by a dash ("{event/ingredient}-{number}")
# If the event is "rest":
# oYou gain energy (the number in the second part). Note: your energy cannot exceed your initial energy (100). Print: "You gained {gained_energy} energy.".
# oAfter that, print your current energy: "Current energy: {current_energy}.".
# If the event is "order":
# oYou've earned some coins (the number in the second part).
# oEach time you get an order, your energy decreases by 30 points.
# If you have the energy to complete the order, print: "You earned {earned} coins.".
# Otherwise, skip the order and gain 50 energy points. Print: "You had to rest!".
# In any other case, you have an ingredient you should buy. The second part of the event contains the coins you should spend.
# oIf you have enough money, you should buy the ingredient and print:
# "You bought {ingredient}."
# oOtherwise, print "Closed! Cannot afford {ingredient}." and your bakery rush is over.
# If you managed to handle all events through the day, print on the following 3 lines:
# "Day completed!"
# "Coins: {coins}"
# "Energy: {energy}"
# Input / Constraints
# You will receive a string representing the working day events, separated with '|' (vertical bar) in the format:
# "event1|event2| … eventN".
# Each event contains an event name or an ingredient and a number, separated by a dash in the format: "{event/ingredient}-{number}"
# Output
# Print the corresponding messages described above.
#
# Input
# rest-2|order-10|eggs-100|rest-10
#
# Output
# You gained 0 energy.
# Current energy: 100.
# You earned 10 coins.
# You bought eggs.
# You gained 10 energy.
# Current energy: 80.
# Day completed!
# Coins: 10
# Energy: 80

event_list = input().split("|")
energy = 100
coins = 100

complpeted_day = True

for i in event_list:
    event = i.split("-")
    event_type = event[0]
    event_value = int(event[1])

    if event_type == "rest":
        if energy + event_value <= 100:
            energy += event_value
            print(f"You gained {event_value} energy.")
        else:
            gained_energy = 100 - energy
            energy = 100
            print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {energy}.")

    elif event_type == "order":
        if energy - 30 >= 0:
            energy -= 30
            coins += event_value
            print(f"You earned {event_value} coins.")
        else:
            if energy + 50 <= 100:
                energy += 50
            else:
                energy = 100
            print("You had to rest!")

    else:
        if coins >= event_value:
            coins -= event_value
            print(f"You bought {event_type}.")
        else:
            print(f"Closed! Cannot afford {event_type}.")
            complpeted_day = False
            break

if complpeted_day:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
