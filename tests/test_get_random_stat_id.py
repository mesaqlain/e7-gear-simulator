from set_directory_function import set_directory
set_directory()

import unittest
import json
import random
from src.utilities import get_random_stat_id, convert_int_to_str

with open('data/types.json', 'r') as types_file:
    TYPES = json.load(types_file)
with open('data/stats.json', 'r') as stats_file:
    STATS = json.load(stats_file)
    
class TestGetRandomStatID(unittest.TestCase):
    
    def test_get_random_stat_id_no_args(self):
        """
        We should get every possible stat id if no args are provided.
        """
        expected_stats = list(STATS.keys())
        
        for i in range(1000):
            stat_id = get_random_stat_id()
            self.assertIn(stat_id, expected_stats, f"{stat_id} not in expected {expected_stats}")
            self.assertTrue(isinstance(stat_id, str))

            
    def test_get_random_stat_no_gear_type_subs(self):
        """
        We should get every possible stat id if no gear_type is provided but we specify substats.
        """
        expected_stats = list(STATS.keys())
        
        for i in range(1000):
            stat_id = get_random_stat_id(stat_type = 'substat')
            self.assertIn(stat_id, expected_stats, f"{stat_id} not in expected {expected_stats}")
            self.assertTrue(isinstance(stat_id, str))
            
            
    def test_get_random_stat_no_gear_type_main(self):
        """
        We should get every possible stat id if no gear_type is provided but we specify substats.
        """
        expected_stats = list(STATS.keys())
        
        for i in range(1000):
            stat_id = get_random_stat_id(stat_type = 'mainstat')
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
                stat_id = get_random_stat_id(gear_type=t, stat_type = 'mainstat')
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
                stat_id = get_random_stat_id(gear_type=t, stat_type = 'substat')
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
                stat_id = get_random_stat_id(gear_type=t)
                self.assertIn(stat_id, expected_stats, f"{stat_id} not in expected {expected_stats}")
                self.assertTrue(isinstance(stat_id, str))
                
        
if __name__ == '__main__':
    unittest.main()
