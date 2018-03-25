# -*- coding: utf-8 -*-
import unittest
import toy_package


class TestToyPackage(unittest.TestCase):

    def test_average(self):
        people = [
            {'name': 'name1', 'age': 1, 'home': 'here', 'weight': 12},
            {'name': 'name2', 'age': 2, 'home': 'here', 'weight': 18},
        ]
        self.assertEqual(toy_package.average('weight', people), 15)
        self.assertEqual(toy_package.average('age', people), 1.5)
