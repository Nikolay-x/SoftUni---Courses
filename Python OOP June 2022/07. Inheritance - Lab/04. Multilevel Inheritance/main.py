# 4.Multilevel Inheritance
# In a folder called project create three files: vehicle.py and car.py, and sports_car.py.
# In each file, create its corresponding class - Vehicle, Car, and SportsCar:
# Vehicle with a single method move() that returns: "moving..."
# Car with a single method drive() that returns: "driving..."
# SportsCar with a single method race() that returns: "racing...".
# SportsCar should inherit from Car and Car should inherit from Vehicle.
# Submit in Judge a zip file of the folder project.

from project.sports_car import SportsCar

sport_car = SportsCar()

print(sport_car.move())
print(sport_car.drive())
print(sport_car.race())
