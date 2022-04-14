# 6.Сватбени места
# Младоженците искат да направят списък кой на кое място ще седи на сватбената церемония. Местата са разделени на различни сектори. Секторите са главните латински букви като започват от A. Във всеки сектор има определен брой редове. От конзолата се чете броят на редовете в първия сектор (A), като във всеки следващ сектор редовете се увеличават с 1. На всеки ред има определен брой места - тяхната номерация е представена с малките латински букви. Броя на местата на нечетните редове се прочита от конзолата, а на четните редове местата са с 2 повече.
# Вход
# От конзолата се четaт 3 реда:
# Последния сектор от секторите - символ (B-Z)
# Броят на редовете в първия сектор - цяло число (1-100)
# Броят на местата на нечетен ред - цяло число (1-24)
# Изход
# Да се отпечата на конзолата всяко място на отделен ред по следния формат:
# {сектор}{ред}{място}
# Накрая трябва да отпечата броя на всички места.
#
# Вход
# B
# 3
# 2
#
# Изход
# A1a
# A1b
# A2a
# A2b
# A2c
# A2d
# A3a
# A3b
# B1a
# B1b
# B2a
# B2b
# B2c
# B2d
# B3a
# B3b
# B4a
# B4b
# B4c
# B4d
# 20
#
# # last_sector = input()
# # sector_a_rows = int(input())
# # odd_rows_seats = int(input())
# #
# # seats_count = 0
# # first_sector = "A"
# # first_seat = "a"
# #
# # for sector in range(ord(first_sector), ord(last_sector) +1):
# #     for rows in range(1, sector_a_rows +1):
# #         if rows % 2 != 0:
# #             for seats in range(ord(first_seat), ord(first_seat) + odd_rows_seats):
# #                 print(f"{chr(sector)}{rows}{chr(seats)}")
# #                 seats_count += 1
# #         elif rows % 2 == 0:
# #             for seats in range(ord(first_seat), ord(first_seat) + odd_rows_seats + 2):
# #                 print(f"{chr(sector)}{rows}{chr(seats)}")
# #                 seats_count += 1
# #     sector_a_rows += 1
# # print(seats_count)

last_sector = input()
sector_a_rows = int(input())
odd_rows_seats = int(input())

seats_count = 0

for sector in range(ord("A"), ord(last_sector) +1):
    for rows in range(1, sector_a_rows +1):
        if rows % 2 != 0:
            for seats in range(ord("a"), ord("a") + odd_rows_seats):
                print(f"{chr(sector)}{rows}{chr(seats)}")
                seats_count += 1
        elif rows % 2 == 0:
            for seats in range(ord("a"), ord("a") + odd_rows_seats + 2):
                print(f"{chr(sector)}{rows}{chr(seats)}")
                seats_count += 1
    sector_a_rows += 1
print(seats_count)
