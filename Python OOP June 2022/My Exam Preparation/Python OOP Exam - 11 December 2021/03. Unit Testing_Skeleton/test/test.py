from project.team import Team
import unittest


class TeamTests(unittest.TestCase):
    NAME = "Name"
    MEMBERS = {}

    def setUp(self) -> None:
        self.team = Team(self.NAME)

    def test_init__expect_correct_input(self):
        error_message = "Team Name can contain only letters!"
        wrong_name = "Team name"
        with self.assertRaises(ValueError) as error:
            self.team = Team(wrong_name)
        self.assertEqual(error_message, str(error.exception))

        name = "TeamA"
        self.team.name = name
        self.assertEqual(name, self.team.name)
        self.assertDictEqual({}, self.team.members)
        self.assertTrue(hasattr(self.team, "_Team__name"))
        self.assertEqual(name, self.team._Team__name)

    def test_name_getter_and_setter__valid_input(self):
        value = "Newname"
        self.team.name = value
        self.assertEqual(value, self.team.name)

    def test_name_getter_and_setter__invalid_input__expect_to_raise(self):
        value = "New name"
        with self.assertRaises(ValueError) as error:
            self.team.name = value
        self.assertEqual("Team Name can contain only letters!", str(error.exception))
        self.assertEqual(self.NAME, self.team.name)

    def test_add_member__valid_input__expect_correct_output(self):
        name_age_dict = {"a": 1, "b": 2, "c": "text"}
        expected = "Successfully added: a, b, c"
        actual = self.team.add_member(**name_age_dict)
        self.assertEqual(name_age_dict, self.team.members)
        self.assertEqual(expected, actual)

        add_members = {"c": 4, "d": 5}
        actual_result = self.team.add_member(**add_members)
        self.assertEqual("Successfully added: d", actual_result)
        self.assertEqual({"a": 1, "b": 2, "c": "text", "d": 5}, self.team.members)

    def test_remove_member__valid__input__expect_correct_output(self):
        name_age_dict = {"a": 1, "b": 2, "c": 3}
        self.team.members = name_age_dict
        member_name = "a"
        expected = f"Member {member_name} removed"
        actual = self.team.remove_member(member_name)
        self.assertEqual(expected, actual)
        self.assertEqual({"b": 2, "c": 3}, self.team.members)

    def test_remove_member__invalid__input__expect_to_raise(self):
        name_age_dict = {"a": 1, "b": 2, "c": 3}
        self.team.members = name_age_dict
        member_name = "d"
        expected = f"Member with name {member_name} does not exist"
        actual = self.team.remove_member(member_name)
        self.assertEqual(expected, actual)
        self.assertEqual({"a": 1, "b": 2, "c": 3}, self.team.members)

    def test_gt__self_gt__other__expect_correct_output(self):
        name_age_dict = {"a": 1, "b": 2, "c": 3}
        other_name_age_dict = {"a": 1, "b": 2}
        other_team = Team("Othername")
        self.team.members = name_age_dict
        other_team.members = other_name_age_dict
        expected = True
        actual = self.team > other_team
        self.assertEqual(expected, actual)

    def test_gt__other_gt__self__expect_correct_output(self):
        name_age_dict = {"a": 1, "b": 2}
        other_name_age_dict = {"a": 1, "b": 2, "c": 3}
        other_team = Team("Othername")
        self.team.members = name_age_dict
        other_team.members = other_name_age_dict
        expected = False
        actual = self.team > other_team
        self.assertEqual(expected, actual)

    def test_len(self):
        name_age_dict = {"a": 1, "b": 2, "c": 3}
        self.team.members = name_age_dict
        expected = len(name_age_dict)
        actual = len(self.team)
        self.assertEqual(expected, actual)

    def test_add__self_other__expect_correct_output(self):
        name_age_dict = {"a": 1, "b": 2, "c": 3}
        other_name_age_dict = {"d": 4, "e": 5}
        other_team = Team("Othername")
        self.team.members = name_age_dict
        other_team.members = other_name_age_dict
        actual_new_team = self.team.__add__(other_team)
        actual_new_team_name = actual_new_team.name
        actual_new_team_members = actual_new_team.members
        expected = f"Team name: NameOthername" \
                   f"\nMember: e - 5-years old" \
                   f"\nMember: d - 4-years old" \
                   f"\nMember: c - 3-years old" \
                   f"\nMember: b - 2-years old" \
                   f"\nMember: a - 1-years old"

        self.assertEqual("NameOthername", actual_new_team_name)
        self.assertEqual({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}, actual_new_team_members)
        self.assertEqual(expected, str(actual_new_team))

    def test_str(self):
        name_age_dict = {"a": 1, "b": 2, "c": 3}
        self.team.members = name_age_dict
        actual = self.team.__str__()
        expected = f"Team name: Name\n" \
                   f"Member: c - 3-years old\n" \
                   f"Member: b - 2-years old\n" \
                   f"Member: a - 1-years old"
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
