# 2.Парола
# Напишете програма, която първоначално прочита име и парола на потребителски профил. След това чете парола за вход.
# при въвеждане на грешна парола: потребителя да се подкани да въведе нова парола.
# при въвеждане на правилна парола: отпечатваме "Welcome {username}!".
#
# вход
# Nakov
# 1234
# pass
# 1324
# 1234
#
# изход
# Welcome Nakov!

userid = input()
password = input()

data = input()

while data != password:
    data = input()

print(f"Welcome {userid}!")