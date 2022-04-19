# 4.Phonebook
# Write a program that receives info from the console about people and their phone numbers.
# Each entry should have a name and a number (both strings) separated by a "-". If you receive a name that already exists in the phonebook, update its number.
# After filling the phonebook, you will receive a number – N. Your program should be able to perform a search of contact by name and print its details in the format: "{name} -> {number}". In case the contact isn't found, print: "Contact {name} does not exist."
#
# Input
# Adam-0888080808
# 2
# Mery
# Adam
#
# Output
# Contact Mery does not exist.
# Adam -> 0888080808

# def phone_book_information(number_of_lines, phone_book):
#     for x in range(number_of_lines):
#         name = input()
#         if name not in phone_book:
#             print(f"Contact {name} does not exist")
#         else:
#             print(f"{name} -> {phone_book[name]}")
#     return True
#
#
# def phonebook_info():
#     phone_book = {}
#     condition = False
#     while True:
#         contact_information = input().split("-")
#         if contact_information[0].isdigit():
#             condition = phone_book_information(int(contact_information[0]), phone_book)
#         else:
#             phone_book[contact_information[0]] = contact_information[1]
#
#         if condition:
#             break
#
#
# phonebook_info()


def phonebook():
    phonebook_dict = dict()
    while True:
        entry = input()
        if "-" not in entry:
            break
        entry = entry.split("-")
        name = entry[0]
        number = entry[1]
        phonebook_dict[name] = number

    n = int(entry)
    for i in range(n):
        searched_name = input()
        if searched_name in phonebook_dict.keys():
            print(f"{searched_name} -> {phonebook_dict[searched_name]}")
        else:
            print(f"Contact {searched_name} does not exist.")


phonebook()
