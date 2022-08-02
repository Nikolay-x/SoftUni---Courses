from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    @abstractmethod
    def create_chair(self):
        raise NotImplementedError()

    @abstractmethod
    def create_sofa(self):
        raise NotImplementedError

    @abstractmethod
    def create_table(self):
        raise NotImplementedError


class Chair:
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return self._name


class Sofa:
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return self._name


class Table:
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return self._name


class VictorianFactory(AbstractFactory):
    def create_chair(self):
        return Chair('victorian Chair')

    def create_sofa(self):
        return Sofa('victorian sofa')

    def create_table(self):
        return Table('victorian table')


class ModernFactory(AbstractFactory):
    def create_chair(self):
        return Chair('modern chair')

    def create_sofa(self):
        return Sofa('modern sofa')

    def create_table(self):
        return Table('modern table')


class FuturisticFactory(AbstractFactory):
    def create_chair(self):
        return Chair('futuristic chair')

    def create_sofa(self):
        return Sofa('futuristic sofa')

    def create_table(self):
        return Table('futuristic table')


ff = FuturisticFactory()
print(ff)
print(ff.__class__.__name__)
print(ff.__class__.__dict__)
print(ff.__dict__)
print(ff.__class__.__repr__(ff))
print(ff.__repr__())
print(ff.__doc__)

print('-' * 18)

fc = ff.create_chair()
print(fc)
print(fc.__class__.__name__)
print(fc.__class__.__dict__)
print(fc.__dict__)
print(fc.__class__.__repr__(fc))
print(fc.__repr__())
print(ff.__doc__)
