# 7.Доставка на храна
# Ресторант отваря врати и предлага няколко менюта на преференциални цени:
# •Пилешко меню –  10.35 лв.
# •Меню с риба – 12.40 лв.
# •Вегетарианско меню  – 8.15 лв.
# Напишете програма, която изчислява колко ще струва на група хора да си поръчат храна за вкъщи.
# Групата ще си поръча и десерт, чиято цена е равна на 20% от общата сметка (без доставката).
# Цената на доставка е 2.50 лв и се начислява най-накрая.
# Вход
# От конзолата се четат 3 реда:
# Брой пилешки менюта – цяло число в интервала [0 … 99]
# Брой менюта с риба – цяло число в интервала [0 … 99]
# Брой вегетариански менюта – цяло число в интервала [0 … 99]
# Изход
# Да се отпечата на конзолата един ред:  "{цена на поръчката}"
#
# Вход
# 2
# 4
# 3
#
# Изход
# 116.2

chicken_menu_price = 10.35
fish_menu_price = 12.4
vegan_menu_price = 8.15
delivery = 2.5

chicken_menu_number = int(input())
fish_menu_number = int(input())
vegan_menu_number = int(input())

chicken_menu_total_price = chicken_menu_number * chicken_menu_price
fish_menu_total_price = fish_menu_number * fish_menu_price
vegan_menu_total_price = vegan_menu_number * vegan_menu_price
all_menus_total_price = chicken_menu_total_price + fish_menu_total_price + vegan_menu_total_price
desserts_total_price = all_menus_total_price * 0.2
order_total_sum = all_menus_total_price + desserts_total_price + delivery

print(order_total_sum)
