# 3.Суми прости и непрости числа
# Напишете програма, която чете от конзолата цели числа, докато не се получи команда "stop". Да се намери сумата на всички въведени прости и сумата на всички въведени непрости числа. Тъй като по дефиниция от математиката отрицателните числа не могат да бъдат прости, ако на входа се подаде отрицателно число, да се изведе следното съобщение "Number is negative.". В този случай въведено число се игнорира и не се прибавя към нито една от двете суми, а програмата продължава своето изпълнение, очаквайки въвеждане на следващо число.
# На изхода да се отпечатат на два реда двете намерени суми в следния формат:
# "Sum of all prime numbers is: {prime numbers sum}"
# "Sum of all non prime numbers is: {nonprime numbers sum}"
#
# Вход
# 3
# 9
# 0
# 7
# 19
# 4
# stop
#
# Изход
# Sum of all prime numbers is: 29
# Sum of all non prime numbers is: 13

command = input()

prime_numbers_sum = 0
non_prime_numbers_sum = 0

while command != "stop":
    is_prime = True
    number = int(command)

    if number < 0:
        print("Number is negative.")
    else:
        for i in range (2, number):
            if number % i == 0:
                is_prime = False

        if is_prime:
            prime_numbers_sum += number
        else:
            non_prime_numbers_sum += number

    command = input()

print(f"Sum of all prime numbers is: {prime_numbers_sum}")
print(f"Sum of all non prime numbers is: {non_prime_numbers_sum}")
