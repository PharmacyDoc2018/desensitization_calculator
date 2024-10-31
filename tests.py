import unittest

from functions import *

class Tests(unittest.TestCase):
    def test_to_measurable(self):
        self.assertEqual(to_measurable(3.14), 3.1)
        self.assertEqual(to_measurable(25.2), 25)
        self.assertEqual(to_measurable(4.2), 4.2)
        self.assertEqual(to_measurable(0.108), 0.1)
    
    def test_is_increment(self):
        self.assertEqual(is_increment(4.2), True)
        self.assertEqual(is_increment(4.1), True)
        self.assertEqual(is_increment(3.14), False)
        self.assertEqual(is_increment(3.1), True)

    def test_next_lower_measureable(self):
        self.assertEqual(next_lower_measurable(3.1), 3)
        self.assertEqual(next_lower_measurable(4.2), 4.1)
        self.assertEqual(next_lower_measurable(10.5), 10)
        self.assertEqual(next_lower_measurable(23.5), 23)
    
    def test_true_mod(self):
        self.assertEqual(true_mod(3.0, 0.05), 0)

    def test_next_higher_measurable(self):
        self.assertEqual(next_higher_measurable(3.1), 3.2)
        self.assertEqual(next_higher_measurable(4.2), 4.3)
        self.assertEqual(next_higher_measurable(10.5), 11)
        self.assertEqual(next_higher_measurable(3), 3.1)
        self.assertEqual(next_higher_measurable(10), 10.5)

    def test_generate_desensitization(self):
        bag_list = generate_desensitization(Cyclophosphamide, 1080)
        for bag in bag_list:
            print(f"{bag.drug} {bag.dose} mg in {bag.diluent} {bag.volume} mL")

    def test_true_floor_division(self):
        self.assertEqual(true_floor_division(106, 10), 10)