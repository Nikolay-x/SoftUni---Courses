# 10.*Winning Ticket
# The lottery is exciting. However, checking a million tickets for winnings only by hand is not. So, you are given the task of creating a program that automatically checks if a ticket is a winner.
# You are given a collection of tickets separated by commas and spaces (one or many). You need to check each ticket to see if it has a winning combination of symbols:
# A valid ticket has exactly 20 characters.
# A winning ticket is a valid one, containing one of the symbols '@', '#', '$' or '^' uninterruptedly repeated at least 6 times in both halves of the tickets.
# In order to win a Jackpot, the ticket should contain the same winning symbol 10 times on both sides
# An example of a valid winning ticket:
# "Cash$$$$$$Ca$$$$$$sh"
# An example of a Jackpot winning valid ticket:
# "$$$$$$$$$$$$$$$$$$$$"
# Input
# The input will be read from the console. The input consists of a single line containing all tickets separated by commas and one or more white spaces in the format:
# "{ticket}, {ticket}, … {ticket}"
# Output
# Print the result for every ticket in the order of their appearance, each on a separate line in the format:
# If the ticket is invalid: "invalid ticket"
# If the ticket is valid, but it is not winning: "ticket "{ticket}" - no match"
# If the ticket is valid and winning, but not a Jackpot:
# "ticket "{ticket}" - {uninterrupted_match_length}{match_symbol}"
# It the ticket hits the Jackpot:
# "ticket "{ticket}" - {uninterrupted_match_length}{match_symbol} Jackpot!"
# Constrains
# Number of tickets will be in range [0 … 100]
#
# Input
# Cash$$$$$$Ca$$$$$$sh
#
# Output
# ticket "Cash$$$$$$Ca$$$$$$sh" - 6$

# def additional_func(partition):
#     current_max_num = 0
#     special_char = ''
#
#     for ch in partition:
#         if ch != special_char:
#             if current_max_num >= 6:
#                 break
#             current_max_num = 1
#             special_char = ch
#         else:
#             current_max_num += 1
#     return [current_max_num, special_char]
#
#
# def ticket_validator(ticket):
#     ticket_condition = ''
#
#     if len(ticket) != 20:
#         ticket_condition = "invalid ticket"
#     elif ticket[0] * 20 == ticket and ticket[0] in '@#$^':
#         ticket_condition = f'ticket "{ticket}" - 10{ticket[0]} Jackpot!'
#     else:
#         data_source = ''
#         if additional_func(ticket[0:10]) > additional_func(ticket[10:]):
#             data_source = additional_func(ticket[10:])
#         else:
#             data_source = additional_func(ticket[0:10])
#
#         number_of_special_signs = data_source[0]
#         special_sign = data_source[1]
#
#         if number_of_special_signs < 6 or special_sign not in '@#$^':
#             ticket_condition = f'ticket "{ticket}" - no match'
#         else:
#             ticket_condition = f'ticket "{ticket}" - {number_of_special_signs}{special_sign}'
#
#     return ticket_condition
#
#
# def winning_ticket(data):
#     for ticket in data:
#         print(ticket_validator(ticket))
#
#
# tickets_info = input()
# data = [x.strip() for x in tickets_info.split(',')]
# winning_ticket(data)


tickets = [ticket.strip() for ticket in input().split(",")]

