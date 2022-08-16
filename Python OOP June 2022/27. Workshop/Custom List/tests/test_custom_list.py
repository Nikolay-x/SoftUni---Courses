import unittest
from project.custom_list import CustomList


class CustomListTests(unittest.TestCase):
    DATA = []

    def setUp(self) -> None:
        self.custom_list = CustomList()
        self.custom_list.data = self.DATA

    def test_append__value_in_empty_list__expect_single_value(self):
        value = 4
        actual = self.custom_list.append(value)
        expected = [4]
        self.assertEqual(expected, actual)

    def test_append__value_in_list_with_elements__expect_values(self):
        input_data = [1, 2, 3]
        self.custom_list.data = input_data
        value = 4
        actual = self.custom_list.append(value)
        expected = [1, 2, 3, 4]
        self.assertEqual(expected, actual)

    def test_remove__idx_not_int__expect_raise(self):
        input_data = [1, 2, 3]
        self.custom_list.data = input_data
        index = "2"
        with self.assertRaises(TypeError) as error:
            self.custom_list.remove(index)
        self.assertIsNotNone(error)
        expected_msg = "Index must be integer."
        expected_list = [1, 2, 3]
        actual_list = self.custom_list.data
        self.assertEqual(expected_msg, str(error.exception))
        self.assertEqual(expected_list, actual_list)

    def test_remove__idx_out_of_range__expect_raise(self):
        input_data = [1, 2, 3]
        self.custom_list.data = input_data
        index = 3
        with self.assertRaises(IndexError) as error:
            self.custom_list.remove(index)
        self.assertIsNotNone(error)
        expected_msg = "Index out of range."
        expected_list = [1, 2, 3]
        actual_list = self.custom_list.data
        self.assertEqual(expected_msg, str(error.exception))
        self.assertEqual(expected_list, actual_list)

    def test_remove__idx_in_range__expect_to_remove(self):
        input_data = [1, 2, 3]
        self.custom_list.data = input_data
        index = 1

        expected_value = 2
        actual_value = self.custom_list.remove(index)
        expected_list = [1, 3]
        actual_list = self.custom_list.data

        self.assertEqual(expected_value, actual_value)
        self.assertEqual(expected_list, actual_list)

    def test_remove__idx_in_range_last_value__expect_to_remove(self):
        input_data = [3]
        self.custom_list.data = input_data
        index = 0

        expected_value = 3
        actual_value = self.custom_list.remove(index)
        expected_list = []
        actual_list = self.custom_list.data

        self.assertEqual(expected_value, actual_value)
        self.assertEqual(expected_list, actual_list)

    def test_get__idx_not_int__expect_raise(self):
        input_data = [1, 2, 3]
        self.custom_list.data = input_data
        index = "2"
        with self.assertRaises(TypeError) as error:
            self.custom_list.get(index)
        self.assertIsNotNone(error)
        expected_msg = "Index must be integer."
        expected_list = [1, 2, 3]
        actual_list = self.custom_list.data
        self.assertEqual(expected_msg, str(error.exception))
        self.assertEqual(expected_list, actual_list)

    def test_get__idx_out_of_range__expect_raise(self):
        input_data = [1, 2, 3]
        self.custom_list.data = input_data
        index = 3
        with self.assertRaises(IndexError) as error:
            self.custom_list.get(index)
        self.assertIsNotNone(error)
        expected_msg = "Index out of range."
        expected_list = [1, 2, 3]
        actual_list = self.custom_list.data
        self.assertEqual(expected_msg, str(error.exception))
        self.assertEqual(expected_list, actual_list)

    def test_get__idx_in_range_last_value__expect_to_get(self):
        input_data = [3]
        self.custom_list.data = input_data
        index = 0

        expected_value = 3
        actual_value = self.custom_list.get(index)
        expected_list = [3]
        actual_list = self.custom_list.data

        self.assertEqual(expected_value, actual_value)
        self.assertEqual(expected_list, actual_list)

    def test_get__idx_in_range_values__expect_to_get(self):
        input_data = [1, 2, 3]
        self.custom_list.data = input_data
        index = 1

        expected_value = 2
        actual_value = self.custom_list.get(index)
        expected_list = [1, 2, 3]
        actual_list = self.custom_list.data

        self.assertEqual(expected_value, actual_value)
        self.assertEqual(expected_list, actual_list)

    def test_get__idx_negative_in_range_values__expect_to_get(self):
        input_data = [1, 2, 3]
        self.custom_list.data = input_data
        index = -2

        expected_value = 2
        actual_value = self.custom_list.get(index)
        expected_list = [1, 2, 3]
        actual_list = self.custom_list.data

        self.assertEqual(expected_value, actual_value)
        self.assertEqual(expected_list, actual_list)

    def test_extend__obj_not_iter__expect_raise(self):
        input_data = [1, 2, 3]
        self.custom_list.data = input_data
        iterable = True
        with self.assertRaises(TypeError) as error:
            self.custom_list.extend(iterable)
        self.assertIsNotNone(error)
        expected_msg = "Object must be iterable."
        expected_list = [1, 2, 3]
        actual_list = self.custom_list.data
        self.assertEqual(expected_msg, str(error.exception))
        self.assertEqual(expected_list, actual_list)

    def test_extend__obj_is_iter__expect_to_extend(self):
        input_data = [1, 2, 3]
        self.custom_list.data = input_data
        iterable = (4, 5), 6, 7

        expected_list = [1, 2, 3, (4, 5), 6, 7]
        actual_list = self.custom_list.extend(iterable)

        self.assertEqual(expected_list, actual_list)

    def test_extend__obj_is_iter_empty_list__expect_to_extend(self):
        input_data = []
        self.custom_list.data = input_data
        iterable = "abc"

        expected_list = ['a', 'b', 'c']
        actual_list = self.custom_list.extend(iterable)

        self.assertEqual(expected_list, actual_list)

    def test_extend__obj_is_iter_and__is_empty_list__expect_to_extend(self):
        input_data = [1, 2, 3]
        self.custom_list.data = input_data
        iterable = []

        expected_list = [1, 2, 3]
        actual_list = self.custom_list.extend(iterable)

        self.assertEqual(expected_list, actual_list)

    def test_extend__obj_is_iter_two_empty_lists__expect_to_extend(self):
        input_data = []
        self.custom_list.data = input_data
        iterable = []

        expected_list = []
        actual_list = self.custom_list.extend(iterable)

        self.assertEqual(expected_list, actual_list)

    def test_insert__idx_not_int__expect_raise(self):
        input_data = [1, 2, 3]
        self.custom_list.data = input_data
        index = "2"
        value = 4
        with self.assertRaises(TypeError) as error:
            self.custom_list.insert(index, value)
        self.assertIsNotNone(error)
        expected_msg = "Index must be integer."
        expected_list = [1, 2, 3]
        actual_list = self.custom_list.data
        self.assertEqual(expected_msg, str(error.exception))
        self.assertEqual(expected_list, actual_list)

    def test_insert__valid_idx_value_is_empty__expect_to_insert(self):
        input_data = [1, 2, 3]
        self.custom_list.data = input_data
        index = 1
        value = ""

        expected_list = [1, '', 2, 3]
        actual_list = self.custom_list.insert(index, value)

        self.assertEqual(expected_list, actual_list)

    def test_insert__valid_idx_value__expect_to_insert(self):
        input_data = [1, 2, 3]
        self.custom_list.data = input_data
        index = 0
        value = 4

        expected_list = [4, 1, 2, 3]
        actual_list = self.custom_list.insert(index, value)

        self.assertEqual(expected_list, actual_list)

    def test_insert__valid_negative_idx_value__expect_to_insert(self):
        input_data = [1, 2, 3]
        self.custom_list.data = input_data
        index = -1
        value = 4

        expected_list = [1, 2, 4, 3]
        actual_list = self.custom_list.insert(index, value)

        self.assertEqual(expected_list, actual_list)

    def test_insert__valid_idx_above_size_value__expect_to_insert(self):
        input_data = [1, 2, 3]
        self.custom_list.data = input_data
        index = 9
        value = 4

        expected_list = [1, 2, 3, 4]
        actual_list = self.custom_list.insert(index, value)

        self.assertEqual(expected_list, actual_list)

    def test_insert__valid_idx_below_size_value__expect_to_insert(self):
        input_data = [1, 2, 3]
        self.custom_list.data = input_data
        index = -9
        value = 4

        expected_list = [4, 1, 2, 3]
        actual_list = self.custom_list.insert(index, value)

        self.assertEqual(expected_list, actual_list)

    def test_insert__valid_idx_empty_list__expect_to_insert(self):
        input_data = []
        self.custom_list.data = input_data
        index = 0
        value = 3

        expected_list = [3]
        actual_list = self.custom_list.insert(index, value)

        self.assertEqual(expected_list, actual_list)

    def test_pop__list_with_out_values__expect_to_raise(self):
        input_data = []
        self.custom_list.data = input_data

        with self.assertRaises(IndexError) as error:
            self.custom_list.pop()
        self.assertIsNotNone(error)

        expected_list = []
        actual_list = self.custom_list.data

        self.assertEqual("pop from empty list", str(error.exception))
        self.assertEqual(expected_list, actual_list)

    def test_pop__list_with_values__expect_to_pop(self):
        input_data = [1, 2, 3]
        self.custom_list.data = input_data

        expected_value = 3
        actual_value = self.custom_list.pop()
        expected_list = [1, 2]
        actual_list = self.custom_list.data

        self.assertEqual(expected_value, actual_value)
        self.assertEqual(expected_list, actual_list)

    def test_pop__list_with__one_value__expect_to_pop(self):
        input_data = [3]
        self.custom_list.data = input_data

        expected_value = 3
        actual_value = self.custom_list.pop()
        expected_list = []
        actual_list = self.custom_list.data

        self.assertEqual(expected_value, actual_value)
        self.assertEqual(expected_list, actual_list)

    def test_clear__list_with_values__expect_to_empty_list(self):
        input_data = [1, 2, 3]
        self.custom_list.data = input_data

        self.custom_list.clear()
        expected_list = []
        actual_list = self.custom_list.data

        self.assertEqual(expected_list, actual_list)

    def test_clear__list_with_out_values__expect_to_empty_list(self):
        input_data = []
        self.custom_list.data = input_data

        self.custom_list.clear()
        expected_list = []
        actual_list = self.custom_list.data

        self.assertEqual(expected_list, actual_list)

    def test_index__list_with_values__expect_to_return_index(self):
        input_data = [1, 2, 3]
        self.custom_list.data = input_data

        value = 3
        expected_index = 2
        actual_index = self.custom_list.index(value)
        expected_list = [1, 2, 3]
        actual_list = self.custom_list.data

        self.assertEqual(expected_index, actual_index)
        self.assertEqual(expected_list, actual_list)

    def test_index__list_with_out_values__expect_to_return_index(self):
        input_data = []
        self.custom_list.data = input_data

        value = 3
        with self.assertRaises(ValueError) as error:
            self.custom_list.index(value)

        self.assertIsNotNone(error)
        expected_list = []
        actual_list = self.custom_list.data

        self.assertEqual("3 is not in list", str(error.exception))
        self.assertEqual(expected_list, actual_list)

    def test_count__list_with_values_value_in_list__expect_to_return_count(self):
        input_data = [1, 2, 3, 3, 3, 3]
        self.custom_list.data = input_data

        value = 3
        expected_count = 4
        actual_count = self.custom_list.count(value)
        expected_list = [1, 2, 3, 3, 3, 3]
        actual_list = self.custom_list.data

        self.assertEqual(expected_count, actual_count)
        self.assertEqual(expected_list, actual_list)

    def test_count__list_with_values_value_once_in_list__expect_to_return_count(self):
        input_data = [1, 2, 3, 3, 3, 3]
        self.custom_list.data = input_data

        value = 2
        expected_count = 1
        actual_count = self.custom_list.count(value)
        expected_list = [1, 2, 3, 3, 3, 3]
        actual_list = self.custom_list.data

        self.assertEqual(expected_count, actual_count)
        self.assertEqual(expected_list, actual_list)

    def test_count__list_with_values_value_not_in_list__expect_to_return_count(self):
        input_data = [1, 2, 3, 3, 3, 3]
        self.custom_list.data = input_data

        value = 4
        expected_count = 0
        actual_count = self.custom_list.count(value)
        expected_list = [1, 2, 3, 3, 3, 3]
        actual_list = self.custom_list.data

        self.assertEqual(expected_count, actual_count)
        self.assertEqual(expected_list, actual_list)

    def test_count__empty_list__expect_to_return_count(self):
        input_data = []
        self.custom_list.data = input_data

        value = 0
        expected_count = 0
        actual_count = self.custom_list.count(value)
        expected_list = []
        actual_list = self.custom_list.data

        self.assertEqual(expected_count, actual_count)
        self.assertEqual(expected_list, actual_list)

    def test_reverse__list_with_values__expect_to_return_reversed_list(self):
        input_data = [1, 2, 3]
        self.custom_list.data = input_data

        expected_list = [3, 2, 1]
        actual_list = self.custom_list.reverse()

        self.assertEqual(expected_list, actual_list)

    def test_reverse__empty_list__expect_to_return_empty_list(self):
        input_data = []
        self.custom_list.data = input_data

        expected_list = []
        actual_list = self.custom_list.reverse()

        self.assertEqual(expected_list, actual_list)

    def test_copy__list_with_values__expect_to_return_copy_list_different_object(self):
        input_data = [1, 2, 3]
        self.custom_list.data = input_data

        actual_list_object = self.custom_list
        copy_list_object = self.custom_list.copy()

        self.assertEqual(list(copy_list_object), list(actual_list_object.data))
        self.assertNotEqual(copy_list_object, actual_list_object)

    def test_copy__empty_list__expect_to_return_empty_list(self):
        input_data = []
        self.custom_list.data = input_data

        actual_list_object = self.custom_list
        copy_list_object = self.custom_list.copy()

        self.assertEqual(list(copy_list_object), list(actual_list_object.data))
        self.assertNotEqual(copy_list_object, actual_list_object)

    def test_size__list_with_values__expect_to_return_len(self):
        input_data = [1, 2, 3, 3, 3, 3]
        self.custom_list.data = input_data

        expected_size = 6
        actual_size = self.custom_list.size()
        expected_list = [1, 2, 3, 3, 3, 3]
        actual_list = self.custom_list.data

        self.assertEqual(expected_size, actual_size)
        self.assertEqual(expected_list, actual_list)

    def test_size__empty_list__expect_to_return_len(self):
        input_data = []
        self.custom_list.data = input_data

        expected_size = 0
        actual_size = self.custom_list.size()
        expected_list = []
        actual_list = self.custom_list.data

        self.assertEqual(expected_size, actual_size)
        self.assertEqual(expected_list, actual_list)

    def test_len__list_with_values__expect_to_return_len(self):
        input_data = [1, 2, 3, 3, 3, 3]
        self.custom_list.data = input_data

        expected_size = 6
        actual_size = len(self.custom_list.data)
        expected_list = [1, 2, 3, 3, 3, 3]
        actual_list = self.custom_list.data

        self.assertEqual(expected_size, actual_size)
        self.assertEqual(expected_list, actual_list)

    def test_len__empty_list__expect_to_return_len(self):
        input_data = []
        self.custom_list.data = input_data

        expected_size = 0
        actual_size = len(self.custom_list.data)
        expected_list = []
        actual_list = self.custom_list.data

        self.assertEqual(expected_size, actual_size)
        self.assertEqual(expected_list, actual_list)

    def test_add_first__value__expect_to_add(self):
        input_data = [1, 2, 3]
        self.custom_list.data = input_data
        index = 0
        value = 4

        expected_list = [4, 1, 2, 3]
        actual_list = self.custom_list.insert(index, value)

        self.assertEqual(expected_list, actual_list)

    def test_add_first__empty_list_and_value__expect_to_add(self):
        input_data = []
        self.custom_list.data = input_data
        index = 0
        value = ""

        expected_list = ['']
        actual_list = self.custom_list.insert(index, value)

        self.assertEqual(expected_list, actual_list)

    def test_dictionize__list_with_unhashable_values__expect_error_message(self):
        input_data = [1, 2, 3, 4, "a", "b", {1: 2}]
        self.custom_list.data = input_data

        expected = "One or more elements are not hashable."
        actual = self.custom_list.dictionize()

        self.assertEqual(expected, actual)
        self.assertEqual([1, 2, 3, 4, 'a', 'b', {1: 2}], self.custom_list.data)

    def test_dictionize__list_with_even_number_of_values__expect_dict(self):
        input_data = [1, 2, 3, 4, "a", "b"]
        self.custom_list.data = input_data

        expected_dict = {1: 2, 3: 4, 'a': 'b'}
        actual_dict = self.custom_list.dictionize()

        self.assertEqual(expected_dict, actual_dict)

    def test_dictionize__list_with_odd_number_of_values__expect_dict(self):
        input_data = [1, 2, 3, 4, "a", "b", 5]
        self.custom_list.data = input_data

        expected_dict = {1: 2, 3: 4, 'a': 'b', 5: " "}
        actual_dict = self.custom_list.dictionize()

        self.assertEqual(expected_dict, actual_dict)

    def test_dictionize__empty_list__expect_empty_dict(self):
        input_data = []
        self.custom_list.data = input_data

        expected_dict = {}
        actual_dict = self.custom_list.dictionize()

        self.assertEqual(expected_dict, actual_dict)

    def test_move__amount_not_int__expect_to_raise(self):
        input_data = [1, 2, 3, 4, 5, 6]
        self.custom_list.data = input_data
        amount = "3"

        with self.assertRaises(TypeError) as error:
            self.custom_list.move(amount)

        self.assertIsNotNone(error)
        expected_list = [1, 2, 3, 4, 5, 6]
        actual_list = self.custom_list.data
        self.assertEqual("Amount must be int.", str(error.exception))
        self.assertEqual(expected_list, actual_list)

    def test_move__amount_out_of_range__expect_to_raise(self):
        input_data = [1, 2, 3]
        self.custom_list.data = input_data
        amount = 4

        with self.assertRaises(ValueError) as error:
            self.custom_list.move(amount)

        self.assertIsNotNone(error)
        expected_list = [1, 2, 3]
        actual_list = self.custom_list.data
        self.assertEqual("There are not 4 number of elements", str(error.exception))
        self.assertEqual(expected_list, actual_list)

    def test_move__valid_amount__expect_to_move(self):
        input_data = [1, 2, 3, 4, 5, 6]
        self.custom_list.data = input_data
        amount = 2

        expected_list = [3, 4, 5, 6, 1, 2]
        actual_list = self.custom_list.move(amount)

        self.assertEqual(expected_list, actual_list)

    def test_move__valid_amount_zero__expect_to_move(self):
        input_data = [1, 2, 3]
        self.custom_list.data = input_data
        amount = 0

        expected_list = [1, 2, 3]
        actual_list = self.custom_list.move(amount)

        self.assertEqual(expected_list, actual_list)

    def test_move__valid_amount_list_len__expect_to_move(self):
        input_data = [1, 2, 3]
        self.custom_list.data = input_data
        amount = 3

        expected_list = [1, 2, 3]
        actual_list = self.custom_list.move(amount)

        self.assertEqual(expected_list, actual_list)

    def test_sum__list_with_values__expect_sum(self):
        input_data = [1, 2, 3, 4.5, "abc", (2, 3)]
        self.custom_list.data = input_data

        expected_sum = 15.5
        actual_sum = self.custom_list.sum()

        self.assertEqual(expected_sum, actual_sum)

    def test_sum__empty_list__expect_sum(self):
        input_data = []
        self.custom_list.data = input_data

        expected_sum = 0
        actual_sum = self.custom_list.sum()

        self.assertEqual(expected_sum, actual_sum)

    def test_sum__list_with_zeros__expect_sum(self):
        input_data = [0, 0, 0, 0, 0, 0]
        self.custom_list.data = input_data

        expected_sum = 0
        actual_sum = self.custom_list.sum()

        self.assertEqual(expected_sum, actual_sum)

    def test_overbound__list_with_values_without_len__expect_to_raise(self):
        input_data = [4, 4.5, True, {1: "a"}, (2, 3)]
        self.custom_list.data = input_data

        with self.assertRaises(ValueError) as error:
            self.custom_list.overbound()

        self.assertIsNotNone(error)
        self.assertEqual("One or more invalid values.", str(error.exception))
        self.assertEqual([4, 4.5, True, {1: "a"}, (2, 3)], self.custom_list.data)

    def test_overbound__list_with_values__expect_to_return_correct_index(self):
        input_data = [4, 4.5, "abcde", {1: "a", "b": 2, 3: "c", 4: "d", 5: "e", 6: "f"}, (2, 3)]
        self.custom_list.data = input_data

        expected_index = 3
        actual_index = self.custom_list.overbound()

        self.assertEqual(expected_index, actual_index)

    def test_overbound__empty_list_return_correct_index(self):
        input_data = []
        self.custom_list.data = input_data

        expected_index = None
        actual_index = self.custom_list.overbound()

        self.assertEqual(expected_index, actual_index)

    def test_overbound__one_el_list_return_correct_index(self):
        input_data = [(2, 3, 4)]
        self.custom_list.data = input_data

        expected_index = 0
        actual_index = self.custom_list.overbound()

        self.assertEqual(expected_index, actual_index)

    def test_underbound__list_with_values_without_len__expect_to_raise(self):
        input_data = [4, 4.5, True, {1: "a"}, (2, 3)]
        self.custom_list.data = input_data

        with self.assertRaises(ValueError) as error:
            self.custom_list.underbound()

        self.assertIsNotNone(error)
        self.assertEqual("One or more invalid values.", str(error.exception))
        self.assertEqual([4, 4.5, True, {1: "a"}, (2, 3)], self.custom_list.data)

    def test_underbound__list_with_values__expect_to_return_correct_index(self):
        input_data = [4, 4.5, "abcde", {1: "a"}, (2, 3)]
        self.custom_list.data = input_data

        expected_index = 3
        actual_index = self.custom_list.underbound()

        self.assertEqual(expected_index, actual_index)

    def test_underbound__empty_list_return_correct_index(self):
        input_data = []
        self.custom_list.data = input_data

        expected_index = None
        actual_index = self.custom_list.underbound()

        self.assertEqual(expected_index, actual_index)

    def test_underbound__one_el_list_return_correct_index(self):
        input_data = [(2, 3, 4)]
        self.custom_list.data = input_data

        expected_index = 0
        actual_index = self.custom_list.underbound()

        self.assertEqual(expected_index, actual_index)


if __name__ == "__main__":
    unittest.main()
