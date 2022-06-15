# 2.ASCII Art
# Write a program that encrypts given words by using the characters: "-|_/\()" to structure the word. Use the pyfiglet module. You can read more about it here - https://www.geeksforgeeks.org/python-ascii-art-using-pyfiglet-module/
# Directions
# 1.First you need to install the module that we will be using. To install it go to Setting --> Project <your_project_name> --> Project Interpreter --> + --> search for pyfiglet --> install package.
# 2.Import the module
# 3.Implement the logic. We will be using the figlet_format method
#
# Input
# Python 3.8
#
# Output
#  ____        _   _                   _____  ___
# |  _ \ _   _| |_| |__   ___  _ __   |___ / ( _ )
# | |_) | | | | __| '_ \ / _ \| '_ \    |_ \ / _ \
# |  __/| |_| | |_| | | | (_) | | | |  ___) | (_) |
# |_|    \__, |\__|_| |_|\___/|_| |_| |____(_)___/
#        |___/

from pyfiglet import figlet_format


def print_art(msg):
    ascii_art1 = figlet_format(msg, font="isometric1")
    ascii_art2 = figlet_format(msg, font="alligator")
    ascii_art3 = figlet_format(msg, font="dotmatrix")
    ascii_art4 = figlet_format(msg, font="bubble")
    ascii_art5 = figlet_format(msg, font="letters")
    ascii_art6 = figlet_format(msg, font="doh")
    ascii_art7 = figlet_format(msg, font="standard")
    print(ascii_art1)
    print(ascii_art2)
    print(ascii_art3)
    print(ascii_art4)
    print(ascii_art5)
    print(ascii_art6)
    print(ascii_art7)


print_art("Python 3.8")
