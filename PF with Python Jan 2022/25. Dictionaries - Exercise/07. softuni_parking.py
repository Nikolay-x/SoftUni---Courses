# 7.SoftUni Parking
# SoftUni just got a new fancy parking lot. It even has online parking validation, except the online service doesn't work. It can only receive users' data, but it doesn't know what to do with it. Good thing you're on the dev team and know how to fix it, right?
# Write a program, which validates a parking place - users can register to enter the park and unregister to leave.
# The program receives 2 types of commands:
# "register {username} {license_plate_number}":
# oThe system only supports one car per user at the moment, so if a user tries to register another license plate using the same username, the system should print:
# "ERROR: already registered with plate number {license_plate_number}"
# oIf the check above passes successfully, the user should be registered, so the system should print:
#  "{username} registered {license_plate_number} successfully"
# "unregister {username}":
# oIf the user is not present in the database, the system should print:
# "ERROR: user {username} not found"
# oIf the check above passes successfully, the system should print:
# "{username} unregistered successfully"
# After you execute all of the commands, print all the currently registered users and their license plates in the format:
# "{username} => {license_plate_number}"
# Input
# First line: n - number of commands - integer
# Next n lines: commands in one of the two possible formats:
# oRegister: "register {username} {license_plate_number}"
# oUnregister: "unregister {username}"
# The input will always be valid, and you do not need to check it explicitly.
#
# Input
# 5
# register John CS1234JS
# register George JAVA123S
# register Andy AB4142CD
# register Jesica VR1223EE
# unregister Andy
#
# Output
# John registered CS1234JS successfully
# George registered JAVA123S successfully
# Andy registered AB4142CD successfully
# Jesica registered VR1223EE successfully
# Andy unregistered successfully
# John => CS1234JS
# George => JAVA123S
# Jesica => VR1223EE

commands_count = int(input())
parking = {"register": {}}

for i in range(commands_count):
    command = input().split(" ")
    if command[0] == "register":
        user = command[1]
        user_car_plate = command[2]

        if user not in parking["register"]:
            parking["register"][user] = user_car_plate
            print(f'{user} registered {user_car_plate} successfully')
        else:
            print(f'ERROR: already registered with plate number {parking["register"][user]}')

    elif command[0] == "unregister":
        user = command[1]

        if user not in parking["register"]:
            print(f'ERROR: user {user} not found')
        else:
            print(f'{user} unregistered successfully')
            parking["register"].pop(user)

for user in parking["register"]:
    print(f'{user} => {parking["register"][user]}')
