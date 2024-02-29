#!/usr/bin/python3
"""
unnitest for Base class
"""


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_increment_id(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_specific_id(self):
        b3 = Base(10)
        self.assertEqual(b3.id, 10)


if __name__ == '__main__':
    unittest.main()
