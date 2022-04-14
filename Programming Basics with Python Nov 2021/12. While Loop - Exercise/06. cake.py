# 6.Торта
# Поканени сте на 30-ти рожден ден, на който рожденикът черпи с огромна торта. Той обаче не знае колко парчета могат да си вземат гостите от нея. Вашата задача е да напишете програма, която изчислява броя на парчетата, които гостите са взели преди тя да свърши. Ще получите размерите на тортата (широчина и дължина – цели числа и след това на всеки ред, до получаване на командата "STOP" или докато не свърши тортата, броят на парчетата, които гостите вземат от нея. Всяко парче торта е с размер 1х1 см.
# Да се отпечата на конзолата един от следните редове:
# "{брой парчета} pieces are left." - ако стигнете до STOP и не са свършили парчетата торта;
# "No more cake left! You need {брой недостигащи парчета} pieces more."
#
# Вход
# 10
# 10
# 20
# 20
# 20
# 20
# 21
#
# Изход
# No more cake left! You need 1 pieces more.

cake_width = int(input())
cake_length = int(input())

cake_pcs = cake_width * cake_length
total_pcs = 0

while True:

    cake_pcs_count = input()

    if cake_pcs_count != "STOP":
        cake_pcs_count = int(cake_pcs_count)
        total_pcs += cake_pcs_count
    else:
        break

    if total_pcs > cake_pcs:
        break

if total_pcs <= cake_pcs:
    print(f"{cake_pcs - total_pcs} pieces are left.")
else:
    print(f"No more cake left! You need {total_pcs - cake_pcs} pieces more.")
