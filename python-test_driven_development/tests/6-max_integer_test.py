"""Unittest for max_integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_ordered_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([10, 2, 3, 4]), 10)

    def test_one_element(self):
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-10, -5, 0, 5, 10]), 10)

    def test_all_equal(self):
        self.assertEqual(max_integer([2, 2, 2, 2]), 2)

    def test_float_numbers(self):
        self.assertEqual(max_integer([1.5, 2.3, 0.7]), 2.3)

    def test_string_list(self):
        self.assertEqual(max_integer(["a", "b", "c"]), "c")

    def test_empty_string(self):
        self.assertIsNone(max_integer([]))


if __name__ == "__main__":
    unittest.main()