from set_directory_function import set_directory
set_directory()

import random
import json
import unittest
from src.utilities import validate_gear_grade

GRADES = json.loads(open('data/grades.json', 'r').read())

class TestValidateGearGrade(unittest.TestCase):
    
    def test_validate_gear_grade_valid_inputs_lower(self):
        """
        Test whether valid inputs in the lower case yield expected results.
        """
        valid_inputs = ['normal', 'good', 'rare', 'heroic', 'epic']
        expected_outputs = ['normal', 'good', 'rare', 'heroic', 'epic']
        for i, val in enumerate(valid_inputs):
            with self.subTest(input_ = val):
                self.assertEqual(validate_gear_grade(val), expected_outputs[i])

    def test_validate_gear_grade_valid_inputs_capital(self):
        """
        Test whether valid inputs in the capital case yield expected results.
        """
        valid_inputs = ['Normal', 'Good', 'Rare', 'Heroic', 'Epic']
        expected_outputs = ['normal', 'good', 'rare', 'heroic', 'epic']
        for i, val in enumerate(valid_inputs):
            with self.subTest(input_ = val):
                self.assertEqual(validate_gear_grade(val), expected_outputs[i])

    def test_validate_gear_grade_valid_inputs_upper(self):
        """
        Test whether valid inputs in the upper case yield expected results.
        """
        valid_inputs = ['NORMAL', 'GOOD', 'RARE', 'HEROIC', 'EPIC']
        expected_outputs = ['normal', 'good', 'rare', 'heroic', 'epic']
        for i, val in enumerate(valid_inputs):
            with self.subTest(input_ = val):
                self.assertEqual(validate_gear_grade(val), expected_outputs[i])

    def test_validate_gear_grade_valid_inputs_mixed(self):
        """
        Test whether valid inputs in the mixed case yield expected results.
        """
        valid_inputs = ['norMAL', 'gOOd', 'RarE', 'heROIc', 'epIC']
        expected_outputs = ['normal', 'good', 'rare', 'heroic', 'epic']
        for i, val in enumerate(valid_inputs):
            with self.subTest(input_ = val):
                self.assertEqual(validate_gear_grade(val), expected_outputs[i])

    def test_validate_gear_grade_invalid_inputs_mixed(self):
        """
        Test whether invalid inputs raise ValueErrors.
        """
        invalid_inputs = ['some str', 'excellent', 1, -1, 0]
        for val in invalid_inputs:
            with self.assertRaises(ValueError):
                validate_gear_grade(val)
                
    def test_validate_gear_grade_none_input(self):
        """
        Test whether a None input returns a correct random grade.
        """
        expected_outputs = ['normal', 'good', 'rare', 'heroic', 'epic']
        for i in range(1000):
            with self.subTest(val = i):
                self.assertIn(validate_gear_grade(None), expected_outputs)
                
if __name__ == '__main__':
    unittest.main()
