# 3.Нов дом
# Марин и Нели си купуват къща недалеч от София. Нели толкова много обича цветята, че Ви убеждава да напишете програма, която да изчисли колко  ще им струва, за да засадят определен брой цветя и дали наличният бюджет ще им е достатъчен. Различните цветя са с различни цени:
# цвете	Роза	Далия	Лале	Нарцис	Гладиола
# Цена на брой в лева	5	3.80	2.80	3	2.50
# Съществуват следните отстъпки:
# Ако Нели купи повече от 80 Рози - 10% отстъпка от крайната цена;
# Ако Нели купи повече от 90  Далии - 15% отстъпка от крайната цена;
# Ако Нели купи повече от 80 Лалета - 15% отстъпка от крайната цена;
# Ако Нели купи по-малко от 120 Нарциса - цената се оскъпява с 15%;
# Ако Нели Купи по-малко от 80 Гладиоли - цената се оскъпява с 20%.
# От конзолата се четат 3 реда:
# Вид цветя - текст с възможности "Roses", "Dahlias", "Tulips", "Narcissus" или "Gladiolus";
# Брой цветя - цяло число;
# Бюджет - цяло число.
# Да се отпечата на конзолата на един ред:
# Ако бюджетът им е достатъчен - "Hey, you have a great garden with {броя цвета} {вид цветя} and {останалата сума} leva left.";
# Ако бюджета им е НЕ достатъчен - "Not enough money, you need {нужната сума} leva more.".
# Сумата да бъде форматирана до втория знак след десетичната запетая.
#
# Вход
# Roses
# 55
# 250
#
# Изход
# Not enough money, you need 25.00 leva more.

flower_type = input()
flower_number = int(input())
buget = int(input())

price = 0

if flower_type == "Roses":
    price = flower_number * 5
    if flower_number > 80:
        price = price - price * 0.1
elif flower_type == 'Dahlias':
    price = flower_number * 3.8
    if flower_number > 90:
        price = price - price * 0.15
elif flower_type == 'Tulips':
    price = flower_number * 2.8
    if flower_number > 80:
        price = price - price * 0.15
elif flower_type == 'Narcissus':
    price = flower_number * 3
    if flower_number < 120:
        price = price + price * 0.15
elif flower_type == 'Gladiolus':
    price = flower_number * 2.5
    if flower_number < 80:
        price = price + price * 0.2

if buget - price >= 0:
    print(f"Hey, you have a great garden with {flower_number} {flower_type} and {(buget - price):.2f} leva left.")
else:
    print(f"Not enough money, you need {(price - buget):.2f} leva more.")
