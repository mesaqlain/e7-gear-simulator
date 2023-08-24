from set_directory_function import set_directory
set_directory()

import random
import json
import unittest
from tests.test_functions import test_get_mainstat_id

with open('data/types.json', 'r') as types_file:
    TYPES = json.load(types_file)

class TestGetMainstatID(unittest.TestCase):
    
    def test_all_none(self):
        """If no args are provided, we should get ValueError"""
        with self.assertRaises(ValueError):
            test_get_mainstat_id()
            
            
    def test_none_2(self):
        """If no gear_type provided, we should get Value Error, even if substat_id is provided."""
        with self.assertRaises(ValueError):
            test_get_mainstat_id(substat_ids = 1)
            
            
    def test_none_3(self):
        """If no gear_type provided, we should get Value Error, even if mainstat_id is provided."""
        with self.assertRaises(ValueError):
            test_get_mainstat_id(mainstat_id = 1)
            
            
    def test_none_4(self):
        """If no gear_type provided, we should get Value Error, even if mainstat_id and substat_ids are provided."""
        with self.assertRaises(ValueError):
            test_get_mainstat_id(mainstat_id = 1, substat_ids = [3, 4])
            
            
    def test_invalid_gear_type(self):
        """If invalid gear_type provided we'll get an error."""
        with self.assertRaises(ValueError):
            test_get_mainstat_id('shirt')
            
            
    def test_invalid_gear_type_main(self):
        """If invalid mainstats given gear_type are provided we'll get an error."""
        valid_inputs = ['weapon', 'helm', 'armor', 'necklace', 'ring', 'boots']
        invalid_mains = [2, 10, 10, 8, 6, 7]
        for i, val in enumerate(valid_inputs):
            with self.assertRaises(ValueError):
                test_get_mainstat_id(val, invalid_mains[i])
                
                
    def test_invalid_gear_type_subs(self):
        """If invalid substats given gear_type are provided we'll get an error."""
        valid_inputs = ['weapon', 'helm', 'armor']
        invalid_subs = [4, 2, 0]
        for i, val in enumerate(valid_inputs):
            with self.assertRaises(ValueError):
                test_get_mainstat_id(val, invalid_subs[i])
                
                
    def test_invalid_gear_type_duplicate_subs(self):
        """If invalid mainstats given gear_type are provided we'll get an error."""
        valid_inputs = ['weapon', 'helm', 'armor']
        invalid_subs = [
            [4, 4],
            [0, 0, 10, 9],
            [7, 7, 10, 10]
        ]
        for i, val in enumerate(valid_inputs):
            with self.assertRaises(ValueError):
                test_get_mainstat_id(val, invalid_subs[i])
                
                
    def test_too_many_subs(self):
        """If too many subs are provided, we'll get an error."""
        with self.assertRaises(ValueError):
            test_get_mainstat_id(substat_ids = [1, 2, 3, 4, 5])
                
            
    def test_no_subs_no_main(self):
        """
        If we specify a gear type, and no subs or mains are provided, we'll get a mainstat appropriately from the pool of
        allowed mainstats given the gear type:
        """
        valid_inputs = ['weapon', 'helm', 'armor', 'necklace', 'ring', 'boots']
        expected_mainstat_ids = [
            ['0'],
            ['2'],
            ['4'],
            ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
            ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
            ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        ]
        for i, val in enumerate(valid_inputs):
            with self.subTest(gear_type=val):
                for j in range(1000):
                    picked_mainstat_id = test_get_mainstat_id(gear_type=val)
                    expected_mainstats = expected_mainstat_ids[i]
                    self.assertIn(picked_mainstat_id, expected_mainstats)
                    
                    
    def test_no_subs_main_provided(self):
        """
        If we specify a gear type along with correct mainstats and no subs provided, 
        we'll get the mainstat back.
        """
        valid_inputs = ['weapon', 'helm', 'armor', 'necklace', 'necklace', 'ring', 'ring', 'boots']
        expected_mainstat_ids = ['0', '2', '4', '3', '0', '9', '8', '10']
        for i, val in enumerate(valid_inputs):
            with self.subTest(gear_type=val):
                for j in range(1000):
                    expected_mainstats = expected_mainstat_ids[i]
                    picked_mainstat_id = test_get_mainstat_id(gear_type=val, mainstat_id=expected_mainstats)
                    self.assertEqual(picked_mainstat_id, expected_mainstats)
                    
                    
    def test_subs_main_provided(self):
        """
        If we specify a gear type along with correct mainstats and substats, 
        we'll get the mainstat back.
        """
        valid_inputs = ['weapon', 'helm', 'armor', 'necklace', 'necklace', 'ring', 'ring', 'boots']
        expected_mainstat_ids = ['0', '2', '4', '3', '0', '9', '8', '10']
        valid_subs = [
            3,
            [0, 10, 7],
            [10, 6, 7, 8],
            [1, 2, 10, 4],
            [6, 7, 8],
            1,
            [3, 4, 2, 5],
            [0, 1, 2, 3]
        ]
        for i, val in enumerate(valid_inputs):
            with self.subTest(gear_type=val):
                for j in range(1000):
                    expected_mainstats = expected_mainstat_ids[i]
                    picked_mainstat_id = test_get_mainstat_id(gear_type=val, mainstat_id=expected_mainstats, substat_ids=valid_subs[i])
                    self.assertEqual(picked_mainstat_id, expected_mainstats)
                    
                    
    def test_subs_no_main_provided(self):
        """
        If we specify a gear type along with substats, 
        we'll get an appropriate mainstat back that is not already in the substat.
        """
        valid_inputs = ['weapon', 'helm', 'armor', 'necklace', 'necklace', 'ring', 'ring', 'boots']
        valid_subs = [
            3,
            [0, 10, 7],
            [10, 6, 7, 8],
            [1, 2, 10, 4],
            [6, 7, 8],
            1,
            [3, 4, 2, 5],
            [0, 1, 2, 3]
        ]
        expected_mainstat_ids = ['0', 
                                 '2', 
                                 '4', 
                                 ['0', '3', '5', '6', '7', '8', '9'],
                                 ['0', '1', '2', '3', '4', '5', '9', '10'],
                                 ['0', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
                                 ['0', '1', '6', '7', '8', '9', '10'],
                                 ['4', '5', '10']
                                ]
        for i, val in enumerate(valid_inputs):
            with self.subTest(gear_type=val, substats=valid_subs[i]):
                for j in range(1000):
                    expected_mainstats = expected_mainstat_ids[i]
                    picked_mainstat_id = test_get_mainstat_id(gear_type=val, substat_ids=valid_subs[i])
                    self.assertIn(picked_mainstat_id, expected_mainstats)
            
             
if __name__ == '__main__':
    unittest.main()