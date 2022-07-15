# 3.Playing
# Create a function called start_playing which will receive an instance and will return its play() method.
# Submit only the start_playing function in the judge system
#
# Test Code
# class Guitar:
#     def play(self):
#         return "Playing the guitar"
#
# guitar = Guitar()
# print(start_playing(guitar))
#
# Output
# Playing the guitar

def start_playing(instance):
    return instance.play()


class Guitar:
    @staticmethod
    def play():
        return "Playing the guitar"


guitar = Guitar()
print(start_playing(guitar))


class Children:
    def play(self):
        return "Children are playing"


children = Children()
print(start_playing(children))
