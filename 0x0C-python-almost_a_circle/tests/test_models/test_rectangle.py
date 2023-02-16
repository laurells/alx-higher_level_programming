#!/usr/bin/python3
"""Module that Test_rectangle class"""
import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """Test_rectangle"""

    def test_equal(self):
        """test_equal for a each option to rectbagle"""
        b1 = Rectangle(10, 12)
        self.assertEqual((b1.width, b1.height, b1.id), (10, 12, 4))

    def test_x(self):
        """test_equal for a each option to rectbagle"""
        b2 = Rectangle(10, 12, 1)
        self.assertEqual((b2.x, b2.id), (1, 5))

    def test_correct_value(self):
        """test_equal for a each option to rectbagle"""
        b3 = Rectangle(10, 12, 1, 1)
        self.assertEqual((b3.width, b3.height, b3.x, b3.y), (10, 12, 1, 1))

    def test_id(self):
        """test_equal for a each option to rectbagle"""
        b4 = Rectangle(10, 12, 1, 1, 5)
        self.assertEqual((b4.x, b4.y, b4.id), (1, 1, 5))

class test_area(unittest.TestCase):
    """test_area public method"""

    def test_area_three_cases(self):
        """test_area_three_cases"""
        b5 = Rectangle(3, 2)
        self.assertEqual((b5.area()), (6))
        b6 = Rectangle(2, 10)
        self.assertEqual(b6.area(), 20)
        b7 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(b7.area(), 56)
