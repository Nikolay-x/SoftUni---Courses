# 6.Оскари
# Поканени сте от академията да напишете софтуер, който да пресмята точките за актьор/актриса. Академията ще ви даде първоначални точки за актьора. След това всеки оценяващ ще дава своята оценка. Точките, които актьора получава се формират от: дължината на името на оценяващия умножено по точките, които дава делено на две.
# Ако резултатът в някой момент надхвърли 1250.5 програмата трябва да прекъсне и да се отпечата, че дадения актьор е получил номинация.
# Вход
# •Име на актьора - текст
# •Точки от академията - реално число в интервала [2.0... 450.5]
# •Брой оценяващи n - цяло число в интервала[1… 20]
# На следващите n-на брой реда:
# oИме на оценяващия - текст
# oТочки от оценяващия - реално число в интервала [1.0... 50.0]
# Изход
# Да се отпечата на конзолата един ред:
# Ако точките са над 1250.5:
# "Congratulations, {име на актьора} got a nominee for leading role with {точки}!"
# Ако точките не са достатъчни:
# 	"Sorry, {име на актьора} you need {нужни точки} more!"
# Резултатът да се форматирана до първата цифра след десетичния знак!
#
# Вход
# Zahari Baharov
# 205
# 4
# Johnny Depp
# 45
# Will Smith
# 29
# Jet Lee
# 10
# Matthew Mcconaughey
# 39
#
# Изход
# Sorry, Zahari Baharov you need 247.5 more!

actor_name = input()
academy_points = float(input())
jury_count = int(input())

total_points = academy_points

for i in range(1, jury_count +1):
    jury_name = input()
    jury_points = float(input())
    total_points += len(jury_name) * jury_points / 2
    if total_points > 1250.5:
        print("")
        print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!")
        break

if total_points <= 1250.5:
    print(f"Sorry, {actor_name} you need {(1250.5 - total_points):.1f} more!")
