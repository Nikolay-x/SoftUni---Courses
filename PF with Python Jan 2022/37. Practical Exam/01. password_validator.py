import string

expected_elements = string.ascii_letters + string.digits + "_"
input_password = input()
upper_count = 0
lower_count = 0
digit_count = 0

while True:
    line = input().split(" ")
    if line[0] == "Complete":
        break
    if line[0] == "Make":
        if line[1] == "Upper":
            index = int(line[2])
            if 0 <= index < len(input_password) and input_password[index].isalpha():
                input_password = input_password[:index] + input_password[index].upper() + input_password[index + 1:]
                print(input_password)
        if line[1] == "Lower":
            index = int(line[2])
            if 0 <= index < len(input_password) and input_password[index].isalpha():
                input_password = input_password[:index] + input_password[index].lower() + input_password[index + 1:]
                print(input_password)
    if line[0] == "Insert":
        index = int(line[1])
        char = line[2]
        if 0 <= index < len(input_password):
            input_password = input_password[:index] + char + input_password[index:]
            print(input_password)
    if line[0] == "Replace":
        char = line[1]
        value = int(line[2])
        if char in input_password:
            new_char = chr(ord(char) + value)
            if char in input_password:
                input_password = input_password.replace(char, new_char)
                print(input_password)
    if line[0] == "Validation":
        if len(input_password) < 8:
            print("Password must be at least 8 characters long!")
        for ch in input_password:
            if ch not in expected_elements:
                print("Password must consist only of letters, digits and _!")
        for ch in input_password:
            if ch.isupper():
                upper_count += 1
            if ch.islower():
                lower_count += 1
            if ch.isdigit():
                digit_count += 1
        if upper_count == 0:
            print("Password must consist at least one uppercase letter!")
        if lower_count == 0:
            print("Password must consist at least one lowercase letter!")
        if digit_count == 0:
            print("Password must consist at least one digit!")
