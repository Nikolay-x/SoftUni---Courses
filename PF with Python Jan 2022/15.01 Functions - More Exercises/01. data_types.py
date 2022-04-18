# 1.Data Types
# Write a function that, depending on the first line of the input, reads one of the following strings: "int", "real", or "string".
# If the data type is an int, multiply the number by 2.
# If the data type is real, multiply the number by 1.5 and format the result to the second decimal point.
# If the data type is a string, surround the input with "$".
# Print the result on the console.
#
# Input
# int
# 5
#
# Output
# 10

def data_types(command, n):
    if command == "int":
        result = int(n) * 2
    elif command == "real":
        result = f"{(float(n) * 1.5):.2f}"
    elif command == "string":
        result = f"${n}$"
    return result

input_line = input()
m = input()

print(data_types(input_line, m))
