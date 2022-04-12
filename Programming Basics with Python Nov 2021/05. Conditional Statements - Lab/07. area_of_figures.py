# 7.Лица на фигури
# Да се напише програма, в която потребителят въвежда вида и размерите на геометрична фигура и пресмята лицето й. Фигурите са четири вида: квадрат (square), правоъгълник (rectangle), кръг (circle) и триъгълник (triangle). На първия ред на входа се чете вида на фигурата (текст със следните възможности: square, rectangle, circle или triangle).
# Ако фигурата е квадрат (square): на следващия ред се чете едно дробно число - дължина на страната му
# Ако фигурата е правоъгълник (rectangle): на следващите два реда четат две дробни числа - дължините на страните му
# Ако фигурата е кръг (circle): на следващия ред чете едно дробно число - радиусът на кръга
# Ако фигурата е триъгълник (triangle): на следващите два реда четат две дробни числа - дължината на страната му и дължината на височината към нея
# Резултатът да се закръгли до 3 цифри след десетичната запетая.
#
# вход
# square
# 5
#
# изход
# 25.000

from math import pi

figure_type = str(input())
result = 0

if figure_type == "square":
    a = float(input())
    result = a * a
elif figure_type == "rectangle":
    a = float(input())
    b = float(input())
    result = a * b
elif figure_type == "circle":
    radius = float(input())
    result = pi * (radius ** 2)
elif figure_type == "triangle":
    a = float(input())
    ha = float(input())
    result = a * ha / 2

print(f"{result:.3f}")
