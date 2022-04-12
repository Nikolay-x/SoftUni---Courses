# 3.Калкулатор депозити
# Напишете програма, която изчислява каква сума ще получите в края на депозитния период при определен лихвен процент. Използвайте следната формула:
# сума = депозирана сума  + срок на депозита * ((депозирана сума * годишен лихвен процент ) / 12)
# Вход
# От конзолата се четат 3 реда:
# 1.Депозирана сума – реално число в интервала [100.00 … 10000.00]
# 2.Срок на депозита (в месеци) – цяло число в интервала [1…12]
# 3.Годишен лихвен процент – реално число в интервала [0.00 …100.00]
# Изход
# Да се отпечата на конзолата сумата в края на срока.
#
# Вход
# 200
# 3
# 5.7
#
# Изход
# 202.85

deposit = float(input())
deposit_duration_months = int(input())
annual_interest_percentage = float(input())

annual_interest_sum = deposit * annual_interest_percentage / 100
monthly_interest_sum = annual_interest_sum / 12
maturity_date_sum = deposit + deposit_duration_months * monthly_interest_sum

print(maturity_date_sum)
