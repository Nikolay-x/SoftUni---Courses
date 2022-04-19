# 11.*Force Book
# The force users struggle to remember which side is the different force users from because they switch them too often. So you are tasked to create a web application to manage their profiles. You should store information for every unique force user registered in the application.
# You will receive several input lines in one of the following formats:
# "{force_side} | {force_user}"
# "{force_user} -> {force_side}"
# The "force_user" and "force_side" are strings, containing any character.
# If you receive "force_side | force_user":
# If there is no such force user and no such force side -> create a new force side and add the force user to the corresponding side.
# Only if there is no such force user in any force side -> add the force user to the corresponding side.
# If there is such force user already -> skip the command and continue to the next operation.
# If you receive a "force_user -> force_side":
# If there is such force user already -> change their side.
# If there is no such force user in any force side -> add the force user to the corresponding force side.
# If there is no such force user and no such force side -> create new force side and add the force user to the corresponding side.
# Then you should print on the console: "{force_user} joins the {force_side} side!".
# You should end your program when you receive the command "Lumpawaroo". At that point, you should print each force side. For each side, print the force users.
# In case there are no force users on a side, you shouldn't print the side information.
# Input / Constraints
# The input comes in the form of commands in one of the formats specified above.
# The input ends when you receive the command "Lumpawaroo".
# Output
# As output for each force side, you must print all the force users.
# The output format is:
# "Side: {force_side}, Members: {force_users_count}
# ! {force_user1}
# ! {force_user2}
# …
# ! {force_userN}"
# In case there are NO force users on a side, don't print this side.
#
# Input
# Light | Peter
# Dark | Kim
# Light | Kim
# Lumpawaroo
#
# Output
# Side: Light, Members: 1
# ! Peter
# Side: Dark, Members: 1
# ! Kim

# Solution need to be fixed for the below input:
#
# Lighter | Royal
# Darker | DCay
# Ivan Ivanov -> Lighter
# DCay -> Lighter
# DCay -> Lig
# Lumpawaroo
#
# def create_force_side(side, member, user_info_dict):
#     condition = [current_side for current_side in user_info_dict if member in user_info_dict[current_side]]
#
#     if len(condition) == 0:
#         condition.clear()
#         if side not in user_info_dict:
#             user_info_dict[side] = [member]
#         else:
#             user_info_dict[side].append(member)
#
#     return user_info_dict
#
#
# def create_force_user(member, side, user_info_dict):
#     for current_side in user_info_dict:
#         if member in user_info_dict[current_side]:
#             if len(user_info_dict[current_side]) > 1:
#                 user_info_dict[current_side].pop(member)
#                 break
#             else:
#                 del user_info_dict[current_side]
#                 break
#
#     if side in user_info_dict:
#         user_info_dict[side].append(member)
#     else:
#         user_info_dict[side] = [member]
#
#     print(f"{member} joins the {side} side!")
#
#
# def force_book():
#     user_info_dict = {}
#
#     while True:
#         command = input()
#
#         if command == 'Lumpawaroo':
#             break
#
#         if '|' in command:
#             command = command.split(' | ')
#             side = command[0]
#             member = command[1]
#             create_force_side(side, member, user_info_dict)
#
#         elif '->' in command:
#             command = command.split(' -> ')
#             member = command[0]
#             side = command[1]
#             create_force_user(member, side, user_info_dict)
#
#     for data in user_info_dict:
#         print(f'Side: {data}, Members: {len(user_info_dict[data])}')
#         for name in user_info_dict[data]:
#             print(f'! {name}')
#
#
# force_book()


force_book = dict()
count = 0
count1 = 0

while True:
    line = input()
    if line == "Lumpawaroo":
        break
    if "|" in line:
        line = line.split(" | ")
        force_side = line[0]
        force_user = line[1]
        count = 0
        for f_s in force_book:
            if force_user in force_book[f_s]:
                count += 1
        if count == 0:
            if force_side not in force_book:
                force_book[force_side] = [force_user]
                # force_book[force_side] = []
                # force_book[force_side].append(force_user)
            else:
                force_book[force_side].append(force_user)
    if "->" in line:
        line = line.split(" -> ")
        force_user = line[0]
        force_side = line[1]
        count1 = 0
        for f_s in force_book:
            if force_user in force_book[f_s]:
                count1 += 1
        if count1 > 0:
            if force_side in force_book:
                force_book[force_side].append(force_user)
                for f_s in force_book:
                    if f_s != force_side and force_user in force_book[f_s]:
                        force_book[f_s].remove(force_user)
            else:
                force_book[force_side] = [force_user]
                for f_s in force_book:
                    if f_s != force_side and force_user in force_book[f_s]:
                        force_book[f_s].remove(force_user)
        if count1 == 0:
            if force_side in force_book:
                force_book[force_side].append(force_user)
            else:
                force_book[force_side] = [force_user]
                # force_book[force_side] = []
                # force_book[force_side].append(force_user)
        print(f'{force_user} joins the {force_side} side!')

for f_s in force_book:
    if len(force_book[f_s]) > 0:
        print(f'Side: {f_s}, Members: {len(force_book[f_s])}')
        for f_u in force_book[f_s]:
            print(f'! {f_u}')
