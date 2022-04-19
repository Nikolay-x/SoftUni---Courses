# 1.Ranking
# Here comes the final and the most interesting part – the Final ranking of the candidate-interns. The final ranking is determined by the points of the interview tasks and by the points from the exams in SoftUni. Here is your final task. You will receive some lines of input in the format "{contest}:{password for contest}" until you receive "end of contests". Save that data because you will need it later. After that you will receive other type of inputs in format "{contest}=>{password}=>{username}=>{points}" until you receive "end of submissions". Here is what you need to do.
# Check if the contest is valid (It is considered valid if you received it in the first type of input)
# Check if the password is correct for the given contest
# If the contest and the password is valid, save the user with the contest they take part in (a user can take part in many contests) and the points the user has in the given contest. If you receive the same contest and the same user update the points only if the new ones are more than the older ones.
# In the end, you should print the info for the user with the most points (total points for all contents they participated in) in the format "Best candidate is {user} with total {total_points} points.". After that print all students ordered by their names. For each user print each contest with the points in descending order. See the examples.
# Input
# Strings in format "{contest}:{password for contest}" until the "end of contests" command. There will be no case with two equal contests
# Strings in format "{contest}=>{password}=>{username}=>{points}" until the "end of submissions" command.
# There will be no case with 2 or more users with same total points!
# Output
# On the first line, print the best user in format "Best candidate is {user} with total {total points} points.".
# Then print all students ordered as mentioned above in format:
# "{user_name1}
# #  {contest1} -> {points}
# #  {contest2} -> {points}
# …
# #  {contestN} -> {points}"
# Constraints
# The strings may contain any ASCII character except from (:, =, >).
# The numbers will be in range [0 - 10000].
# Second input is always valid.
#
# Input
# Part One Interview:success
# JS Fundamentals:fundExam
# C# Fundamentals:fundPass
# Algorithms:fun
# end of contests
# C# Fundamentals=>fundPass=>Tanya=>350
# Algorithms=>fun=>Tanya=>380
# Part One Interview=>success=>Nikola=>120
# Java Basics Exam=>wrong_pass=>Teo=>400
# Part One Interview=>success=>Tanya=>220
# OOP Advanced=>password123=>Kay=>231
# C# Fundamentals=>fundPass=>Tanya=>250
# C# Fundamentals=>fundPass=>Nikola=>200
# JS Fundamentals=>fundExam=>Tanya=>400
# end of submissions
#
# Output
# Best candidate is Tanya with total 1350 points.
# Ranking:
# Nikola
# #  C# Fundamentals -> 200
# #  Part One Interview -> 120
# Tanya
# #  JS Fundamentals -> 400
# #  Algorithms -> 380
# #  C# Fundamentals -> 350
# #  Part One Interview -> 220

# contest_data = input()
# contests_dict = dict()
#
# while contest_data != "end of contests":
#     (contest, password) = contest_data.split(":")
#     contests_dict[contest] = password
#     contest_data = input()
#
# submission_data = input()
# users_dict = dict()
#
# while submission_data != "end of submissions":
#     (contest, password, user, points) = submission_data.split("=>")
#
#     if contest in contests_dict and contests_dict[contest] == password:
#
#         if user not in users_dict:
#             users_dict[user] = dict()
#
#         if contest not in users_dict[user]:
#             users_dict[user][contest] = int(points)
#         else:
#             if users_dict[user][contest] < int(points):
#                 users_dict[user][contest] = int(points)
#
#     submission_data = input()
#
# best_user = ""
# best_points = 0
#
# for user in users_dict.keys():
#     total_points = sum(users_dict[user].values())
#     if total_points > best_points:
#         best_points = total_points
#         best_user = user
#
# print(f"Best candidate is {best_user} with total {best_points} points.")
# print("Ranking:")
# for user in sorted(users_dict.keys()):
#     print(user)
#     for (contest, points) in sorted(users_dict[user].items(), key=lambda cp: cp[1], reverse=True):
#     # for (contest, points) in sorted(users_dict[user].items(), key=lambda cp: -cp[1]):
#         print(f"#  {contest} -> {points}")


contests = dict()
submissions = dict()
max_points_dict = dict()
max_points = 0
best_candidate = None

while True:
    contest_data = input()
    if contest_data == "end of contests":
        break
    contest_data = contest_data.split(":")
    contest = contest_data[0]
    contest_password = contest_data[1]
    if contest not in contests:
        contests[contest] = contest_password

while True:
    submission = input()
    if submission == "end of submissions":
        break
    submission = submission.split("=>")
    contest = submission[0]
    password = submission[1]
    username = submission[2]
    points = int(submission[3])
    if contest in contests:
        if password == contests[contest]:
            if username not in submissions:
                submissions[username] = {contest: points}
            else:
                if contest in submissions[username]:
                    if points > submissions[username][contest]:
                        submissions[username][contest] = points
                else:
                    submissions[username].update({contest: points})

for username in submissions:
    for contest in submissions[username]:
        if username not in max_points_dict:
            max_points_dict[username] = submissions[username][contest]
        else:
            max_points_dict[username] += submissions[username][contest]

for username in max_points_dict:
    if max_points_dict[username] > max_points:
        max_points = max_points_dict[username]
        best_candidate = username

print(f"Best candidate is {best_candidate} with total {max_points} points.")
print("Ranking:")

s = sorted(submissions.keys())

for user in s:
    print(f"{user}")
    q = sorted(submissions[user].values())
    q.reverse()
    for val in q:
        for contest in submissions[user]:
            if submissions[user][contest] == val:
                print(f"#  {contest} -> {val}")
