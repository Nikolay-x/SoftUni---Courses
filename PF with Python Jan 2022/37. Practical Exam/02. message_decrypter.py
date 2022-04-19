import re

regex = r"^(\$|\%)([A-Z][a-z]{2,})\1: \[(\d+)\]\|\[(\d+)\]\|\[(\d+)\]\|$"
n_count = int(input())

for i in range(n_count):
    line = input()
    result = ""
    matches = re.finditer(regex, line)
    for match in matches:
        valid_message = match.group()
        tag = match[2]
        first_char = int(match[3])
        second_char = int(match[4])
        third_char = int(match[5])
        decrypted_message = chr(first_char) + chr(second_char) + chr(third_char)
        result = f"{tag}: {decrypted_message}"
    if result != "":
        print(result)
    else:
        print("Valid message not found!")
