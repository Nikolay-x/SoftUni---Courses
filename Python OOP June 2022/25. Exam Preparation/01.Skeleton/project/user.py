class User:
    def __init__(self, username, age):
        self.username = username
        self.age = age
        self.movies_liked = []
        self.movies_owned = []

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if not isinstance(value, str) or value == "":
            raise ValueError("Invalid username!")
        self.__username = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if not isinstance(value, int) or value < 6:
            raise ValueError("Users under the age of 6 are not allowed!")
        self.__age = value

    def __str__(self):
        liked_movies = "No movies liked."
        if self.movies_liked:
            liked_movies = "\n".join([m.details() for m in self.movies_liked])

        owned_movies = "No movies owned."
        if self.movies_owned:
            owned_movies = "\n".join([m.details() for m in self.movies_owned])

        result = f"Username: {self.username}, Age: {self.age}\n"
        result += "Liked movies:\n"
        result += f"{liked_movies}\n"
        result += f"Owned movies:\n"
        result += f"{owned_movies}"

        return result
