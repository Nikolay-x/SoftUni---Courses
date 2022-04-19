# 2.Judge
# You know the judge system, right?! Your job is to create a program similar to the Judge system.
# You will receive several input lines in one of the following formats:
# "{username} -> {contest} -> {points}"
# The "contest" and "username" are strings, the given "points" will be an integer number. You need to keep track of every contest and points of each user:
# If the user has already participated in the contest, update their points only if the new ones are more than the older ones.
# Otherwise, just save the data - contest, username, and points.
# Also, you need to keep individual statistics for each user - the total points of all contests (including even points from the same contents).
# You should end your program when you receive the command "no more time". At that point you should print each contest in order of input, for each contest print the participants ordered by points in descending order, then ordered by name in ascending order. After that, you should print individual statistics for every participant ordered by total points in descending order, and then by alphabetical order.
# Input / Constraints
# The input comes in the form of commands in one of the formats specified above.
# Username and contest name always will be one word.
# Points will be an integer will be an integer in range [0, 1000].
# There will be no invalid input lines.
# If all sorting criteria fail, the order should be by order of input.
# The input ends when you receive the command "no more time".
# Output
# The output format for the contests is:
# "{constest_name}: {number_participants} participants
# 1. {username1} <::> {points}
# 2. {username2} <::> {points}
# …
# {N}. {usernameN} <::> {points}"
# After you print all contests, print the individual statistics for every participant.
# The output format is:
# "Individual standings:
# 1.{username1} -> {total_points}
# 2.{username} -> {total_points}
# …
# {N}. {username} -> {total_points}"
#
# Input
# Peter -> Algo -> 400
# George -> Algo -> 300
# Simo -> Algo -> 200
# Peter -> DS -> 150
# Mariya -> DS -> 600
# no more time
#
# Output
# Algo: 3 participants
# 1. Peter <::> 400
# 2. George <::> 300
# 3. Simo <::> 200
# DS: 2 participants
# 1. Mariya <::> 600
# 2. Peter <::> 150
# Individual standings:
# 1. Mariya -> 600
# 2. Peter -> 550
# 3. George -> 300
# 4. Simo -> 200

contests_dict = dict()

while True:
    line = input()
    if line == "no more time":
        break
    line = line.split(" -> ")
    username = line[0]
    contest = line[1]
    points = int(line[2])
    if contest not in contests_dict:
        contests_dict[contest] = {username: points}
    else:
        if username not in contests_dict[contest]:
            contests_dict[contest].update({username: points})
        else:
            if points > contests_dict[contest][username]:
                contests_dict[contest][username] = points

for contest in contests_dict:
    print(f"{contest}: {len(contests_dict[contest])} participants")
    p = 1
    for (username, points) in sorted(contests_dict[contest].items(), key=lambda p: (-p[1], p[0])):
        print(f"{p}. {username} <::> {points}")
        p += 1

print("Individual standings:")
individual_results = {}
for contest in contests_dict:
    for username in contests_dict[contest]:
        if username not in individual_results:
            individual_results[username] = 0
        individual_results[username] += contests_dict[contest][username]

i = 1
for (username, points) in sorted(individual_results.items(), key=lambda x: (-x[1], x[0])):
    print(f"{i}. {username} -> {points}")
    i += 1
