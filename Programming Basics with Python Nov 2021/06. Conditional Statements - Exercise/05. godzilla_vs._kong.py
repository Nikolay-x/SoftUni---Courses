# 5.Годзила срещу Конг
# Снимките за дългоочаквания филм "Годзила срещу Конг" започват. Сценаристът Адам Уингард ви моли да напишете програма, която да изчисли, дали предвидените средства са достатъчни за снимането на филма. За снимките  ще бъдат нужни определен брой статисти, облекло за всеки един статист и декор.
# Известно е, че:
# Декорът за филма е на стойност 10% от бюджета.
# При повече от 150 статиста,  има отстъпка за облеклото на стойност 10%.
# Вход
# От конзолата се четат 3 реда:
# Ред 1.Бюджет за филма – реално число в интервала [1.00 … 1000000.00]
# Ред 2.Брой на статистите – цяло число в интервала [1 … 500]
# Ред 3.Цена за облекло на един статист – реално число в интервала [1.00 … 1000.00]
# Изход
# На конзолата трябва да се отпечатат два реда:
# Ако  парите за декора и дрехите са повече от бюджета:
# o"Not enough money!"
# o"Wingard needs {парите недостигащи за филма} leva more."
# Ако парите за декора и дрехите са по малко или равни на бюджета:
# o"Action!"
# o"Wingard starts filming with {останалите пари} leva left."
# Резултатът трябва да е форматиран до втория знак след десетичната запетая.
#
# Вход
# 20000
# 120
# 55.5
#
# Изход
# Action!
# Wingard starts filming with 11340.00 leva left.

film_budget = float(input())
extra_number = int(input())
extra_clothes_price = float(input())

decor_price = film_budget * 0.1

if extra_number > 150:
    extra_clothes_total_price = (extra_number * extra_clothes_price) * 0.9
else:
    extra_clothes_total_price = extra_number * extra_clothes_price

film_price = decor_price + extra_clothes_total_price

if film_price > film_budget:
    print(f"Not enough money!")
    print(f"Wingard needs {(film_price - film_budget):.2f} leva more.")
else:
    print(f"Action!")
    print(f"Wingard starts filming with {(film_budget - film_price):.2f} leva left.")
