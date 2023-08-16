from set_directory_function import set_directory
set_directory()

import unittest
import json
from src.validation_utils import validate_gear_type

TYPES = json.loads(open('data/types.json', 'r').read())

class TestValidateGearType(unittest.TestCase):

    def test_valid_gear_type_exact(self):
        """Test valid gear types when written exactly as in types.json file"""
        valid_gear_types = ['Weapon', 'Helm', 'Armor', 'Necklace', 'Ring', 'Boots']
        for gear_type in valid_gear_types:
            self.assertEqual(validate_gear_type(gear_type), gear_type.lower())

    def test_valid_gear_type_lower(self):
        """Test valid gear types when written in lower case"""
        valid_gear_types = ['weapon', 'helm', 'armor', 'necklace', 'ring', 'boots']
        for gear_type in valid_gear_types:
            self.assertEqual(validate_gear_type(gear_type), gear_type.lower())
            
    def test_valid_gear_type_mixed(self):
        """Test valid gear types when written in mixed case"""
        valid_gear_types = ['WeapoN', 'HELM', 'aRmOr', 'NECKlace', 'riNG', 'bOOtS']
        for gear_type in valid_gear_types:
            self.assertEqual(validate_gear_type(gear_type), gear_type.lower())

    def test_invalid_gear_type_str(self):
        """Test invalid gear types written as str"""
        invalid_gear_types = ['Sword', 'mask', 'MAIL', 'Jewelry', 'Accessory', 'Shoes']
        for gear_type in invalid_gear_types:
            with self.assertRaises(ValueError):
                validate_gear_type(gear_type)
                
    def test_invalid_gear_type_int(self):
        """Test invalid gear types when an int is entered"""
        with self.assertRaises(ValueError):
            validate_gear_type(-1)

    def test_none_gear_type(self):
        self.assertIsNone(validate_gear_type(None))

if __name__ == '__main__':
    unittest.main()
