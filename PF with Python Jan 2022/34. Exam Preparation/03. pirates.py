# 03. P!rates
# Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2302#2.
#
# Anno 1681. The Caribbean. The golden age of piracy. You are a well-known pirate captain by the name of Jack Daniels. Together with your comrades Jim (Beam) and Johnny (Walker), you have been roaming the seas, looking for gold and treasure… and the occasional killing, of course. Go ahead, target some wealthy settlements and show them the pirate's way!
# Until the "Sail" command is given, you will be receiving:
# You and your crew have targeted cities, with their population and gold, separated by "||".
# If you receive a city that has already been received, you have to increase the population and gold with the given values.
# After the "Sail" command, you will start receiving lines of text representing events until the "End" command is given.
# Events will be in the following format:
# "Plunder=>{town}=>{people}=>{gold}"
# oYou have successfully attacked and plundered the town, killing the given number of people and stealing the respective amount of gold.
# oFor every town you attack print this message: "{town} plundered! {gold} gold stolen, {people} citizens killed."
# oIf any of those two values (population or gold) reaches zero, the town is disbanded.
# You need to remove it from your collection of targeted cities and print the following message: "{town} has been wiped off the map!"
# oThere will be no case of receiving more people or gold than there is in the city.
# "Prosper=>{town}=>{gold}"
# oThere has been dramatic economic growth in the given city, increasing its treasury by the given amount of gold.
# oThe gold amount can be a negative number, so be careful. If a negative amount of gold is given, print: "Gold added cannot be a negative number!" and ignore the command.
# oIf the given gold is a valid amount, increase the town's gold reserves by the respective amount and print the following message:
# "{gold added} gold added to the city treasury. {town} now has {total gold} gold."
# Input
# On the first lines, until the "Sail" command, you will be receiving strings representing the cities with their gold and population, separated by "||"
# On the following lines, until the "End" command, you will be receiving strings representing the actions described above, separated by "=>"
# Output
# After receiving the "End" command, if there are any existing settlements on your list of targets, you need to print all of them, in the following format:
# "Ahoy, Captain! There are {count} wealthy settlements to go to:
# {town1} -> Population: {people} citizens, Gold: {gold} kg
# {town2} -> Population: {people} citizens, Gold: {gold} kg
#    …
# {town…n} -> Population: {people} citizens, Gold: {gold} kg"
# If there are no settlements left to plunder, print:
# "Ahoy, Captain! All targets have been plundered and destroyed!"
# Constraints
# The initial population and gold of the settlements will be valid 32-bit integers, never negative, or exceed the respective limits.
# The town names in the events will always be valid towns that should be on your list.
#
# Input
# Tortuga||345000||1250
# Santo Domingo||240000||630
# Havana||410000||1100
# Sail
# Plunder=>Tortuga=>75000=>380
# Prosper=>Santo Domingo=>180
# End
#
# Output
# Tortuga plundered! 380 gold stolen, 75000 citizens killed.
# 180 gold added to the city treasury. Santo Domingo now has 810 gold.
# Ahoy, Captain! There are 3 wealthy settlements to go to:
# Tortuga -> Population: 270000 citizens, Gold: 870 kg
# Santo Domingo -> Population: 240000 citizens, Gold: 810 kg
# Havana -> Population: 410000 citizens, Gold: 1100 kg

cities_dict = dict()

while True:
    fill_in_data = input().split("||")
    if fill_in_data[0] == "Sail":
        break
    city = fill_in_data[0]
    population = int(fill_in_data[1])
    gold = int(fill_in_data[2])
    if city not in cities_dict:
        cities_dict[city] = [population, gold]
    else:
        cities_dict[city][0] += population
        cities_dict[city][1] += gold

while True:
    event = input().split("=>")
    if event[0] == "End":
        break
    if event[0] == "Plunder":
        city = event[1]
        people = int(event[2])
        gold = int(event[3])
        cities_dict[city][0] -= people
        cities_dict[city][1] -= gold
        print(f"{city} plundered! {gold} gold stolen, {people} citizens killed.")
        if cities_dict[city][0] <= 0 or cities_dict[city][1] <= 0:
            del cities_dict[city]
            print(f"{city} has been wiped off the map!")
    if event[0] == "Prosper":
        city = event[1]
        gold = int(event[2])
        if gold <= 0:
            print(f"Gold added cannot be a negative number!")
        else:
            cities_dict[city][1] += gold
            print(f"{gold} gold added to the city treasury. {city} now has {cities_dict[city][1]} gold.")

if cities_dict:
    print(f"Ahoy, Captain! There are {len(cities_dict)} wealthy settlements to go to:")
    for city in cities_dict:
        print(f"{city} -> Population: {cities_dict[city][0]} citizens, Gold: {cities_dict[city][1]} kg")
else:
    print(f"Ahoy, Captain! All targets have been plundered and destroyed!")
