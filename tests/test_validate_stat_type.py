from set_directory_function import set_directory
set_directory()

import unittest
from src.validation_utils import validate_stat_type

class TestValidateStatType(unittest.TestCase):

    def test_valid_stat_types(self):
        """Test valid stat types when written in smaller case, upper case, or mixed case, mod = False default"""
        valid_stat_types = ['mainstat', 'substat', 'Mainstat', 'Substat', 'MAINstat', 'subSTAT']
        for stat_type in valid_stat_types:
            self.assertEqual(validate_stat_type(stat_type), stat_type.lower())

            
    def test_invalid_gear_type_str(self):
        """Test invalid stat types written as str, mod = False default"""
        invalid_stat_types = ['mainstats', 'SUBSTATS', 'subs', 'Main', 'stATs', 'stat']
        for stat_type in invalid_stat_types:
            with self.assertRaises(ValueError):
                validate_stat_type(stat_type)
                
                
    def test_invalid_stat_type_int(self):
        """Test invalid stat types when an int is entered, mod = False default"""
        with self.assertRaises(ValueError):
            validate_stat_type(111)

            
    def test_none_stat_type(self):
        """Test invalid stat types when None is entered, should default to 'mainstat', mod = False default"""
        self.assertEqual(validate_stat_type(None), 'mainstat')
        
        
    def test_valid_stat_types_mod_True(self):
        """Test valid stat types when written in smaller case, upper case, or mixed case, mod = True"""
        valid_stat_types = ['substat', 'Substat', 'subSTAT']
        for stat_type in valid_stat_types:
            self.assertEqual(validate_stat_type(stat_type, mod = True), stat_type.lower())
        
        
    def test_invalid_stat_types_mod_True(self):
        """Test valid stat types when written in smaller case, upper case, or mixed case, mod = True"""
        invalid_stat_types = ['mainstat', 'Mainstat', 'MAINstat']
        for stat_type in invalid_stat_types:
            with self.assertRaises(ValueError):
                validate_stat_type(stat_type, mod = True)
        

    def test_valid_stat_types_rolled_zero(self):
        """Test valid stat types when written in smaller case, upper case, or mixed case, mod = False default, rolled=0"""
        valid_stat_types = ['mainstat', 'substat', 'Mainstat', 'Substat', 'MAINstat', 'subSTAT']
        for stat_type in valid_stat_types:
            self.assertEqual(validate_stat_type(stat_type, rolled=0), stat_type.lower())
            
            
    def test_valid_stat_types_rolled_non_zero_subsstats(self):
        """Test valid stat types when written in smaller case, upper case, or mixed case, mod = False default, rolled=0"""
        valid_stat_types = ['substat', 'Substat', 'subSTAT']
        for stat_type in valid_stat_types:
            self.assertEqual(validate_stat_type(stat_type, rolled=2), stat_type.lower())
        
        
    def test_invalid_stat_types_rolled_non_zero(self):
        """Test invalid stat types when written in smaller case, upper case, or mixed case, rolled=3"""
        invalid_stat_types = ['mainstat', 'Mainstat', 'MAINstat']
        for stat_type in invalid_stat_types:
            with self.assertRaises(ValueError):
                validate_stat_type(stat_type, rolled=3)

        
if __name__ == '__main__':
    unittest.main()
