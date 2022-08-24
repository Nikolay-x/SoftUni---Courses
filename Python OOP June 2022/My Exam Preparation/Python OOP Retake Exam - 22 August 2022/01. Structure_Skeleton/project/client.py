class Client:
    def __init__(self, phone_number: str):
        self.phone_number = phone_number
        self.shopping_cart = []
        self.bill = 0.0

    @property
    def phone_number(self):
        return self.__phone_number
    
    @phone_number.setter
    def phone_number(self, value):
        if value[0] == "0" and len(value) == 10 and self.chars_are_digits(value):
            self.__phone_number = value
        else:
            raise ValueError("Invalid phone number!")

    @staticmethod
    def chars_are_digits(number):
        phone_number_consists_of_digits = True
        for ch in number:
            if not ch.isdigit():
                phone_number_consists_of_digits = False
        return phone_number_consists_of_digits
