#!/usr/bin/python3
import unittest
from models.base import Base

class TestBase(unittest.TestCase):

    def setUp(self):
        Base.__nb_objects = 0

    def test_equal(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)
        b4 = Base(12)
        self.assertEqual(b4.id, 12)
