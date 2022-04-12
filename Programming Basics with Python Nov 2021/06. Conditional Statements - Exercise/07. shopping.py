# 7. Пазаруване
# Петър иска да купи N видеокарти, M процесора и P на брой рам памет. Ако броя на видеокартите е по-голям от този на процесорите получава 15% отстъпка от крайната сметка. Важат следните цени:
# Видеокарта – 250 лв./бр.
# Процесор – 35% от цената на закупените видеокарти/бр.
# Рам памет – 10% от цената на закупените видеокарти/бр.
# Да се изчисли нужната сума за закупуване на материалите и да се пресметне дали бюджета ще му стигне.
# Вход
# Входът се състои от четири реда:
# 1.Бюджетът на Петър - реално число в интервала [1.0…100000.0]
# 2.Броят видеокарти - цяло число в интервала [1…100]
# 3.Броят процесори - цяло число в интервала [1…100]
# 4.Броят рам памет - цяло число в интервала [1…100]
# Изход
# На конзолата се отпечатва 1 ред, който трябва да изглежда по следния начин:
# Ако бюджета е достатъчен:
# "You have {остатъчен бюджет} leva left!"
# Ако сумата надхвърля бюджета:
# "Not enough money! You need {нужна сума} leva more!"
# Резултатът да се форматира до втория знак след десетичната запетая.
#
# Вход
# 900
# 2
# 1
# 3
#
# Изход
# You have 198.75 leva left!

peter_budget = float(input())
videocards_number = int(input())
processors_number = int(input())
rams_number = int(input())

videocards_price = videocards_number * 250
processor_price = videocards_price * 0.35
processors_price = processors_number * processor_price
ram_price = videocards_price * 0.1
rams_price = rams_number * ram_price

total_price = videocards_price + processors_price + rams_price

if videocards_number > processors_number:
    total_price = total_price - total_price * 0.15

if peter_budget >= total_price:
    print(f"You have {(peter_budget - total_price):.2f} leva left!")
else:
    print(f"Not enough money! You need {(total_price - peter_budget):.2f} leva more!")
