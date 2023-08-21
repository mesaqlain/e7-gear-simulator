from set_directory_function import set_directory
set_directory()

import unittest
import json
import random
# from tests.test_functions import * 
from src.validation_utils import *

class TestReforgeIncrease(unittest.TestCase):
    
    def test_valid_get_reforge_increase(self):
        """Test whether valid entries yield the expected results"""
        test_cases = [
            (0, None, None, 525), # stat_id = 0, stat_type = None, rolled = None, expected = 525
            (0, 'mainstat', None, 525),
            (0, 'mainstat', 0, 525),
            (0, None, 0, 525),
            (0, 'substat', None, 11),
            (5, 'substat', 3, 5),
            ('5', 'substat', 3, 5),
        ]
        for stat_id, stat_type, rolled, expected in test_cases:
            with self.subTest(stat_id=stat_id, stat_type=stat_type, rolled=rolled, expected=expected):
                reforge_increase = get_reforge_increase(stat_id, stat_type, rolled)
                self.assertEqual(reforge_increase, expected)

    def test_invalid_get_reforge_increase(self):
        """Test whether invalid entries raise ValueError"""
        test_cases = [
            (-1, None, None), # invalid stat_id
            (0, 'some string', 2), # invalid stat_type
            (3, 'mainstat', -1), # invalid rolled (negative)
            (4, 'substat', '1') # invalid rolled (str)
        ]
        for stat_id, stat_type, rolled in test_cases:
            with self.subTest(stat_id=stat_id, stat_type=stat_type, rolled=rolled):
                with self.assertRaises(ValueError):
                    reforge_increase = get_reforge_increase(stat_id, stat_type, rolled)

                
if __name__ == '__main__':
    unittest.main()
