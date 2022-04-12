# 8.Баскетболно оборудване
# Джеси решава, че иска да се занимава с баскетбол, но за да тренира е нужна екипировка. Напишете програма, която изчислява какви разходи ще има Джеси, ако започне да тренира, като знаете колко е таксата за тренировки по баскетбол за период от 1 година. Нужна екипировка:
# •Баскетболни кецове – цената им е 40% по-малка от таксата за една година
# •Баскетболен екип – цената му е 20% по-евтина от тази на кецовете
# •Баскетболна топка – цената ѝ е 1 / 4 от цената на баскетболния екип
# •Баскетболни аксесоари – цената им е 1 / 5 от цената на баскетболната топка
# Вход
# От конзолата се четe 1 ред:
# Годишната такса за тренировки по баскетбол – цяло число в интервала [0… 9999]
# Изход
# Да се отпечата на конзолата колко ще са разходите на Джеси, ако започне да спортува баскетбол.
#
# Вход
# 365
#
# Изход
# 811.76

annual_basketball_training_fee = int(input())

basketball_sneakers_price = annual_basketball_training_fee - annual_basketball_training_fee * 0.4
basketball_sportswear_price = basketball_sneakers_price - basketball_sneakers_price * 0.2
basketball_ball_price = basketball_sportswear_price * 0.25
basketball_accessories_price = basketball_ball_price * 0.2
basketball_training_total_sum = annual_basketball_training_fee + basketball_sneakers_price + \
                                basketball_sportswear_price + basketball_ball_price + basketball_accessories_price

print(basketball_training_total_sum)
