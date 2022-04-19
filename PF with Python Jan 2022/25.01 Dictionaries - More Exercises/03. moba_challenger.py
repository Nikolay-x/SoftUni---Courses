# 3.MOBA Challenger
# You are a pro MOBA player, you are struggling to become а master of the Challenger tier. So, you carefully watch the statistics in the tier.
# You will receive several input lines in one of the following formats:
# "{player} -> {position} -> {skill}"
# "{player} vs {player}"
# The "player" and "position" are strings, and the given "skill" will be an integer number. You need to keep track of every player.
# When you receive a player with his position and skill, add him to the players' pool, if he isn`t present, else add his position and skill or update his skill, only if the current position skill is lower than the new value.
# If you receive "{player} vs {player}" and both players exist in the tier, they duel with the following rules:
# If they got at least one position in common, the player with better total skill points wins and the other is demoted from the tier -> remove him.
# If they have same total skill points at the same positions, the duel is tie and they both continue in the Season.
# If they don`t have positions in common, the duel isn`t happening and both continue in the Season.
# You should end your program when you receive the command "Season end". At that point you should print the players, ordered by total skill in descending order, then ordered by player name in ascending order. For each player print their position and skill, ordered descending by skill, then ordered by position name in ascending order.
# Input / Constraints
# The input comes in the form of commands in one of the formats specified above.
# Player and position will always be one word string, containing no whitespaces.
# Skill will be an integer in the range [0, 1000].
# There will be no invalid input lines.
# The program ends when you receive the command "Season end".
# Output
# The output format for each player is:
# "{player}: {total_skills} skill"
# - {position1} <::> {skill}
# - {position2} <::> {skill}
# …
# - {positionN} <::> {skill}"
#
# Input
# Peter -> Adc -> 400
# George -> Jungle -> 300
# Simon -> Mid -> 200
# Simon -> Support -> 250
# Season end
#
# Output
# Simon: 450 skill
# - Support <::> 250
# - Mid <::> 200
# Peter: 400 skill
# - Adc <::> 400
# George: 300 skill
# - Jungle <::> 300

moba_dict = dict()
total_skill_dict = dict()

while True:
    line = input()
    if line == "Season end":
        break
    if "->" in line:
        (player, position, skill) = line.split(" -> ")
        if player not in moba_dict:
            moba_dict[player] = {position: int(skill)}
            total_skill_dict[player] = int(skill)
        else:
            if position not in moba_dict[player]:
                moba_dict[player].update({position: int(skill)})
                total_skill_dict[player] += int(skill)
            else:
                if moba_dict[player][position] < int(skill):
                    moba_dict[player][position] = int(skill)
                    total_skill_dict[player] += int(skill) - moba_dict[player][position]

    if "vs" in line:
        (player1, player2) = line.split(" vs ")
        if player1 in moba_dict and player2 in moba_dict:
            for position in moba_dict[player1]:
                if position in moba_dict[player2]:
                    if total_skill_dict[player1] > total_skill_dict[player2]:
                        del moba_dict[player2]
                        del total_skill_dict[player2]
                        break
                    elif total_skill_dict[player1] < total_skill_dict[player2]:
                        del moba_dict[player1]
                        del total_skill_dict[player1]
                        break

for (player, skill) in sorted(total_skill_dict.items(), key=lambda x: (-x[1], x[0])):
    print(f"{player}: {skill} skill")
    for (position, skills) in sorted(moba_dict[player].items(), key=lambda x: (-x[1], x[0])):
        print(f"- {position} <::> {skills}")
