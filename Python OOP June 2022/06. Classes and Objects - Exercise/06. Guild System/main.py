# 6.Guild System
# You are tasked to create two classes: a Player class and a Guild class.
#
# project
#     __init__.py
#     guild.py
#     player.py
#
# The Player class should receive a name (string), a hp (int), and a mp (int) upon initialization. The Player also has 2 instance attributes: skills (empty dictionary that will contain the skills of each player and its mana cost) and a guild set to "Unaffiliated" by default.
# The Player class should also have two additional methods:
# -add_skill(skill_name, mana_cost)
# oAdds the skill and the corresponding mana cost to the dictionary of skills. Returns "Skill {skill_name} added to the collection of the player {player_name}"
# oIf the skill is already in the collection, returns "Skill already added"
# -player_info()
# oReturns the player's information, including their skills, in this format:
# "Name: {player_name}
#  Guild: {guild_name}
#  HP: {hp}
#  MP: {mp}
#  ==={skill_name_1} - {skill_mana_cost}
#  ==={skill_name_2} - {skill_mana_cost}
#  …
#  ==={skill_name_N} - {skill_mana_cost}"
#
# The Guild class receives a name (string). The Guild should also have one instance attribute players (an empty list which will contain the players of the guild). The class also has 3 additional methods:
# -assign_player(player: Player)
# oAdds the player to the guild and returns "Welcome player {player_name} to the guild {guild_name}". Remember to change the player's guild in the player class.
# oIf he is already in the guild, returns "Player {player_name} is already in the guild."
# oIf the player is in another guild, returns "Player {player_name} is in another guild."
# -kick_player(player_name: str)
# oRemoves the player from the guild and returns "Player {player_name} has been removed from the guild.". Remember to change the player's guild in the player class to "Unaffiliated".
# oIf there is no such player in the guild, returns "Player {player_name} is not in the guild."
# -guild_info()
# oReturns the guild's information, including the players in the guild, in the format:
# "Guild: {guild_name}
# {first_player's info}
# …
# {Nplayer's info}"
#
# Test Code
# player = Player("George", 50, 100)
# print(player.add_skill("Shield Break", 20))
# print(player.player_info())
# guild = Guild("UGT")
# print(guild.assign_player(player))
# print(guild.guild_info())
#
# Output
# Skill Shield Break added to the collection of the player George
# Name: George
# Guild: Unaffiliated
# HP: 50
# MP: 100
# ===Shield Break - 20
#
# Welcome player George to the guild UGT
# Guild: UGT
# Name: George
# Guild: UGT
# HP: 50
# MP: 100
# ===Shield Break - 20

from project.guild import Guild
from project.player import Player

player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())

# player = Player("George", 50, 100)
# player1 = Player("Ivan", 60, 120)
# print(player.add_skill("Shield Break", 20))
# print(player1.add_skill("Ring Of Chaos", 30))
# print(player.player_info())
# print(player1.player_info())
# print()
#
# guild = Guild("UGT")
# guild1 = Guild("PTL")
# print(guild.assign_player(player))
# print(guild.assign_player(player))
# print(guild1.assign_player(player1))
# print(guild1.assign_player(player))
# print()
#
# print(guild.kick_player("Georg"))
# print(guild.kick_player("Ivan"))
# print(guild1.kick_player("Ivan"))
# print()
#
# print(guild.guild_info())
# print(guild1.guild_info())
# print()
#
# print(player.player_info())
# print(player1.player_info())
