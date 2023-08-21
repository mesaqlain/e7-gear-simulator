from set_directory_function import set_directory
set_directory()

import unittest
from src.validation_utils import validate_mod

class TestValidateMod(unittest.TestCase):
    
    def test_valid_mod_True(self):
        """Test valid mods when mod = True"""
        valid_mods = [True]
        for mod in valid_mods:
            self.assertTrue(validate_mod(mod), f"{mod} should return True.")
            
            
    def test_valid_mod_True_2(self):
        """Test valid mods when mod = True and stat_type='substat'"""
        valid_mods = [True]
        for mod in valid_mods:
            self.assertTrue(validate_mod(mod, stat_type='substat'), f"{mod} should return True.")

            
    def test_valid_mod_True_3(self):
        """Test valid mods when mod = True and stat_type='substat'"""
        valid_mods = [True]
        for mod in valid_mods:
            self.assertTrue(validate_mod(mod, stat_type=None), f"{mod} should return True.")

            
    def test_valid_mod_False(self):
        """Test valid mods when mod = False"""
        valid_mods = [False]
        for mod in valid_mods:
            self.assertFalse(validate_mod(mod), f"{mod} should return False.")

            
    def test_valid_mod_False_2(self):
        """Test valid mods when mod = False and stat_type='substat'"""
        valid_mods = [False]
        for mod in valid_mods:
            self.assertFalse(validate_mod(mod, stat_type='substat'), f"{mod} should return False.")

            
    def test_valid_mod_False_3(self):
        """Test valid mods when mod = False and stat_type='mainstat'"""
        valid_mods = [False]
        for mod in valid_mods:
            self.assertFalse(validate_mod(mod, stat_type='mainstat'), f"{mod} should return False.")
            
            
    def test_valid_mod_False_4(self):
        """Test valid mods when mod = False and stat_type='None'"""
        valid_mods = [False]
        for mod in valid_mods:
            self.assertFalse(validate_mod(mod, stat_type=None), f"{mod} should return False.")
            
            
    def test_ivalid_mods(self):
        """
        Test invalid mods.
        Case 1: None
        Case 2: str
        Case 3: list
        Case 4: negative
        Case 5: large int
        Case 6: 0
        Case 7: 1
        """
        invalid_mods = [None, 'True', [True], -1, 100, 0, 1]
        for mod in invalid_mods:
            with self.assertRaises(ValueError):
                validate_mod(mod)
                
            
    def test_ivalid_mods_2(self):
        """
        Incorrect stat_type
        """
        with self.assertRaises(ValueError):
            validate_mod(True, 'mainstat')
            
        
            
if __name__ == '__main__':
    unittest.main()
