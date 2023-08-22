from set_directory_function import set_directory
set_directory()

import random
import json
import unittest
from src.validation_utils import validate_gear_set

SETS = json.loads(open('data/sets.json', 'r').read())

class TestValidateGearSet(unittest.TestCase):
    
    def test_validate_gear_set_1(self):
        """
        Test whether valid inputs in the lower case yield expected results.
        """
        valid_inputs = ['health', 'lifesteal', 'attack', 'destruction', 'speed']
        expected_outputs = ['health', 'lifesteal', 'attack', 'destruction', 'speed']
        for i, val in enumerate(valid_inputs):
            with self.subTest(input_ = val):
                self.assertEqual(validate_gear_set(val), expected_outputs[i])

    def test_validate_gear_set_2(self):
        """
        Test whether valid inputs in the Capital case yield expected results.
        """
        valid_inputs = ['Hit', 'Critical', 'Torrent', 'Immunity', 'Rage']
        expected_outputs = ['hit', 'critical', 'torrent', 'immunity', 'rage']
        for i, val in enumerate(valid_inputs):
            with self.subTest(input_ = val):
                self.assertEqual(validate_gear_set(val), expected_outputs[i])

    def test_validate_gear_set_3(self):
        """
        Test whether valid inputs in the UPPER case yield expected results.
        """
        valid_inputs = ['COUNTER', 'PROTECTION', 'REVENGE', 'PENETRATION', 'SPEED']
        expected_outputs = ['counter', 'protection', 'revenge', 'penetration', 'speed']
        for i, val in enumerate(valid_inputs):
            with self.subTest(input_ = val):
                self.assertEqual(validate_gear_set(val), expected_outputs[i])

    def test_validate_gear_set_4(self):
        """
        Test whether valid inputs in the miXEed case yield expected results.
        """
        valid_inputs = ['countER', 'proTEction', 'REVenge', 'PenETRAtioN', 'spEEd']
        expected_outputs = ['counter', 'protection', 'revenge', 'penetration', 'speed']
        for i, val in enumerate(valid_inputs):
            with self.subTest(input_ = val):
                self.assertEqual(validate_gear_set(val), expected_outputs[i])

    def test_validate_gear_set_invalid_inputs(self):
        """
        Test whether invalid inputs raise ValueErrors.
        """
        invalid_inputs = ['some str', 'excellent', 1, -1, 0]
        for val in invalid_inputs:
            with self.assertRaises(ValueError):
                validate_gear_set(val)
                
    def test_validate_gear_set_none(self):
        """
        Test whether a None input returns a correct random grade.
        """
        expected_outputs = list(SETS.keys())
        for i in range(1000):
            with self.subTest(val = i):
                self.assertIn(validate_gear_set(None), expected_outputs)
                
if __name__ == '__main__':
    unittest.main()

