# 1.Четене на думи
# Напишете програма, която чете текст от конзолата(стринг) и го принтира, докато не получи командата "Stop".
#
# вход
# Nakov
# SoftUni
# Sofia
# Bulgaria
# SomeText
# Stop
# AfterStop
# Europe
# HelloWorld
#
# изход
# Nakov
# SoftUni
# Sofia
# Bulgaria
# SomeText
#
# # while True:
# #     text = input()
# #     if text == "Stop":
# #         break
# #     print(text)

text = input()
print("")

while text != "Stop":
    print(text)
    text = input()
