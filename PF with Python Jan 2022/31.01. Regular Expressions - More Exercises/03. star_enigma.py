# 3.Star Enigma
# The war is in its peak, but you, young Padawan, can turn the tides with your programming skills. You are tasked to create a program to decrypt the messages of The Order and prevent the death of hundreds of lives.
# You will receive several messages, which are encrypted using the legendary star enigma. You should decrypt the messages, following these rules:
# To properly decrypt a message, you should count all the letters [s, t, a, r] – case insensitive and remove the count from the current ASCII value of each symbol of the encrypted message.
# After decryption:
# Each message should have a planet name, population, attack type ('A', as attack or 'D', as destruction) and soldier count.
# The planet name starts after '@' and contains only letters from the Latin alphabet.
# The planet population starts after ':' and is an Integer;
# The attack type may be "A"(attack) or "D"(destruction) and must be surrounded by "!" (exclamation mark).
# The soldier count starts after "->" and should be an Integer.
# The order in the message should be: planet name -> planet population -> attack type -> soldier count. Each part can be separated from the others by any character except: '@', '-', '!', ':' and '>'.
# Input / Constraints
# The first line holds n – the number of messages– integer in range [1…100];
# On the next n lines, you will be receiving encrypted messages.
# Output
# After decrypting all messages, you should print the decrypted information in the following format:
# First print the attacked planets, then the destroyed planets.
# "Attacked planets: {attackedPlanetsCount}"
# "-> {planetName}"
# "Destroyed planets: {destroyedPlanetsCount}"
# "-> {planetName}"
# The planets should be ordered by name alphabetically.
#
# Input
# 2
# STCDoghudd4=63333$D$0A53333
# EHfsytsnhf?8555&I&2C9555SR
#
# Output
# Attacked planets: 1
# -> Alderaa
# Destroyed planets: 1
# -> Cantonica

import re
n = int(input())

key_regex = r"[star]"
info_regex = r"(?<=@)([A-Za-z]+)(?:[^\@\-\!\:\>]+)?:(\d+)(?:[^\@\-\!\:\>]+)?!(A|D)!(?:[^\@\-\!\:\>]+)?->(\d+)"

attacked_planets_list = []
destroyed_planets_list = []

for i in range(n):
    entry_is_valid = True
    line = input()
    key_list = []

    decrypted_message = ""
    key_matches = re.finditer(key_regex, line, re.IGNORECASE)
    for match in key_matches:
        key = match.group()
        if key != "":
            key_list.append(key)
    key = len("".join(key_list))
    for ch in line:
        decrypted_message += chr(ord(ch) - key)

    info_matches = re.finditer(info_regex, decrypted_message)

    if info_matches:
        for match in info_matches:

            planet_name = match[1]
            planet_population = int(match[2])
            attack_type = match[3]
            soldier_count = int(match[4])

            if attack_type == "A":
                attacked_planets_list.append(planet_name)
            elif attack_type == "D":
                destroyed_planets_list.append(planet_name)

attacked_planets_list = sorted(attacked_planets_list, key=lambda x: x)
destroyed_planets_list = sorted(destroyed_planets_list, key=lambda x: x)

print(f"Attacked planets: {len(attacked_planets_list)}")
for planet in attacked_planets_list:
    print(f"-> {planet}")
print(f"Destroyed planets: {len(destroyed_planets_list)}")
for planet in destroyed_planets_list:
    print(f"-> {planet}")
