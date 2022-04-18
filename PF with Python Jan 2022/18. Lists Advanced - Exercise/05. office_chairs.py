# 5.Office Chairs
# You are a facility manager at a large business center. One of your responsibilities is to check if each conference room in the center has enough chairs for the visitors.
# On the first line, you will be given an integer n representing the number of rooms in the business center. On the following n lines for each room, you will receive information about the chairs in the room and the number of visitors. Each chair will be presented with the char "X". Next, there will be a single space and the number of visitors at the end. For example: "XXXXX 4" (5 chairs and 4 visitors).
# Keep track of the free chairs:
# If there are not enough chairs in a specific room, print the following message: "{needed_chairs_in_room} more chairs needed in room {number_of_room}". The rooms start from 1.
# Otherwise, print: "Game On, {total_free_chairs} free chairs left".
#
# Input
# 4
# XXXX 4
# XX 1
# XXXXXX 3
# XXX 3
#
# Output
# Game On, 4 free chairs left

rooms_count = int(input())

game_on = True
total_chairs = 0

for room in range(1, rooms_count + 1):
    situation = input().split(" ")
    if len(situation[0]) < int(situation[1]):
        game_on = False
        print(f"{int(situation[1]) - len(situation[0])} more chairs needed in room {room}")
    else:
        total_chairs += len(situation[0]) - int(situation[1])

if game_on:
    print(f"Game On, {total_chairs} free chairs left")
