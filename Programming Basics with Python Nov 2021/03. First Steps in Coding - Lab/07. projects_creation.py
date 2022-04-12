# 7.Изготвяне на проекти
# Напишете програма, която изчислява колко часа ще са необходими на един архитект, за да изготви проектите на няколко строителни обекта. Изготвянето на един проект отнема три часа.
# Вход
# От конзолата се четат 2 реда:
# 1.Името на архитекта - текст
# 2.Брой на проектите, които трябва да изготви - цяло число в интервала [0 … 100]
# Изход
# На конзолата се отпечатва:
# "The architect {името на архитекта} will need {необходими часове} hours to complete {брой на проектите} project/s."
#
# вход
# George
# 4
#
# изход
# The architect George will need 12 hours to complete 4 project/s.

architect_name = input()
projects_number = int(input())
hours_needed = projects_number * 3

print(f"The architect {architect_name} will need {hours_needed} hours to complete {projects_number} project/s.")
