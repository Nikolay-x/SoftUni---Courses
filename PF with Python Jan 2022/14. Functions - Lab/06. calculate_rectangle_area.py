# 6.Calculate Rectangle Area
# Create a function that calculates and returns the area of a rectangle by given width and height. Print the result on the console.
#
# Input
# 3
# 4
#
# Output
# 12

def rectangular_area(width, height):
    result = width * height
    return result

w = int(input())
h = int(input())

print(rectangular_area(w, h))
