# 5.Пътешествие
# Млад програмист разполага с определен бюджет и свободно време в даден сезон. Напишете програма, която да приема на входа бюджета и сезона, а на изхода да изкарва къде ще почива програмистът и колко ще похарчи.
# Бюджетът определя дестинацията, а сезонът - колко от бюджета ще изхарчи. Ако е лято ще почива на къмпинг, а зимата в хотел. Ако е в Европа, независимо от сезона, ще почива в хотел. Всеки къмпинг или хотел, според дестинацията, има собствена цена, която отговаря на даден процент от бюджета:
# При 100 лв. или по-малко - някъде в България:
# oЛято - 30% от бюджета;
# oЗима - 70% от бюджета.
# При 1000 лв. или по малко - някъде на Балканите:
# oЛято - 40% от бюджета;
# oЗима - 80% от бюджета.
# При повече от 1000 лв. - някъде из Европа:
# oПри пътуване из Европа, независимо от сезона, ще похарчи 90% от бюджета.
# Вход
# Входът се чете от конзолата и се състои от два реда, въведени от потребителя:
# Бюджет - реално число;
# Един от двата възможни сезона - "summer” или "winter”.
# Изход
# На конзолата трябва да се отпечатат два реда:
#  "Somewhere in [дестинация]" измежду "Bulgaria", "Balkans" и "Europe"
# "{Вид почивка} - {Похарчена сума}":
# oПочивката може да е между "Camp" и "Hotel"
# oСумата трябва да бъде форматирана с точност до вторият знак след десетичната запетая
#
# вход
# 50
# summer
#
# изход
# Somewhere in Bulgaria
# Camp - 15.00

budget = float(input())
season = input()

destination = ""
place_to_stay = ""
expenses = 0

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        expenses = budget * 0.3
        place_to_stay = 'Camp'
    elif season == 'winter':
        expenses = budget * 0.7
        place_to_stay = 'Hotel'
elif 100 < budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        expenses = budget * 0.4
        place_to_stay = 'Camp'
    elif season == 'winter':
        expenses = budget * 0.8
        place_to_stay = 'Hotel'
elif budget > 1000:
    destination = 'Europe'
    if season == 'summer':
        expenses = budget * 0.9
        place_to_stay = 'Hotel'
    elif season == 'winter':
        expenses = budget * 0.9
        place_to_stay = 'Hotel'

print(f'Somewhere in {destination}')
print(f'{place_to_stay} - {expenses:.2f}')
