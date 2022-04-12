# 4.Лодка за риболов
# Тони и приятели много обичат да ходят за риба и са толкова запалени по риболова, че решават да отидат на риболов с кораб. Цената за наема на кораба зависи от сезона и броя рибари:
# В зависимост от сезона:
# Цената за наем на кораба през пролетта е  3000 лв.;
# Цената за наем на кораба през лятото и есента е  4200 лв.;
# Цената за наем на кораба през зимата е  2600 лв.
# В зависимост от броя на групата има различна отстъпка:
# Ако групата е до 6 човека включително  -  отстъпка от 10%;
# Ако групата е от 7 до 11 човека включително  -  отстъпка от 15%;
# Ако групата е от 12 нагоре  -  отстъпка от 25%.
# Рибарите ползват допълнително 5% отстъпка, ако са четен брой, освен ако не е есен - тогава нямат допълнителна отстъпка, която се начислява след като се приспадне отстъпката по горните критерии.
# Напишете програма, която да пресмята дали рибарите ще съберат достатъчно пари.
# Вход
# От конзолата се четат три реда:
# Бюджет на групата - цяло число;
# Сезон -  текст: "Spring", "Summer", "Autumn" или "Winter";
# Брой рибари - цяло число.
# Изход
# На конзолата да се отпечата следното:
# Ако бюджетът е достатъчен:
# "Yes! You have {останалите пари} leva left."
# Ако бюджетът НЕ Е достатъчен:
# "Not enough money! You need {сумата, която не достига} leva."
# Сумите трябва да са форматирани с точност до два знака след десетичната запетая.
#
# Вход
# 3000
# Summer
# 11
#
# Изход
# Not enough money! You need 570.00 leva.

budget = int(input())
season = input()
fishermen_number = int(input())

price = 0

if season == 'Spring':
    price = 3000
    if fishermen_number <= 6:
        price -= price * 0.1
    elif 7 <= fishermen_number <= 11:
        price -= price * 0.15
    elif fishermen_number >= 12:
        price -= price * 0.25
elif season == 'Summer':
    price = 4200
    if fishermen_number <= 6:
        price -= price * 0.1
    elif 7 <= fishermen_number <= 11:
        price -= price * 0.15
    elif fishermen_number >= 12:
        price -= price * 0.25
elif season == 'Autumn':
    price = 4200
    if fishermen_number <= 6:
        price -= price * 0.1
    elif 7 <= fishermen_number <= 11:
        price -= price * 0.15
    elif fishermen_number >= 12:
        price -= price * 0.25
elif season == 'Winter':
    price = 2600
    if fishermen_number <= 6:
        price -= price * 0.1
    elif 7 <= fishermen_number <= 11:
        price -= price * 0.15
    elif fishermen_number >= 12:
        price -= price * 0.25

if season == "Spring" or season == "Summer" or season == "Winter":
    if fishermen_number % 2 == 0:
        price -= price * 0.05

if budget - price >= 0:
    print(f"Yes! You have {(budget - price):.2f} leva left.")
else:
    print(f'Not enough money! You need {(price - budget):.2f} leva.')