for ticket in tickets:
    first_ticket_half = ticket[:int(len(ticket) / 2)]
    second_ticket_half = ticket[int(len(ticket) / 2):]
    total_list_ch = []
    total_list_num = []

    if len(ticket) == 20:
        temp_count_1 = 0
        temp_count_list_1 = [0]
        temp_count_2 = 0
        temp_count_list_2 = [0]

        for i in range(len(first_ticket_half)):
            if first_ticket_half[i] == "@":
                temp_count_1 += 1
                winning_symbol_1 = "@"
                if i == len(first_ticket_half) - 1:
                    temp_count_list_1.append(temp_count_1)
            else:
                if temp_count_1 != 0:
                    temp_count_list_1.append(temp_count_1)
                    temp_count_1 = 0
            if second_ticket_half[i] == "@":
                temp_count_2 += 1
                winning_symbol_2 = "@"
                if i == len(second_ticket_half) - 1:
                    temp_count_list_2.append(temp_count_2)
            else:
                if temp_count_2 != 0:
                    temp_count_list_2.append(temp_count_2)
                    temp_count_2 = 0

        count_1 = max(temp_count_list_1)
        count_2 = max(temp_count_list_2)
        count = min(count_1, count_2)

        if count != 0:
            total_list_ch.append("@")
            total_list_num.append(count)

        temp_count_1 = 0
        temp_count_list_1 = [0]
        temp_count_2 = 0
        temp_count_list_2 = [0]
        for i in range(len(first_ticket_half)):
            if first_ticket_half[i] == "#":
                temp_count_1 += 1
                winning_symbol_1 = "#"
                if i == len(first_ticket_half) - 1:
                    temp_count_list_1.append(temp_count_1)
            else:
                if temp_count_1 != 0:
                    temp_count_list_1.append(temp_count_1)
                    temp_count_1 = 0
            if second_ticket_half[i] == "#":
                temp_count_2 += 1
                winning_symbol_2 = "#"
                if i == len(second_ticket_half) - 1:
                    temp_count_list_2.append(temp_count_2)
            else:
                if temp_count_2 != 0:
                    temp_count_list_2.append(temp_count_2)
                    temp_count_2 = 0

        count_1 = max(temp_count_list_1)
        count_2 = max(temp_count_list_2)
        count = min(count_1, count_2)

        if count != 0:
            total_list_ch.append("#")
            total_list_num.append(count)

        temp_count_1 = 0
        temp_count_list_1 = [0]
        temp_count_2 = 0
        temp_count_list_2 = [0]
        for i in range(len(first_ticket_half)):
            if first_ticket_half[i] == "$":
                temp_count_1 += 1
                winning_symbol_1 = "$"
                if i == len(first_ticket_half) - 1:
                    temp_count_list_1.append(temp_count_1)
            else:
                if temp_count_1 != 0:
                    temp_count_list_1.append(temp_count_1)
                    temp_count_1 = 0
            if second_ticket_half[i] == "$":
                temp_count_2 += 1
                winning_symbol_2 = "$"
                if i == len(second_ticket_half) - 1:
                    temp_count_list_2.append(temp_count_2)
            else:
                if temp_count_2 != 0:
                    temp_count_list_2.append(temp_count_2)
                    temp_count_2 = 0

        count_1 = max(temp_count_list_1)
        count_2 = max(temp_count_list_2)
        count = min(count_1, count_2)

        if count != 0:
            total_list_ch.append("$")
            total_list_num.append(count)

        temp_count_1 = 0
        temp_count_list_1 = [0]
        temp_count_2 = 0
        temp_count_list_2 = [0]
        for i in range(len(first_ticket_half)):
            if first_ticket_half[i] == "^":
                temp_count_1 += 1
                winning_symbol_1 = "^"
                if i == len(first_ticket_half) - 1:
                    temp_count_list_1.append(temp_count_1)
            else:
                if temp_count_1 != 0:
                    temp_count_list_1.append(temp_count_1)
                    temp_count_1 = 0
            if second_ticket_half[i] == "^":
                temp_count_2 += 1
                winning_symbol_2 = "^"
                if i == len(second_ticket_half) - 1:
                    temp_count_list_2.append(temp_count_2)
            else:
                if temp_count_2 != 0:
                    temp_count_list_2.append(temp_count_2)
                    temp_count_2 = 0

        count_1 = max(temp_count_list_1)
        count_2 = max(temp_count_list_2)
        count = min(count_1, count_2)

        if count != 0:
            total_list_ch.append("^")
            total_list_num.append(count)

        final_count = 0

        for i in range(len(total_list_num)):
            if total_list_num[i] > final_count:
                final_count = total_list_num[i]
                final_ch = total_list_ch[i]

        if 6 <= final_count <= 9:
            print(f'ticket "{ticket}" - {final_count}{final_ch}')
        elif final_count == 10:
            print(f'ticket "{ticket}" - {final_count}{final_ch} Jackpot!')
        else:
            print(f'ticket "{ticket}" - no match')

    else:
        print("invalid ticket")
