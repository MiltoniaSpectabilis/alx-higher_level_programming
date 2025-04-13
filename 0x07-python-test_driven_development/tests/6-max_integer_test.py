#!/usr/bin/python3
"""test cases for 6-max_integer"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """unittest class for max_integer"""

    def test_postive(self):
        """tests positive ints"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_one_int(self):
        """tests one int"""
        self.assertEqual(max_integer([10]), 10)

    def test_postive_middle(self):
        """tests positive ints"""
        self.assertEqual(max_integer([1, 2, 5, 3, 4]), 5)

    def test_mixed(self):
        """tests a mix of positive and negative ints"""
        self.assertEqual(max_integer([6, -2, 0, -3]), 6)

    def test_negative(self):
        """tests negative ints"""
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def test_empty(self):
        """tests empty list"""
        self.assertIsNone(max_integer())

    def test_non_integers(self):
        """tests a list with mixed types"""
        with self.assertRaises(TypeError):
            max_integer([1, 2, 'A', 3])

    # def test_string(self):
    #     """tests a string"""
    #     with self.assertRaises(TypeError):
    #         max_integer("string")


if __name__ == '__main__':
    unittest.main()
