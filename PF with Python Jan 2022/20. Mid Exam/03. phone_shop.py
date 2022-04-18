phones_list = input().split(", ")

line = input()

while line != "End":
    if "Add" in line:
        l = line.split(" - ")
        phone = l[1]
        if phone not in phones_list:
            phones_list.append(phone)
    if "Remove" in line:
        l = line.split(" - ")
        phone = l[1]
        if phone in phones_list:
            phones_list.remove(phone)
    if "Bonus" in line:
        l = line.split(" - ")
        l1 = l[1].split(":")
        old_phone = l1[0]
        new_phone = l1[1]
        for i in range(len(phones_list)):
            if phones_list[i] == old_phone:
                phones_list.insert(i+1, new_phone)
    if "Last" in line:
        l = line.split(" - ")
        phone = l[1]
        if phone in phones_list:
            phones_list.remove(phone)
            phones_list.append(phone)
    line = input()

print(", ".join(phones_list))
