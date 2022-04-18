friends_list = input().split(", ")

line = input()
blacklisted_count = 0
lost_names_count = 0

while line != "Report":
    if "Blacklist" in line:
        l = line.split(" ")
        name = l[1]
        temp_count = 0
        for n in range(len(friends_list)):
            if friends_list[n] == name:
                print(f"{name} was blacklisted.")
                friends_list[n] = "Blacklisted"
                temp_count += 1
                blacklisted_count += 1
        if temp_count == 0:
            print(f"{name} was not found.")
    if "Error" in line:
        l = line.split(" ")
        index = int(l[1])
        if 0 <= index < len(friends_list):
            if friends_list[index] != "Blacklisted" and friends_list[index] != "Lost":
                print(f"{friends_list[index]} was lost due to an error.")
                friends_list[index] = "Lost"
                lost_names_count += 1
    if "Change" in line:
        l = line.split(" ")
        index = int(l[1])
        new_name = l[2]
        if 0 <= index < len(friends_list):
            print(f"{friends_list[index]} changed his username to {new_name}.")
            friends_list[index] = new_name
    line = input()

print(f"Blacklisted names: {blacklisted_count}")
print(f"Lost names: {lost_names_count}")
print(" ".join(friends_list))
