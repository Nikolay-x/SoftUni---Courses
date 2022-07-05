# 1.Food
# In a folder called project create two files: food.py and fruit.py:
# In the food.py file, create a class called Food which will receive an expiration_date (str) upon initialization.
# In the fruit.py file, create a class called Fruit with will receive a name (str) and an expiration_date (str) upon initialization.
# Fruit should inherit from Food.
# Submit in Judge a zip file of the folder project.

from project.food import Food
from project.fruit import Fruit

fruit = Fruit("apple", "09/07/2022")
food = Food("10/07/2022")

print(fruit.name)
print(fruit.expiration_date)
print(food.expiration_date)
