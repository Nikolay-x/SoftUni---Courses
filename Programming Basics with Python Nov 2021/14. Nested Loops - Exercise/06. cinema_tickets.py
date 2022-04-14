# 6.Билети за кино
# Вашата задача е да напишете програма, която да изчислява процента на билетите за всеки тип от продадените билети: студентски(student), стандартен(standard) и детски(kid), за всички прожекции. Трябва да изчислите и колко процента от залата е запълнена за всяка една прожекция.
# Вход
# Входът е поредица от цели числа и текст:
# На първия ред до получаване на командата "Finish" - име на филма – текст
# На втори ред – свободните места в салона за всяка прожекция – цяло число [1 … 100]
# За всеки филм, се чете по един ред до изчерпване на свободните места в залата или до получаване на командата "End":
# oТипа на закупения билет - текст ("student", "standard", "kid")
# Изход
# На конзолата трябва да се печатат следните редове:
# След всеки филм да се отпечата, колко процента от кино залата е пълна
# "{името на филма} - {процент запълненост на залата}% full."
# При получаване на командата "Finish" да се отпечатат четири реда:
# o"Total tickets: {общият брой закупени билети за всички филми}"
# o"{процент на студентските билети}% student tickets."
# o"{процент на стандартните билети}% standard tickets."
# o"{процент на детските билети}% kids tickets."
#
# Вход
# Taxi
# 10
# standard
# kid
# student
# student
# standard
# standard
# End
# Scary Movie
# 6
# student
# student
# student
# student
# student
# student
# Finish
#
# Изход
# Taxi - 60.00% full.
# Scary Movie - 100.00% full.
# Total tickets: 12
# 66.67% student tickets.
# 25.00% standard tickets.
# 8.33% kids tickets.

movie_name = input()

student_ticket_count = 0
standard_ticket_count = 0
kid_ticket_count = 0

while movie_name != "Finish":

    free_seats = int(input())
    seats_taken = 0
    ticket_type = input()

    while ticket_type != "End":

        if ticket_type == "student":
            student_ticket_count += 1
        elif ticket_type == "standard":
            standard_ticket_count += 1
        elif ticket_type == "kid":
            kid_ticket_count += 1

        seats_taken += 1
        if free_seats - seats_taken == 0:
            break
        ticket_type = input()

    print(f"{movie_name} - {(seats_taken / free_seats * 100):.2f}% full.")
    movie_name = input()

all_tickets = student_ticket_count + standard_ticket_count + kid_ticket_count
print(f"Total tickets: {all_tickets}")
print(f"{(student_ticket_count / all_tickets * 100):.2f}% student tickets.")
print(f"{(standard_ticket_count / all_tickets * 100):.2f}% standard tickets.")
print(f"{(kid_ticket_count / all_tickets * 100):.2f}% kids tickets.")
