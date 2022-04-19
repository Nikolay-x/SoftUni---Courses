# Problem 3 - Need for Speed III
# Problem for exam preparation for the Programming Fundamentals Course @SoftUni.
# Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2307#2.
#
# You have just bought the latest and greatest computer game – Need for Seed III. Pick your favorite cars and drive them all you want! We know that you can't wait to start playing.
# On the first line of the standard input, you will receive an integer n – the number of cars that you can obtain. On the next n lines, the cars themselves will follow with their mileage and fuel available, separated by "|" in the following format:
# "{car}|{mileage}|{fuel}"
# Then, you will be receiving different commands, each on a new line, separated by " : ", until the "Stop" command is given:
# "Drive : {car} : {distance} : {fuel}":
# oYou need to drive the given distance, and you will need the given fuel to do that. If the car doesn't have enough fuel, print: "Not enough fuel to make that ride"
# oIf the car has the required fuel available in the tank, increase its mileage with the given distance, decrease its fuel with the given fuel, and print:
# "{car} driven for {distance} kilometers. {fuel} liters of fuel consumed."
# oYou like driving new cars only, so if a car's mileage reaches 100 000 km, remove it from the collection(s) and print: "Time to sell the {car}!"
# "Refuel : {car} : {fuel}":
# oRefill the tank of your car.
# oEach tank can hold a maximum of 75 liters of fuel, so if the given amount of fuel is more than you can fit in the tank, take only what is required to fill it up.
# oPrint a message in the following format: "{car} refueled with {fuel} liters"
# "Revert : {car} : {kilometers}":
# oDecrease the mileage of the given car with the given kilometers and print the kilometers you have decreased it with in the following format:
# "{car} mileage decreased by {amount reverted} kilometers"
# oIf the mileage becomes less than 10 000km after it is decreased, just set it to 10 000km and
# DO NOT print anything.
# Upon receiving the "Stop" command, you need to print all cars in your possession in the following format:
# "{car} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt."
# Input/Constraints
# The mileage and fuel of the cars will be valid, 32-bit integers, and will never be negative.
# The fuel and distance amounts in the commands will never be negative.
# The car names in the commands will always be valid cars in your possession.
# Output
# All the output messages with the appropriate formats are described in the problem description.
#
# Input
# 3
# Audi A6 | 38000 | 62
# Mercedes CLS | 11000 | 35
# Volkswagen Passat CC | 45678 | 5
# Drive: Audi A6: 543: 47
# Drive: Mercedes CLS: 94: 11
# Drive: Volkswagen Passat CC: 69: 8
# Refuel: Audi A6: 50
# Revert: Mercedes CLS: 500
# Revert: Audi A6: 30000
# Stop
#
# Output
# Audi A6 driven for 543 kilometers. 47 liters of fuel consumed.
# Mercedes CLS driven for 94 kilometers. 11 liters of fuel consumed.
# Not enough fuel to make that ride
# Audi A6 refueled with 50 liters
# Mercedes CLS mileage decreased by 500 kilometers
# Audi A6 -> Mileage: 10000 kms, Fuel in the tank: 65 lt.
# Mercedes CLS -> Mileage: 10594 kms, Fuel in the tank: 24 lt.
# Volkswagen Passat CC -> Mileage: 45678 kms, Fuel in the tank: 5 lt.

cars_count = int(input())
cars_dict = dict()
ml = "Mileage"
fl = "Fuel"

for i in range(cars_count):
    current_car = input().split("|")
    car = current_car[0]
    mileage = int(current_car[1])
    fuel = int(current_car[2])
    cars_dict[car] = {ml: mileage}
    cars_dict[car].update({fl: fuel})

while True:
    command = input().split(" : ")
    if command[0] == "Stop":
        break
    car = command[1]
    if command[0] == "Drive":
        distance = int(command[2])
        fuel = int(command[3])
        if cars_dict[car][fl] < fuel:
            print("Not enough fuel to make that ride")
        else:
            cars_dict[car][ml] += distance
            cars_dict[car][fl] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        if cars_dict[car][ml] >= 100000:
            del cars_dict[car]
            print(f"Time to sell the {car}!")
    if command[0] == "Refuel":
        fuel = int(command[2])
        cars_dict[car][fl] += fuel
        if cars_dict[car][fl] > 75:
            fuel -= cars_dict[car][fl] - 75
            cars_dict[car][fl] = 75
        print(f"{car} refueled with {fuel} liters")
    if command[0] == "Revert":
        kilometers = int(command[2])
        cars_dict[car][ml] -= kilometers
        if cars_dict[car][ml] <= 10000:
            cars_dict[car][ml] = 10000
        else:
            print(f"{car} mileage decreased by {kilometers} kilometers")

for car in cars_dict:
    print(f"{car} -> Mileage: {cars_dict[car][ml]} kms, Fuel in the tank: {cars_dict[car][fl]} lt.")
