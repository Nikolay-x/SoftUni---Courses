# 7. Трекинг мания
# Катерачи от цяла България се събират на групи и набелязват следващите върхове за изкачване. Според размера на групата, катерачите ще изкачват различни върхове.
# Група до 5 човека – изкачват Мусала
# Група от 6 до 12 човека – изкачват Монблан
# Група от 13 до 25 човека – изкачват Килиманджаро
# Група от 26 до 40 човека –  изкачват К2
# Група от 41 или повече човека – изкачват Еверест
# Да се напише програма, която изчислява процента на катерачите изкачващи всеки връх.
# Вход
# От конзолата се четат поредица от числа, всяко на отделен ред:
# На първия ред – броя на групите от катерачи – цяло число в интервала [1...1000]
# За всяка една група на отделен ред – броя на хората в групата – цяло число в интервала [1...1000]
# Изход
# Да се отпечатат на конзолата 5 реда, всеки от които съдържа процент между 0.00% и 100.00% с точност до втората цифра след десетичната запетая.
# Първи ред - процентът изкачващи Мусала
# Втори ред – процентът изкачващи Монблан
# Трети ред – процентът изкачващи Килиманджаро
# Четвърти ред – процентът изкачващи К2
# Пети ред – процентът изкачващи Еверест
#
# Вход
# 10
# 10
# 5
# 1
# 100
# 12
# 26
# 17
# 37
# 40
# 78
#
# Изход
# 1.84%
# 6.75%
# 5.21%
# 31.60%
# 54.60%

groups_number = int(input())

musala_people = 0
monblan_people = 0
kilimanjaro_people = 0
k2_people = 0
everest_people = 0

for i in range(1, groups_number +1):
    group_number = int(input())
    if group_number <= 5:
        musala_people += group_number
    elif group_number <= 12:
        monblan_people += group_number
    elif group_number <= 25:
        kilimanjaro_people += group_number
    elif group_number <= 40:
        k2_people += group_number
    elif group_number > 40:
        everest_people += group_number

total_people_number = musala_people + monblan_people + kilimanjaro_people + k2_people +everest_people

print(f"{(musala_people / total_people_number * 100):.2f}%")
print(f"{(monblan_people / total_people_number * 100):.2f}%")
print(f"{(kilimanjaro_people / total_people_number * 100):.2f}%")
print(f"{(k2_people / total_people_number * 100):.2f}%")
print(f"{(everest_people / total_people_number * 100):.2f}%")
