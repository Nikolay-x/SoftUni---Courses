# Problem 3. Unit Tests
# You will be provided with another skeleton for this problem. Open the new skeleton as a new project and write tests for the Movie class. The class will have some methods, fields, and one constructor, all of them working properly. You are NOT ALLOWED to change any class. Cover the whole class with unit tests to make sure that the class is working as intended. Submit only the test folder.

import unittest

from project.movie import Movie


class MovieTests(unittest.TestCase):
    NAME = "Movie name"
    YEAR = 2001
    RATING = 8.5
    ACTORS = []
    MIN_YEAR = 1887

    def setUp(self) -> None:
        self.movie = Movie(self.NAME, self.YEAR, self.RATING)

    def test_init_correct_return(self):
        self.assertEqual(self.NAME, self.movie.name)
        self.assertEqual(self.YEAR, self.movie.year)
        self.assertEqual(self.RATING, self.movie.rating)
        self.assertEqual(self.ACTORS, self.movie.actors)

    def test_name_setter__empty_str__expect_to_raise(self):
        with self.assertRaises(Exception) as error:
            self.movie.name = ""
        self.assertEqual("Name cannot be an empty string!", str(error.exception))

    def test_name_getter_and_setter__valid_name__expect_correct_output(self):
        name = "Movie name 1"
        self.movie.name = name
        self.assertEqual(name, self.movie.name)

    def test_year_setter__lt_min_year__expect_to_raise(self):
        with self.assertRaises(Exception) as error:
            self.movie.year = self.MIN_YEAR-1
        self.assertEqual("Year is not valid!", str(error.exception))

    def test_year_getter_and_setter__valid_year__expect_correct_output(self):
        year = 2001
        self.movie.year = year
        self.assertEqual(year, self.movie.year)

    def test_add_actor__valid_input__expect_to_add_actor(self):
        input_actors = ["actor1", "actor2"]
        self.movie.actors = input_actors
        self.movie.add_actor("actor3")
        actual = self.movie.actors
        expected = ["actor1", "actor2", "actor3"]
        self.assertEqual(expected, actual)

    def test_add_actor__invalid_input__expect_correct_return(self):
        self.movie.add_actor("actor1")
        self.movie.add_actor("actor2")
        added_actor = "actor1"
        actual = self.movie.add_actor(added_actor)
        self.assertEqual(f"{added_actor} is already added in the list of actors!", actual)
        self.assertEqual(["actor1", "actor2"], self.movie.actors)

    def test_gt__self_gt_other_expect_correct_input(self):
        other_rating = self.RATING - 1
        other_name = "Other movie name"
        other_movie = Movie(other_name, self.YEAR, other_rating)
        actual = self.movie.__gt__(other_movie)
        self.assertEqual(f'"{self.movie.name}" is better than "{other_movie.name}"', actual)

    def test_gt__other_gt_self_expect_correct_input(self):
        other_rating = self.RATING + 1
        other_name = "Other movie name"
        other_movie = Movie(other_name, self.YEAR, other_rating)
        actual = self.movie.__gt__(other_movie)
        self.assertEqual(f'"{other_movie.name}" is better than "{self.movie.name}"', actual)

    def test_repr__expect_correct_output(self):
        input_actors = ["actor1", "actor2"]
        self.movie.actors = input_actors

        actual = repr(self.movie)
        expected = f"Name: {self.movie.name}\n" \
               f"Year of Release: {self.movie.year}\n" \
               f"Rating: {self.movie.rating:.2f}\n" \
               f"Cast: {', '.join(self.movie.actors)}"
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
