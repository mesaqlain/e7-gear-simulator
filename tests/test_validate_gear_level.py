from set_directory_function import set_directory
set_directory()

import unittest
from src.utilities import validate_gear_level

class TestValidateGearLevel(unittest.TestCase):
    
    def test_validate_gear_level_valid_inputs(self):
        """
        Tests whether we get the expected int output when we enter a valid gear level
        """
        valid_gear_levels = [58, 59, 69, 71, 85, 88, 90, 99, 100]
        
        for i in valid_gear_levels:
            with self.subTest(gear_level=i):
                self.assertEqual(validate_gear_level(i), i)
                
    def test_validate_gear_level_invalid_inputs(self):
        """
        Tests whether we get ValueError when we enter an invalid gear level
        Invalid ints: 56, 57, 101, 102, 0
        Negative int: -1
        Strings: '70', 'seventy'
        Other objects: list, dict
        """
        invalid_gear_levels = [56, 57, 101, 102, 0, -1, '70', 'eighty', [], {}]
        
        for i in invalid_gear_levels:
            with self.assertRaises(ValueError):
                validate_gear_level(i)
                
    def test_validate_gear_level_none(self):
        """
        Tests whether we get 85 when we gear_level is None
        """
        self.assertEqual(validate_gear_level(None), 85)
                
                
if __name__ == '__main__':
    unittest.main()
