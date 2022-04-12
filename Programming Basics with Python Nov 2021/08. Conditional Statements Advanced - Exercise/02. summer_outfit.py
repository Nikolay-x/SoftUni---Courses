# 2. Лятно облекло
# Лятото е сезон с много променливо време и Виктор има нужда от вашата помощ. Напишете програма, която спрямо времето от денонощието и градусите да препоръча на Виктор какви дрехи да облече. Вашият приятел има различни планове за всеки етап от деня, които изискват и различен външен вид - може да ги видите от таблицата.
# От конзолата се четат точно два реда:
# Градусите - цяло число;
# Време от денонощието - текст с три възможности "Morning", "Afternoon" или "Evening".
# Време от денонощието / градуси
# Morning
# Afternoon
# Evening
# 10 <= градуси <= 18	Outfit = Sweatshirt
# Shoes = Sneakers	Outfit = Shirt
# Shoes = Moccasins	Outfit = Shirt
# Shoes = Moccasins
# 18 < градуси <= 24	Outfit = Shirt
# Shoes = Moccasins	Outfit = T-Shirt
# Shoes = Sandals	Outfit = Shirt
# Shoes = Moccasins
# градуси >= 25	Outfit = T-Shirt
# Shoes = Sandals	Outfit = Swim Suit
# Shoes = Barefoot	Outfit = Shirt
# Shoes = Moccasins
#
# Като изход да се отпечата на конзолата на един ред: "It's {градуси} degrees, get your {облекло} and {обувки}."
#
# Вход
# 16
# Morning
#
# Изход
# It's 16 degrees, get your Sweatshirt and Sneakers.

degrees_outside = int(input())
day_period = input()

outfit = ""
shoes = ""

if 10<= degrees_outside <= 18:
    if day_period == 'Morning':
        outfit = 'Sweatshirt'
        shoes = 'Sneakers'
    elif day_period == 'Afternoon':
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif day_period == 'Evening':
        outfit = 'Shirt'
        shoes = 'Moccasins'
elif 18 < degrees_outside <= 24:
    if day_period == 'Morning':
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif day_period == 'Afternoon':
        outfit = 'T-Shirt'
        shoes = 'Sandals'
    elif day_period == 'Evening':
        outfit = 'Shirt'
        shoes = 'Moccasins'
elif degrees_outside >= 25:
    if day_period == 'Morning':
        outfit = 'T-Shirt'
        shoes = 'Sandals'
    elif day_period == 'Afternoon':
        outfit = 'Swim Suit'
        shoes = 'Barefoot'
    elif day_period == 'Evening':
        outfit = 'Shirt'
        shoes = 'Moccasins'

print(f"It's {degrees_outside} degrees, get your {outfit} and {shoes}.")
