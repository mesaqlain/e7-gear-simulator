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
        
        
    def test_valid_gear_type_stat_id(self):
        """Test valid gear types when stat_id is provided"""
        valid_gear_types = ['WeapoN', 'HELM', 'aRmOr', 'NECKlace', 'riNG', 'bOOtS']
        for gear_type in valid_gear_types:
            self.assertEqual(validate_gear_type(gear_type, stat_id=1), gear_type.lower())
            
    def test_valid_gear_type_stat_id_2(self):
        """Test valid gear types when stat_type is mainstat"""
        valid_gear_types = ['WeapoN', 'HELM', 'aRmOr', 'NECKlace', 'riNG', 'bOOtS']
        for gear_type in valid_gear_types:
            self.assertEqual(validate_gear_type(gear_type, stat_type='mainstat'), gear_type.lower())

    def test_valid_gear_type_stat_id_3(self):
        """Test valid gear types when stat_type is substat"""
        valid_gear_types = ['WeapoN', 'HELM', 'aRmOr', 'NECKlace', 'riNG', 'bOOtS']
        for gear_type in valid_gear_types:
            self.assertEqual(validate_gear_type(gear_type, stat_type='substat'), gear_type.lower())
            
            
    def test_invalid_gear_type_stat_id(self):
        """Check if there is an error when the stat_id is not in the pool of allowed ids"""
        valid_gear_types = ['weapon', 'armor', 'helm', 'necklace', 'ring', 'boots']
        stat_types = ['mainstat', 'substat', 'substat', 'mainstat', 'mainstat', 'mainstat']
        stat_ids = [3, 0, 2, 8, 10, 6]
        for i in range(len(valid_gear_types)):
            
            gear_type = valid_gear_types[i]
            stat_id = stat_ids[i]
            stat_type = stat_types[i]
            
            with self.assertRaises(ValueError, msg=f"The stat {stat_id} cannot be added to gear type {gear_type} as {stat_type}."):
                validate_gear_type(gear_type, stat_id, stat_type)
            
            
if __name__ == '__main__':
    unittest.main()
