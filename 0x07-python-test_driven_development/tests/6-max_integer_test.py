#!/usr/bin/python3

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function"""

    def test_empty_list(self):
        """Test max_integer with an empty list"""
        self.assertIsNone(max_integer([]))

    def test_single_element_list(self):
        """Test max_integer with a single element list"""
        self.assertEqual(max_integer([5]), 5)

    def test_ordered_list(self):
        """Test max_integer with an ordered list"""
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_reversed_list(self):
        """Test max_integer with a reversed list"""
        self.assertEqual(max_integer([5, 4, 3, 2, 1]), 5)

    def test_unordered_list(self):
        """Test max_integer with an unordered list"""
        self.assertEqual(max_integer([4, 2, 5, 1, 3]), 5)

    def test_float_list(self):
        """Test max_integer with a list containing floats"""
        self.assertEqual(max_integer([3.4, 1.2, 5.6, 2.3]), 5.6)

    def test_string_list(self):
        """Test max_integer with a list containing strings"""
        with self.assertRaises(TypeError):
            max_integer(["1", "2", "3"])

    def test_mixed_list(self):
        """Test max_integer with a list containing mixed types"""
        with self.assertRaises(TypeError):
            max_integer([1, 2, "3", 4, 5])


if __name__ == '__main__':
    unittest.main()
