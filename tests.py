import unittest

from functions import *

class Tests(unittest.TestCase):
    def test_to_measurable(self):
        self.assertEqual(to_measurable(3.14), 3.1)
        self.assertEqual(to_measurable(25.2), 25)