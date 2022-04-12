# 4.Магазин за детски играчки
# Петя има магазин за детски играчки. Тя получава голяма поръчка, която трябва да изпълни. С парите, които ще спечели иска да отиде на екскурзия.
# Цени на играчките:
# Пъзел - 2.60 лв.
# Говореща кукла - 3 лв.
# Плюшено мече - 4.10 лв.
# Миньон - 8.20 лв.
# Камионче - 2 лв.
# Ако поръчаните играчки са 50 или повече магазинът прави отстъпка 25% от общата цена. От спечелените пари Петя трябва да даде 10% за наема на магазина. Да се пресметне дали парите ще ѝ стигнат да отиде на екскурзия.
# Вход
# От конзолата се четат 6 реда:
# 1.Цена на екскурзията - реално число в интервала [1.00 … 10000.00]
# 2.Брой пъзели - цяло число в интервала [0… 1000]
# 3.Брой говорещи кукли - цяло число в интервала [0 … 1000]
# 4.Брой плюшени мечета - цяло число в интервала [0 … 1000]
# 5.Брой миньони - цяло число в интервала [0 … 1000]
# 6.Брой камиончета - цяло число в интервала [0 … 1000]
# Изход
# На конзолата се отпечатва:
# Ако парите са достатъчни се отпечатва:
# o"Yes! {оставащите пари} lv left."
# Ако парите НЕ са достатъчни се отпечатва:
# o"Not enough money! {недостигащите пари} lv needed."
#
# Резултатът трябва да се форматира до втория знак след десетичната запетая.
#
# Вход
# 40.8
# 20
# 25
# 30
# 50
# 10
#
# Изход
# Yes! 418.20 lv left.

tour_price = float(input())
puzzles_number = int(input())
dolls_number = int(input())
bears_number = int(input())
minions_number = int(input())
trucks_number = int(input())

toys_price = puzzles_number * 2.6 + dolls_number * 3 + bears_number * 4.1 + \
              minions_number * 8.2 + trucks_number * 2
toys_number = puzzles_number + dolls_number + bears_number + minions_number + trucks_number

if toys_number >= 50:
    discount = toys_price * 0.25
else:
    discount = 0

final_price = toys_price - discount
rent = final_price * 0.1
total_profit = final_price - rent

if total_profit - tour_price >= 0:
    print(f"Yes! {(total_profit - tour_price):.2f} lv left.")
else:
    print(f"Not enough money! {(abs(total_profit - tour_price)):.2f} lv needed.")
