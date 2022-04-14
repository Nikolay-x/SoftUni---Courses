# 4.Стъпки
# Габи иска да започне здравословен начин на живот и си е поставила за цел да върви 10 000 стъпки всеки ден. Някои дни обаче е много уморена от работа и ще иска да се прибере преди да постигне целта си. Напишете програма, която чете от конзолата по колко стъпки изминава тя всеки път като излиза през деня и когато постигне целта си да се изписва "Goal reached! Good job!" и колко стъпки повече е извървяла "{разликата между стъпките} steps over the goal!"
# Ако иска да се прибере преди това, тя ще въведе командата "Going home" и ще въведе стъпките, които е извървяла докато се прибира. След което, ако не е успяла да постигне целта си, на конзолата трябва да се изпише: "{разликата между стъпките} more steps to reach goal."
#
# Вход
# 1000
# 1500
# 2000
# 6500
#
# Изход
# Goal reached! Good job!
# 1000 steps over the goal!

goal = 10000

current_steps = input()
total_steps = 0

while current_steps != "Going home":
    current_steps = int(current_steps)
    total_steps += current_steps

    if total_steps >= goal:
        break

    current_steps = input()

if total_steps < goal:
    current_steps = int(input())
    total_steps += current_steps

if total_steps >= goal:
    print("Goal reached! Good job!")
    print(f"{total_steps - goal} steps over the goal!")
else:
    print(f"{goal - total_steps} more steps to reach goal.")
