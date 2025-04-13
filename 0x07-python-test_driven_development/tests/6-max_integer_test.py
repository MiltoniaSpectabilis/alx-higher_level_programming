#!/usr/bin/python3
"""test cases for 6-max_integer"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_postive(self):
        """tests positive ints"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_mixed(self):
        """tests a mix of positive and negative ints"""
        self.assertEqual(max_integer([6, -2, 0, -3]), 6)

    def test_negative(self):
        """tests negative ints"""
        self.assertEqual(max_integer([-1, -2, -3]), 0)

    def test_empty(self):
        """tests empty list"""
        self.assertEqual(max_integer([]), None)

    def test_string(self):
        """tests a string"""
        with self.assertRaises(TypeError):
            max_integer("string")

    def test_non_integers(self):
        """tests a list with mixed types"""
        with self.assertRaises(TypeError):
            max_integer([1, 2, 'A', 3])
