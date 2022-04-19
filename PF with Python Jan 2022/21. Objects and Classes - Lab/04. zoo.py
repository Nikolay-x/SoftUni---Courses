# 4.Zoo
# Create a class Zoo. It should have a class attribute called __animals that stores the total count of the animals in the zoo. The __init__ method should only receive the name of the zoo. There you should also create 3 empty lists (mammals, fishes, birds). The class should also have 2 more methods:
# add_animal(species, name) - based on the species, adds the name to the corresponding list
# get_info(species) - based on the species returns a string in the following format:
# "{Species} in {zoo_name}: {names}
# Total animals: {total_animals}"
# On the first line, you will receive the name of the zoo. On the second line, you will receive number n. On the following n lines you will receive animal info in the format: "{species} {name}". Add the animal to the zoo to the corresponding list. The species could be "mammal", "fish", or "bird".
# On the final line, you will receive a species.
# At the end, print the info for that species and the total count of animals in the zoo.
#
# Input
# Great
# Zoo
# 5
# mammal
# lion
# mammal
# bear
# fish
# salmon
# bird
# owl
# mammal
# tiger
# mammal
#
# Output
# Mammals in Great Zoo: lion, bear, tiger
# Total animals: 5

class Zoo:
    __animals = 0

    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
            self.__animals += 1
        elif species == "fish":
            self.fishes.append(name)
            self.__animals += 1
        elif species == "bird":
            self.birds.append(name)
            self.__animals += 1

    def get_info(self, species):
        result = ""
        if species == "mammal":
            result += f"Mammals in {self.zoo_name}: {', '.join(self.mammals)}\n"
        if species == "fish":
            result += f"Fishes in {self.zoo_name}: {', '.join(self.fishes)}\n"
        if species == "bird":
            result += f"Birds in {self.zoo_name}: {', '.join(self.birds)}\n"
        result += f"Total animals: {self.__animals}"
        return result


input_zoo_name = input()
zoo = Zoo(input_zoo_name)
n = int(input())
for i in range(n):
    line = input().split(" ")
    i_species = line[0]
    i_name = line[1]
    zoo.add_animal(i_species, i_name)
info = input()
print(zoo.get_info(info))
