# 3.Ducks
# Refactor the provided code so it is in line with the Liskov Substitution Principle.
# Liskov Substitution Principle
#
# from abc import abstractmethod, ABC
#
#
# class Duck(ABC):
#     @staticmethod
#     def quack():
#         pass
#
#     @staticmethod
#     def walk():
#         pass
#
#     @staticmethod
#     def fly():
#         pass
#
#
# class RubberDuck(Duck):
#     @staticmethod
#     def quack():
#         return "Squeek"
#
#     @staticmethod
#     def walk():
#         """Rubber duck can walk only if you move it"""
#         raise Exception('I cannot walk by myself')
#
#     @staticmethod
#     def fly():
#         """Rubber duck can fly only if you throw it"""
#         raise Exception('I cannot fly by myself')
#
#
# class RobotDuck(Duck):
#     HEIGHT = 50
#
#     def __init__(self):
#         self.height = 0
#
#     @staticmethod
#     def quack():
#         return 'Robotic quacking'
#
#     @staticmethod
#     def walk():
#         return 'Robotic walking'
#
#     def fly(self):
#         """can only fly to specific height but
#         when it reaches it starts landing automatically"""
#         if self.height == RobotDuck.HEIGHT:
#             self.land()
#         else:
#             self.height += 1
#
#     def land(self):
#         self.height = 0


from abc import abstractmethod, ABC


class Duck(ABC):
    @staticmethod
    @abstractmethod
    def quack():
        pass

    @staticmethod
    @abstractmethod
    def walk():
        pass

    @staticmethod
    @abstractmethod
    def fly():
        pass


class RubberDuck(Duck):
    @staticmethod
    def quack():
        return "Squeek"

    @staticmethod
    def walk():
        """Rubber duck can walk only if you move it"""
        # raise Exception('I cannot walk by myself')
        return 'I cannot walk by myself'

    @staticmethod
    def fly():
        """Rubber duck can fly only if you throw it"""
        # raise Exception('I cannot fly by myself')
        return 'I cannot fly by myself'


class RobotDuck(Duck):
    HEIGHT = 3

    def __init__(self):
        self.height = 0

    @staticmethod
    def quack():
        return 'Robotic quacking'

    @staticmethod
    def walk():
        return 'Robotic walking'

    def fly(self):
        """can only fly to specific height but
        when it reaches it starts landing automatically"""
        if self.height == RobotDuck.HEIGHT:
            self.land()
        else:
            self.height += 1

    def land(self):
        self.height = 0


rubber_duck = RubberDuck
robot_duck = RobotDuck()

print(rubber_duck.quack())
print(rubber_duck.walk())
print(rubber_duck.fly())

print()

print(robot_duck.quack())
print(robot_duck.walk())
robot_duck.fly()
robot_duck.fly()
robot_duck.fly()
# robot_duck.fly()
print(robot_duck.height)
