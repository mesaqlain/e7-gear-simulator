from set_directory_function import set_directory
set_directory()

import unittest
import json
from src.utilities import convert_int_to_str, check_valid_pool

with open('data/types.json', 'r') as types_file:
    TYPES = json.load(types_file)

class TestCheckValidPool(unittest.TestCase):
    
    def test_check_valid_pool_invalid_1(self):
        """
        If no args provided, we should have ValueError, must provide gear_type
        """
        with self.assertRaises(ValueError):
            check_valid_pool()
            
            
    def test_check_valid_pool_invalid_2(self):
        """
        If gear_type_is provided, we should have ValueError if id is not allowed in pool
        """
        with self.assertRaises(ValueError):
            check_valid_pool(gear_type='weapon', stat_ids=1)
        
        
    def test_check_valid_pool_invalid_3(self):
        """
        If gear_type_is provided, we should have ValueError if mainstat id doesn't match gear_type
        """
        gear_types_list = ['weapon', 'helm', 'armor', 'necklace', 'ring', 'boots']
        stat_types_list = ['mainstat', 'substat', 'substat', 'mainstat', 'mainstat', 'mainstat']
        stat_ids_list = [4, 2, [0, 10], [10], '7', ['8']]
        for i,val in enumerate(gear_types_list):
            with self.subTest(g_type = val):
                with self.assertRaises(ValueError):
                    check_valid_pool(gear_type=val, stat_type=stat_types_list[i], stat_ids=stat_ids_list[i])

        
        
        
    def assertNotRaises(self, exc_type, func, *args, **kwargs):
        try:
            func(*args, **kwargs)
        except exc_type as e:
            self.fail(f"Function raised {exc_type} unexpectedly: {e}")


    def test_check_valid_pool_no_error(self):
        valid_gear_type = ['weapon', 'helm', 'armor']
        valid_stat_ids = [
            [0, '0', [0], ['0']],
            [2, '2', [2], ['2']],
            [4, '4', [4], ['4']]
        ]
        valid_stat_type = 'mainstat'
        for i, g_type in enumerate(valid_gear_type):
            input_gear_type = g_type
            valid_stats = valid_stat_ids[i]
            for j in valid_stats:
                self.assertNotRaises(ValueError, check_valid_pool, gear_type=input_gear_type, stat_ids=j, stat_type=valid_stat_type)
                
                
    def test_check_valid_pool_no_error_subs(self):
        valid_gear_type = ['weapon', 'helm', 'armor', 'ring', 'necklace', 'boots']
        valid_stat_ids = [
            [1, '1', [1], ['1']],
            [3, '3', [3], ['3']],
            [5, '5', [5], ['5']],
            [[10, 3], [5, '4'], [3, 2, 1, 0], ['1', '2', '3']],
            [[10, 3], [5, '4'], [3, 2, 1, 0], ['1', '2', '3']],
            [[10, 3], [5, '4'], [3, 2, 1, 0], ['1', '2', '3']],
        ]
        valid_stat_type = 'substat'
        for i, g_type in enumerate(valid_gear_type):
            input_gear_type = g_type
            valid_stats = valid_stat_ids[i]
            for j in valid_stats:
                self.assertNotRaises(ValueError, check_valid_pool, gear_type=input_gear_type, stat_ids=j, stat_type=valid_stat_type)
            

if __name__ == '__main__':
    unittest.main()