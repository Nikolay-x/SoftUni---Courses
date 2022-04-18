# 3.Wolf in Sheep's Clothing
# Wolves have been reintroduced to Great Britain. You are a sheep farmer and are now plagued by wolves who pretend to be sheep. Fortunately, you are good at spotting them.
# Warn the sheep in front of the wolf that it is about to be eaten. Remember that you are standing at the front of the queue, which is at the end of the list:
# [sheep, sheep, wolf, sheep, sheep] (YOU ARE HERE AT THE FRONT OF THE QUEUE)
#    4      3            2      1
# If the wolf is the closest animal to you, print "Please go away and stop eating my sheep". Otherwise, return "Oi! Sheep number N! You are about to be eaten by a wolf!" where N is the sheep's position in the queue.
# Note: there will always be exactly one wolf on the list.
# Input
# The input will be a single string containing the animals separated by a comma and a single space ", "
#
# Input
# sheep, sheep, wolf
#
# Output
# Please go away and stop eating my sheep

herd = input()

herd_list = herd.split(", ")

for i in range(len(herd_list)):
    if herd_list[i] == "wolf":
        if i == len(herd_list) - 1:
            print("Please go away and stop eating my sheep")
        else:
            print(f"Oi! Sheep number {len(herd_list) - i- 1}! You are about to be eaten by a wolf!")
    else:
        continue
