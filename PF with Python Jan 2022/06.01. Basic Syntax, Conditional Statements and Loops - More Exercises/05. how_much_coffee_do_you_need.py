# 5.How Much Coffee Do You Need?
# Everybody knows that you spend too much time awake during nighttime.
# Your task is to define how much coffee you need to stay awake. Until you receive the command "END", you need to read commands on different lines. According to the commands, you will print the number of coffees you need to stay awake during the daytime. If the count exceeds 5, print 'You need extra sleep'.
# The list of events can contain the following:
# You have homework to do ("coding").
# You have a dog or a cat that just decided to wake up too early ("dog" or "cat").
# You watch a movie ("movie").
# If other events are present, they will be represented by arbitrary strings. Just ignore them!
# Each event can be lowercase or uppercase. If it is lowercase, you need 1 coffee by event, and if it is uppercase, you need 2 coffees.
#
# Input
# dog
# CAT
# gaming
# END
#
# Output
# 3

coffee_count = 0

while True:
    command = input()

    if command == "coding" or command == "dog" or command == "cat" or command == "movie":
        coffee_count += 1
    elif command == "CODING" or command == "DOG" or command == "CAT" or command == "MOVIE":
        coffee_count += 2

    if coffee_count > 5:
        print("You need extra sleep")
        break

    if command == "END":
        break

if coffee_count <= 5:
    print(coffee_count)
