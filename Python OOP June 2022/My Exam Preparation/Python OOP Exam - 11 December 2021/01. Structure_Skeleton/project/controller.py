from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if car_type == "MuscleCar":
            input_car = MuscleCar(model, speed_limit)
        elif car_type == "SportsCar":
            input_car = SportsCar(model, speed_limit)
        else:
            return

        for car in self.cars:
            if car.model == model:
                raise Exception(f"Car {model} is already created!")

        self.cars.append(input_car)
        return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        for d in self.drivers:
            if d.name == driver_name:
                raise Exception(f"Driver {driver_name} is already created!")

        driver = Driver(driver_name)
        self.drivers.append(driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        for r in self.races:
            if r.name == race_name:
                raise Exception(f"Race {race_name} is already created!")

        race = Race(race_name)
        self.races.append(race)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver = self.find_driver_by_name(driver_name)
        if driver is None:
            raise Exception(f"Driver {driver_name} could not be found!")

        if car_type != "MuscleCar" and car_type != "SportsCar":
            return

        car = self.find_last_car_by_type(car_type)
        if car is None:
            raise Exception(f"Car {car_type} could not be found!")

        if driver.car is not None:
            old_car = driver.car
            old_model = old_car.model
            driver.car = car
            car.is_taken = True
            old_car.is_taken = False
            return f"Driver {driver_name} changed his car from {old_model} to {car.model}."
        else:
            driver.car = car
            car.is_taken = True
            return f"Driver {driver_name} chose the car {car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        race = self.find_race_by_name(race_name)
        if race is None:
            raise Exception(f"Race {race_name} could not be found!")

        driver = self.find_driver_by_name(driver_name)
        if driver is None:
            raise Exception(f"Driver {driver_name} could not be found!")

        if driver in race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."

        if driver.car is None:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        race = self.find_race_by_name(race_name)
        if race is None:
            raise Exception(f"Race {race_name} could not be found!")

        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        # result = ''
        # race_results = sorted(race.drivers, key=lambda item: -item.car.speed_limit)[:3]
        # for driver in race_results:
        #     driver.add_win()
        #     result += f"Driver {driver.name} " \
        #               f"wins the {race_name} race " \
        #               f"with a speed of {driver.car.speed_limit}.\n"
        # return result.strip()

        fastest_3_drivers_and_cars = self.find_fastest_3_drivers(race)
        result = ""
        for i in range(3):
            result += f"Driver {fastest_3_drivers_and_cars[i][0]} wins the {race_name} " \
                      f"race with a speed of {fastest_3_drivers_and_cars[i][1]}.\n"
            driver = self.find_driver_by_name(fastest_3_drivers_and_cars[i][0])
            driver.number_of_wins += 1
        return result.strip()

    def find_driver_by_name(self, driver_name):
        for d in self.drivers:
            if d.name == driver_name:
                return d
        return None

    def find_last_car_by_type(self, car_type):
        for car in self.cars[::-1]:
            if car.car_type == car_type and not car.is_taken:
                return car
        return None

    def find_race_by_name(self, race_name):
        for r in self.races:
            if r.name == race_name:
                return r
        return None

    @staticmethod
    def find_fastest_3_drivers(race):
        drivers_dict = {}
        for d in race.drivers:
            if d not in drivers_dict:
                drivers_dict[d.name] = d.car.speed_limit
        sorted_drivers = sorted(drivers_dict.items(), key=lambda x: -x[1])
        fastest_3_drivers = sorted_drivers[0], sorted_drivers[1], sorted_drivers[2]
        return fastest_3_drivers
