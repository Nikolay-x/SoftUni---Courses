# In this exercise everyone should use the source code (skeleton) written for each of the four problems (01. Mammal, 02. Vehicle, 03. Hero and 04. Student) from the Testing exercise. You have the structure and functionality of the classes, and now you should test them. You are NOT ALLOWED to change the class. Cover the whole class with unit tests to make sure that the class is working as intended.
# Submit only the test folder.

from project.mammal import Mammal
import unittest


class MammalTests(unittest.TestCase):
    NAME = "Name"
    TYPE = "Mammal type"
    SOUND = "Sound"

    def setUp(self) -> None:
        self.mammal = Mammal(self.NAME, self.TYPE, self.SOUND)

    def test_init__expect_correct_input(self):
        self.assertEqual(self.NAME, self.mammal.name)
        self.assertEqual(self.TYPE, self.mammal.type)
        self.assertEqual(self.SOUND, self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_sound__expect_correct_sound(self):
        actual_result = self.mammal.make_sound()
        expected_result = f"{self.NAME} makes {self.SOUND}"
        self.assertEqual(expected_result, actual_result)

    def test_get_kingdom__expected_correct_values(self):
        actual_result = self.mammal.get_kingdom()
        expected_result = "animals"
        self.assertEqual(expected_result, actual_result)

    def test_info__expect_correct_return(self):
        actual_result = self.mammal.info()
        expected_result = f"{self.NAME} is of type {self.TYPE}"
        self.assertEqual(expected_result, actual_result)


if __name__ == "__main__":
    unittest.main()
