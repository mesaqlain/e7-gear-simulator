from set_directory_function import set_directory
set_directory()

import unittest
from src.validation_utils import validate_mod_type

class TestValidateMod(unittest.TestCase):
    
    def test_valid_mod_type_greater(self):
        """Test valid mod types when 'greater' is written in different cases"""
        valid_mod_types = ['greater', 'Greater', 'grEATer']
        for mod_type in valid_mod_types:
            self.assertEqual(validate_mod_type(mod_type), 'greater', f"{mod_type} should return 'greater'.")

    def test_valid_mod_type_lesser(self):
        """Test valid mod types when 'lesser' is written in different cases"""
        valid_mod_types = ['lesser', 'Lesser', 'LeSSeR']
        for mod_type in valid_mod_types:
            self.assertEqual(validate_mod_type(mod_type), 'lesser', f"{mod_type} should return 'lesser'.")
            
    def test_valid_mod_type_none(self):
        """Test valid mod types when it is None"""
        self.assertEqual(validate_mod_type(None), 'greater', f"{None} should return 'greater'.")
            
    def test_ivalid_mod_types(self):
        """
        Test invalid mod types.
        Case 1: str
        Case 2: list
        Case 3: negative
        Case 4: large int
        """
        invalid_mod_types = ['big mod', ['small mod'], -1, 100]
        for mod_type in invalid_mod_types:
            with self.subTest(mod_type=mod_type):
                with self.assertRaises(ValueError):
                    validate_mod_type(mod_type)
                
            
if __name__ == '__main__':
    unittest.main()
