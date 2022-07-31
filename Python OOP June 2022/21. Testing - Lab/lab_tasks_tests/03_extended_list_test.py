# 3.List
# You are provided with a class IntegerList. It should only store integers. The initial integers should be set by the constructor. They are stored as a list. IntegerList has a functionality to add, remove_index, get, insert, get the biggest number, and get the index of an element. Your task is to test the class.
# Note: You are not allowed to change the structure of the provided code
# Constraints
# add operation, should add an element and returns the list.
# oIf the element is not an integer, a ValueError is thrown
# remove_index operation removes the element on that index and returns it.
# oIf the index is out of range, an IndexError is thrown
# __init__ should only take integers, and store them
# get should return the specific element
# oIf the index is out of range, an IndexError is thrown
# insert
# oIf the index is out of range, IndexError is thrown
# oIf the element is not an integer, ValueError is thrown
# get_biggest
# get_index
# Hint
# Do not forget to test the constructor

from lab_tasks.extended_list import IntegerList
import unittest


class ListTests(unittest.TestCase):

    def test_constructor(self):
        int_list = [1, 2, -3]
        ll = IntegerList(*int_list)
        self.assertTrue(hasattr(ll, f"_{ll.__class__.__name__}__data"))
        self.assertListEqual(getattr(ll, f"_{ll.__class__.__name__}__data", None), int_list)

    def test_only_int_stored(self):
        ll = IntegerList("1", -2, "b")
        expected = [-2]
        self.assertListEqual(expected, getattr(ll, f"_{ll.__class__.__name__}__data", None))

    def test_all_methods_exist(self):
        ll = IntegerList(1, -2, 3)
        self.assertTrue(hasattr(ll, "add") and callable(getattr(ll, "add", None)))
        self.assertTrue(hasattr(ll, "get_data") and callable(getattr(ll, "get_data", None)))
        self.assertTrue(hasattr(ll, "remove_index") and callable(getattr(ll, "remove_index", None)))
        self.assertTrue(hasattr(ll, "get") and callable(getattr(ll, "get", None)))
        self.assertTrue(hasattr(ll, "insert") and callable(getattr(ll, "insert", None)))
        self.assertTrue(hasattr(ll, "get_biggest") and callable(getattr(ll, "get_biggest", None)))
        self.assertTrue(hasattr(ll, "get_index") and callable(getattr(ll, "get_index", None)))

    def test_get_data_expect_correct_data(self):
        ll = IntegerList(1, 2, 3)
        self.assertEqual([1, 2, 3], ll.get_data())

    def test_add__expect_adding_el(self):
        int_list = IntegerList()
        internal_list = int_list.add(1)
        self.assertEqual([1], internal_list)

    def test_add_type__expect_to_raise_if_not_int(self):
        int_list = IntegerList()
        with self.assertRaises(Exception) as context:
            int_list.add("test")
        self.assertIsNotNone(context)
        self.assertEqual('Element is not Integer', str(context.exception))

    def test_remove_idx__expect_removing_idx_el(self):
        value_to_be_removed = 3
        int_list = IntegerList(1, 2, value_to_be_removed, 4)

        result = int_list.remove_index(2)
        self.assertEqual(value_to_be_removed, result)
        self.assertEqual([1, 2, 4], int_list.get_data())

    def test_remove__expect_to_raise(self):
        idx = 4
        int_list = IntegerList(1, 2, 3, 4)
        with self.assertRaises(Exception) as error:
            int_list.remove_index(idx)
        self.assertEqual("Index is out of range", str(error.exception))

    def test_get__idx_out_of_range__expect_to_raise(self):
        idx = 4
        int_list = IntegerList(1, 2, 3, 4)
        with self.assertRaises(Exception) as error:
            int_list.get(idx)
        self.assertEqual("Index is out of range", str(error.exception))

    def test_get__return_value__expect_correct_value(self):
        idx = 3
        int_list = IntegerList(1, 2, 3, 4)
        result = int_list.get(idx)
        self.assertEqual(4, result)

    def test_insert__idx_out_of_range__expect_to_raise(self):
        idx = 4
        el = 5
        int_list = IntegerList(1, 2, 3, 4)
        with self.assertRaises(Exception) as error:
            int_list.insert(idx, el)
        self.assertEqual("Index is out of range", str(error.exception))

    def test_insert__value_int_type__expect_to_raise(self):
        idx = 3
        el = '5'
        int_list = IntegerList(1, 2, 3, 4)
        with self.assertRaises(ValueError) as error:
            int_list.insert(idx, el)
        self.assertEqual("Element is not Integer", str(error.exception))

    def test_insert__valid_value___expect_correct_value(self):
        idx = 3
        el = 5
        int_list = IntegerList(1, 2, 3, 4)
        int_list.insert(idx, el)
        actual_result = getattr(int_list, f'_{int_list.__class__.__name__}__data')
        expected_result = [1, 2, 3, 5, 4]
        self.assertListEqual(expected_result, actual_result)

    def test_get_biggest__return__expect_correct_value(self):
        int_list = IntegerList(1, 2, 3, 4)
        actual_result = int_list.get_biggest()
        expected_result = 4
        self.assertEqual(expected_result, actual_result)

    def test_get_idx__return__expect_correct_value(self):
        el = 3
        int_list = IntegerList(1, 2, 3, 4)
        actual_result = int_list.get_index(el)
        expected_result = 2
        self.assertEqual(expected_result, actual_result)


if __name__ == "__main__":
    unittest.main()
