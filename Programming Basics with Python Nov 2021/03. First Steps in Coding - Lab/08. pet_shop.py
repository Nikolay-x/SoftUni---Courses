# Напишете програма, която пресмята нужните разходи за закупуването на храна за кучета и котки.  Храната се пазарува от зоомагазин, като една опаковка храна за кучета е на цена 2.50 лв, а опаковка храна за котки струва 4 лв.
# Вход
# От конзолата се четат 2 реда:
# 1.Броят на опаковките храна за кучета – цяло число в интервала [0… 100]
# 2.Броят на опаковките храна за котки –  цяло число в интервала [0… 100]
# Изход
# На конзолата се отпечатва:
# "{крайната сума} lv."
#
# вход
# 5
# 4
#
# изход
# 28.5 lv.

dog_food_package_price = 2.5
cat_food_package_price = 4

dog_food_package_number = int(input())
cat_food_package_number = int(input())

total_sum = dog_food_package_number * dog_food_package_price + cat_food_package_number * cat_food_package_price

print(f'{total_sum} lv.')
