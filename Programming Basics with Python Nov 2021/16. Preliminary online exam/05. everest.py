# Задача 5. Еверест
# Атанас е алпинист, чиято следваща цел е изкачването на Еверест. Вашата задача е да напишете програма която да следи до каква височина е достигнал Атанас и за колко дни е изкачил върха. Той започва изкачването си от ден първи от базов лагер, който е на 5 364 метра, а самият връх е на 8 848м. Преди всяко изкачване на определени метри, Атанас може да си почине в някой лагер и да продължи на следващия ден или да продължи изкачването без да спре, като максималното време, в което той може да изкачва върха е 5 дни. Програмата приключва при получаване на командата "END", при достигане на върха(8 848м) или при превишаване на разрешените 5 дни за изкачване.
#
# Вход
# От конзолата се четат по два реда до въвеждане на команда "END", ако са минали повече от 5 дни в изкачване или се достигне върха (8 848м):
# "Yes" / "No" - текст - дали Атанас ще нощува преди изкачването на следващите метри или не
# Изкачени метри - цяло число в интервала [1...4000]
#
# Изход
# След получаване на командата "END", превишаване на разрешениете 5 дни за изкачване или се достигне върха (8 848м), на конзолата се отпечатва:
# Ако Атанас е изкачил Еверест:
# "Goal reached for {брой дни които Атанас е изкачвал върха} days!"
# Ако Атанас НЕ е изкачил Еверест:
# "Failed!"
# "{достигнатите от Атанас метри}"
#
# Вход
# Yes
# 1254
# Yes
# 1402
# No
# 250
# Yes
# 635
#
# Изход
# Goal reached for 4 days!

command = input()

current_elevation = 5364

days_count = 1

while command != "END":

    daily_meters = int(input())

    if days_count <= 5:
        if command == "Yes":
            days_count += 1
            current_elevation += daily_meters
        elif command == "No":
            current_elevation += daily_meters

    if days_count > 5:
        current_elevation -= daily_meters
        break

    if current_elevation >= 8848:
        break

    command = input()

if current_elevation >= 8848:
    print(f"Goal reached for {days_count:.0f} days!")
else:
    print("Failed!")
    print(f"{current_elevation:.0f}")