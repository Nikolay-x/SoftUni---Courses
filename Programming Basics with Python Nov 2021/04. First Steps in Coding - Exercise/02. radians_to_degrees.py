# 2.Конвертор: от радиани в градуси
# Напишете програма, която чете ъгъл в радиани (десетично число) и го преобразува в градуси. Използвайте формулата: градус = радиан * 180 / π. Числото π в Python може да достъпите чрез модула math. За да ползвате функционалността му, първо трябва да включите констатата pi.
#
# вход
# 3.1416
#
# изход
# 180.0004209182994

from math import pi
radians = float(input())
degrees = radians * 180 / pi

print(degrees)
