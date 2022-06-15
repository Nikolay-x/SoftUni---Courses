# 3.Triangle
# Create a module for printing a triangle. You will receive an integer number which is the size of the triangle.
#
# Input
# 3
#
# Output
# 1
# 1 2
# 1 2 3
# 1 2
# 1

# from triangle_module import print_triangle  # 1
from triangle_module.print_triangle import get_triangle  # 2

number = int(input())

# print_triangle.get_triangle(number)  # 1

get_triangle(number)  # 2
