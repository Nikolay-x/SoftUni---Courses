# 12.*SoftUni Exam Results
# Judge statistics on the last Programing Fundamentals exam were not working correctly, so you have the task of taking all the submissions and analyzing them properly. You should collect all the submissions and print the final results and statistics about each language in which the participants submitted their solutions.
# You will be receiving lines in the following format: "{username}-{language}-{points}" until you receive "exam finished". You should store each username and their submissions and points. If a student has two or more submissions for the same language, save only his maximum points.
# You can receive a command to ban a user for cheating in the following format: "{username}-banned". In that case, you should remove the user from the contest but preserve his submissions in the total count of submissions for each language.
# After receiving "exam finished", print each of the participants in the following format:
# "Results:
# {username1} | {points}
# {username2} | {points}
# …
# {usernameN} | {points}"
# After that, print each language used in the exam in the following format:
# "Submissions:
# {language1} - {submissions_count}
# {language2} - {submissions_count}
# …
# {language3} - {submissions_count}"
# Input / Constraints
# Until you receive "exam finished" you will be receiving participant submissions in the following format: "{username}-{language}-{points}"
# You can receive a ban command -> "{username}-banned"
# The points of the participant will always be a valid integer in the range [0-100];
# Output
# Print the exam results for each participant
# After that, print each language in the format shown above
# Allowed working time / memory: 100ms / 16MB
#
# Input
# Peter-Java-84
# George-C#-84
# George-C#-70
# Katy-C#-94
# exam finished
#
# Output
# Results:
# Peter | 84
# George | 84
# Katy | 94
# Submissions:
# Java - 1
# C# - 3

judge_dict = dict()
submissions = dict()

while True:
    line = input()
    if line == "exam finished":
        break
    if "banned" not in line:
        line = line.split("-")
        username = line[0]
        language = line[1]
        points = int(line[2])
        if username not in judge_dict:
            judge_dict[username] = {language: points}
        else:
            if language in judge_dict[username]:
                if points > judge_dict[username][language]:
                    judge_dict[username][language] = points
        if language not in submissions:
            submissions[language] = 1
        else:
            submissions[language] += 1
    else:
        line = line.split("-")
        username = line[0]
        if username in judge_dict:
            judge_dict.pop(username)

print("Results:")
for username in judge_dict:
    for language in judge_dict[username]:
        print(f"{username} | {judge_dict[username][language]}")
print("Submissions:")
for language in submissions:
    print(f"{language} - {submissions[language]}")
