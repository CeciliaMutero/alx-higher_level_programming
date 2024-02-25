#!/usr/bin/python3
"""Unnitest for max integer in a list
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_positive_integers(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([4]), 4)

    def test_negative_integers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-4, -2, -3, -1]), -1)

    def test_mixed_integers(self):
        self.assertEqual(max_integer([-1, 2, 0, -4]), 2)
        self.assertEqual(max_integer([0, -2, 3, -4]), 3)
        self.assertEqual(max_integer([-1, -2, -3, 4]), 4)

    def test_floats(self):
        self.assertEqual(max_integer([1.1, 2.2, 3.3, 4.4]), 4.4)
        self.assertEqual(max_integer([1.1, 3.3, 4.4, 2.2]), 4.4)
        self.assertEqual(max_integer([4.4]), 4.4)

    def test_strings(self):
        self.assertEqual(max_integer(['a', 'b', 'c']), 'c')
        self.assertEqual(max_integer(['abc', 'def', 'ghi']), 'ghi')
        self.assertEqual(max_integer(['apple', 'banana', 'orange']), 'orange')
