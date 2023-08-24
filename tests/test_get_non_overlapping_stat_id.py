from set_directory_function import set_directory
set_directory()

import unittest
import json
import random
from src.utilities import get_random_stat_id, convert_int_to_str, get_non_overlapping_stat_id

with open('data/types.json', 'r') as types_file:
    TYPES = json.load(types_file)
with open('data/stats.json', 'r') as stats_file:
    STATS = json.load(stats_file)
    
class TestGetNonOverlappingStatID(unittest.TestCase):
    
    def test_get_random_stat_id_no_args(self):
        """
        We should get every possible stat id if no args are provided.
        """
        expected_stats = list(STATS.keys())
        
        for i in range(1000):
            stat_id = get_non_overlapping_stat_id()
            self.assertIn(stat_id, expected_stats, f"{stat_id} not in expected {expected_stats}")
            self.assertTrue(isinstance(stat_id, str))

            
    def test_get_random_stat_no_gear_type_subs(self):
        """
        We should get every possible stat id if no gear_type is provided but we specify substats.
        """
        expected_stats = list(STATS.keys())
        
        for i in range(1000):
            stat_id = get_non_overlapping_stat_id(stat_type = 'substat')
            self.assertIn(stat_id, expected_stats, f"{stat_id} not in expected {expected_stats}")
            self.assertTrue(isinstance(stat_id, str))
            
            
    def test_get_random_stat_no_gear_type_main(self):
        """
        We should get every possible stat id if no gear_type is provided but we specify substats.
        """
        expected_stats = list(STATS.keys())
        
        for i in range(1000):
            stat_id = get_non_overlapping_stat_id(stat_type = 'mainstat')
            self.assertIn(stat_id, expected_stats, f"{stat_id} not in expected {expected_stats}")
            self.assertTrue(isinstance(stat_id, str))
            
            
    def test_get_random_stat_main_and_gear(self):
        """
        We should get appropriate stat ids if we provide gear_type and mainstat.
        """
        input_gear_types_list = list(TYPES.keys())
        
        for t in input_gear_types_list:
            expected_stats = convert_int_to_str(TYPES[t]['mainstat'])
            for i in range(1000):
                stat_id = get_non_overlapping_stat_id(gear_type=t, stat_type = 'mainstat')
                self.assertIn(stat_id, expected_stats, f"{stat_id} not in expected {expected_stats}")
                self.assertTrue(isinstance(stat_id, str))
                
                
    def test_get_random_stat_subs_and_gear(self):
        """
        We should get appropriate stat ids if we provide gear_type and substats.
        """
        input_gear_types_list = list(TYPES.keys())
        
        for t in input_gear_types_list:
            expected_stats = convert_int_to_str(TYPES[t]['substat'])
            for i in range(1000):
                stat_id = get_non_overlapping_stat_id(gear_type=t, stat_type = 'substat')
                self.assertIn(stat_id, expected_stats, f"{stat_id} not in expected {expected_stats}")
                self.assertTrue(isinstance(stat_id, str))
                
                
    def test_get_random_stat_gear_only(self):
        """
        We should get appropriate stat ids for substats (default) if we provide gear_type 
        but don't specify stats as substats.
        """
        input_gear_types_list = list(TYPES.keys())
        
        for t in input_gear_types_list:
            expected_stats = convert_int_to_str(TYPES[t]['substat'])
            for i in range(1000):
                stat_id = get_non_overlapping_stat_id(gear_type=t)
                self.assertIn(stat_id, expected_stats, f"{stat_id} not in expected {expected_stats}")
                self.assertTrue(isinstance(stat_id, str))
                
                
    def test_get_random_stat_gear_only_selected_none(self):
        """
        We should get appropriate stat ids for substats (default) if we provide gear_type 
        but don't specify stats as substats. specify selected as None
        """
        input_gear_types_list = list(TYPES.keys())
        
        for t in input_gear_types_list:
            expected_stats = convert_int_to_str(TYPES[t]['substat'])
            for i in range(1000):
                stat_id = get_non_overlapping_stat_id(gear_type=t)
                self.assertIn(stat_id, expected_stats, f"{stat_id} not in expected {expected_stats}")
                self.assertTrue(isinstance(stat_id, str))
                
                
    def test_get_random_stat_gear_only_selected_none(self):
        """
        We should get appropriate stat ids for substats (default) if we provide gear_type 
        but don't specify stats as substats. specify selected as None
        """
        input_gear_types_list = list(TYPES.keys())
        
        for t in input_gear_types_list:
            expected_stats = convert_int_to_str(TYPES[t]['substat'])
            for i in range(1000):
                stat_id = get_non_overlapping_stat_id(selected_stats = None, gear_type=t)
                self.assertIn(stat_id, expected_stats, f"{stat_id} not in expected {expected_stats}")
                self.assertTrue(isinstance(stat_id, str))
                
                
    def test_get_random_stat_gear_only_selected_empty(self):
        """
        We should get appropriate stat ids for substats (default) if we provide gear_type 
        but don't specify stats as substats. specify selected as empty list
        """
        input_gear_types_list = list(TYPES.keys())
        
        for t in input_gear_types_list:
            expected_stats = convert_int_to_str(TYPES[t]['substat'])
            for i in range(1000):
                stat_id = get_non_overlapping_stat_id(selected_stats = [], gear_type=t)
                self.assertIn(stat_id, expected_stats, f"{stat_id} not in expected {expected_stats}")
                self.assertTrue(isinstance(stat_id, str))
                
                
    def test_get_non_overlapping_stats_valid_1(self):
        """
        Don't specify stat_type (should be substat by default), specify a single stat in selected_stats.
        Don't specify gear_type (so available pool should be everything but the one in selected)
        """
        input_stats_list = list(STATS.keys())
        selected_stats = []
        
        for t in input_stats_list:
            
            selected_stats.append(t)
            expected_stats = list(set(input_stats_list) - set(selected_stats))

            for i in range(1000):
                stat_id = get_non_overlapping_stat_id(selected_stats=selected_stats)
                self.assertIn(stat_id, expected_stats, f"{stat_id} not in expected {expected_stats}")
                self.assertTrue(isinstance(stat_id, str))
                
            selected_stats = []
            
            
    def test_get_non_overlapping_stats_valid_2(self):
        """
        Don't specify stat_type (should be substat by default), specify diferent stats in selected_stats.
        Don't specify gear_type (so available pool should be everything but the one in selected)
        """
        all_stats_list = list(STATS.keys())
        input_stats_list = [
            [0, 1],
            [2, 3, 4],
            [10, 5, 7, 9],
            [3, 4, 5, 0]
        ]
        
        for t in input_stats_list:
            selected_stats = convert_int_to_str(t)
            expected_stats = list(set(all_stats_list) - set(selected_stats))

            for i in range(1000):
                stat_id = get_non_overlapping_stat_id(selected_stats=selected_stats)
                self.assertIn(stat_id, expected_stats, f"{stat_id} not in expected {expected_stats}")
                self.assertTrue(isinstance(stat_id, str))
                
                
    def test_get_non_overlapping_stats_valid_3(self):
        """
        Don't specify stat_type (should be substat by default), specify diferent stats in selected_stats.
        Specify gear_type (so available pool should be restricted)
        """
        all_stats_list = list(STATS.keys())
        input_gear_types_list =['weapon', 'helm', 'armor', 'necklace', 'ring', 'boots']
        
        input_stats_list = [
            [0, 1],
            [2, 3, 4],
            [4, 5, 6, 10],
            [10, 5, 7, 9],
            [3, 4, 5, 0],
            [3, 4, 8]
        ]
        
        expected_stats_list = [
            [2, 3, 6, 7, 8, 9, 10],
            [0, 1, 5, 6, 7, 8, 9, 10],
            [2, 3, 7, 8, 9, 10],
            [0, 1, 2, 3, 4, 6, 8],
            [1, 2, 6, 7, 8, 9, 10],
            [0, 1, 2, 5, 6, 7, 9, 10]
        ]
        
        for t, val in enumerate(input_stats_list):
            selected_stats = convert_int_to_str(val)
            expected_stats = convert_int_to_str(expected_stats_list[t])
            input_gear_type = input_gear_types_list[t]
            
            with self.subTest(selected_stats=selected_stats, gear_type=input_gear_type):
                for i in range(1000):
                    stat_id = get_non_overlapping_stat_id(selected_stats=selected_stats, gear_type=input_gear_type)
                    self.assertIn(stat_id, expected_stats, f"{stat_id} not in expected {expected_stats}")
                    self.assertTrue(isinstance(stat_id, str))
                    
        
    def test_get_non_overlapping_stat_id_invalid_1(self):
        """
        Invalid ids (e.g. 11)
        """
        with self.assertRaises(ValueError):
            get_non_overlapping_stat_id([1, 2, 3, 4, 11])
            
            
    def test_get_non_overlapping_stat_id_invalid_2(self):
        """
        Invalid ids (e.g. -1)
        """
        with self.assertRaises(ValueError):
            get_non_overlapping_stat_id([1, 2, 3, 4, -1])
        
        
if __name__ == '__main__':
    unittest.main()
