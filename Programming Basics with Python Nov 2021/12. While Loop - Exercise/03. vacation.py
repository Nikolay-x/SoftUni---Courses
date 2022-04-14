# 3.Почивка
# Джеси е решила да събира пари за екскурзия и иска от вас да ѝ помогнете да разбере дали ще успее да събере необходимата сума. Тя спестява или харчи част от парите си всеки ден. Ако иска да похарчи повече от наличните си пари, то тя ще похарчи колкото има и ще ѝ останат 0 лева.
# Вход
# От конзолата се четат:
# Пари, нужни за екскурзията - реално число;
# Налични пари - реално число.
# След това многократно се четат по два реда:
# Вид действие – текст с две възможности: "spend" или "save";
# Сумата, която ще спести/похарчи - реално число.
# Изход
# Програмата трябва да приключи при следните случаи:
# Ако 5 последователни дни Джеси само харчи, на конзолата да се изпише:
# o"You can't save the money."
# o"{Общ брой изминали дни}"
# Ако Джеси събере парите за почивката, на конзолата се изписва:
# o"You saved the money for {общ брой изминали дни} days."
#
# Вход
# 2000
# 1000
# spend
# 1200
# save
# 2000
#
# Изход
# You saved the money for 2 days.

trip_price = float(input())
money_balance = float(input())

spend_days_count = 0
days_count = 0

while money_balance < trip_price:
    operation = input()
    day_sum = float(input())
    days_count += 1

    if operation == "spend":
        spend_days_count += 1
        if money_balance >= day_sum:
            money_balance -= day_sum
        else:
            money_balance = 0
    if operation == "save":
        money_balance += day_sum
        spend_days_count = 0

    if spend_days_count == 5:
        print("You can't save the money.")
        print(f"{days_count}")
        break

if money_balance >= trip_price:
    print(f"You saved the money for {days_count} days.")
