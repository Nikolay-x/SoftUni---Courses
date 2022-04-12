# 3.Клас животно
# Напишете програма, която отпечатва класа на животното според неговото име, въведено от потребителя.
# 1.dog -> mammal
# 2.crocodile, tortoise, snake -> reptile
# 3.others -> unknown
#
# Вход
# dog
#
# Изход
# mammal

animal_name = input()

if animal_name == 'dog':
    print('mammal')
elif animal_name == 'crocodile' \
        or animal_name == 'tortoise' \
        or animal_name == 'snake':
    print('reptile')
else:
    print('unknown')
