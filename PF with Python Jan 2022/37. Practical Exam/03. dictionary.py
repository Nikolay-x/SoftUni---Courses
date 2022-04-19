lines = input().split(" | ")

words_task3_dict = dict()

for line in lines:
    line = line.split(": ")
    word = line[0]
    definition = line[1]
    if word not in words_task3_dict:
        words_task3_dict[word] = [definition]
    else:
        words_task3_dict[word].append(definition)

searched_words = input().split(" | ")
command = input()

if command == "Test":
    for word in searched_words:
        if word in words_task3_dict:
            print(f"{word}:")
            for d in words_task3_dict[word]:
                print(f" -{d}")
if command == "Hand Over":
    for word in words_task3_dict:
        print(f"{word}", end=" ")
