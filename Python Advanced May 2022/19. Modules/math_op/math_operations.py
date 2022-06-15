def operations(line):
    line = line.split(" ")
    number1 = float(line[0])
    sign = line[1]
    number2 = int(line[2])
    result = 0

    if sign == "/":
        result = number1 / number2
    if sign == "*":
        result = number1 * number2
    if sign == "-":
        result = number1 - number2
    if sign == "+":
        result = number1 + number2
    if sign == "^":
        result = number1 ** 2

    print(f"{result:.2f}")
