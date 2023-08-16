from set_directory_function import set_directory
set_directory()

import unittest
import json
from src.validation_utils import validate_stat_id

STATS = json.loads(open('data/stats.json', 'r').read())

class TestValidateStatID(unittest.TestCase):

    def test_valid_stat_id_str(self):
        """Test valid stat_id when written as str exactly as in 'id' key in stats.json file"""
        valid_stat_ids = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        for stat_id in valid_stat_ids:
            self.assertEqual(validate_stat_id(stat_id), str(stat_id))

    def test_valid_stat_id_int(self):
        """Test valid stat_id when written as int """
        valid_stat_ids = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        for stat_id in valid_stat_ids:
            self.assertEqual(validate_stat_id(stat_id), str(stat_id))
            
    def test_invalid_stat_id_int(self):
        """Test invalid stat_id written as int"""
        invalid_stat_ids = -1
        with self.assertRaises(ValueError):
            validate_stat_id(invalid_stat_ids)
                
    def test_invalid_stat_id_str(self):
        """Test invalid stat_id written as int"""
        invalid_stat_ids = 'Health'
        with self.assertRaises(ValueError):
            validate_stat_id(invalid_stat_ids)
                
    def test_invalid_stat_id_int_not_in_range(self):
        """Test invalid stat_id written as int but not in acceptable range"""
        invalid_stat_ids = 100
        with self.assertRaises(ValueError):
            validate_stat_id(invalid_stat_ids)
            
    def test_invalid_stat_id_str_not_in_range(self):
        """Test invalid stat_id written as str but not in acceptable range"""
        invalid_stat_ids = '50'
        with self.assertRaises(ValueError):
            validate_stat_id(invalid_stat_ids)

    def test_none_gear_type(self):
        with self.assertRaises(ValueError):
            validate_stat_id(None)

if __name__ == '__main__':
    unittest.main()
