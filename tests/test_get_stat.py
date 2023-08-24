from set_directory_function import set_directory
set_directory()

import unittest
from src.utilities import convert_int_to_str
from src.stats import Stat
from src.validation_utils import *
from tests.test_functions import test_get_stat

class TestGetStat(unittest.TestCase):
    
    def test_get_stat_valid_inputs(self):
        """
        Test whether we get appropriate outpus when we get a stat. We test various scenarios by using a variety of input values.
        For the mainstats, the value should be fixed, but for the substats, we expect a range of values, so we repeat the simulations
        1000 times to make sure we get everything. 
        """
        input_stat_id = [0, 3, 10, 5, 6, 7]
        input_stat_type = ['mainstat', 'substat', 'mainstat', 'substat', 'mainstat', 'substat']
        input_gear_type = ['weapon', 'ring', 'boots', 'helm', 'necklace', 'armor']
        input_gear_grade = ['heroic', 'rare', 'epic', 'rare', 'heroic', 'epic']
        input_gear_level = [85, 70, 86, 88, 90, 85]
        input_mod = [False, False, False, False, False, True]
        input_rolled = [None, 1, 0, None, None, 4]
        input_mod_type = ['greater', 'lesser', 'greater', 'lesser', 'greater', 'greater']
        input_show_reforged = [False, False, False, False, False, True]
        expected_reforge_increase_list = [525, 3, 45, 1, 60, 6]
        expected_value_list = [[100], list(range(4,7)), [9], list(range(5,9)), [12], list(range(13,17))]
        expected_modded = [False, False, False, True, False, True]
        
        expected_tier = [6, 5, 7, 7, 7, 6]
        expected_rolled_list = [0, 1, 0, 0, 0, 4]
        
        for i, val in enumerate(input_stat_id):
            with self.subTest(stat_id = val):
                for j in range(1000):
                    stat = test_get_stat(input_stat_id[i], input_stat_type[i], input_gear_type[i],
                                        input_gear_grade[i], input_gear_level[i], input_mod[i],
                                        input_rolled[i], input_mod_type[i], input_show_reforged[i])

                    expected_stat_id = val
                    expeced_stat_type = input_stat_type[i]
                    expected_gear_type = input_gear_type[i]
                    expected_gear_grade = input_gear_grade[i]
                    expected_gear_level = input_gear_level[i]
                    expected_gear_tier = expected_tier[i]
                    expected_rolled = expected_rolled_list[i]
                    expected_reforge_increase = expected_reforge_increase_list[i]
                    expected_value = expected_value_list[i]

                    self.assertEqual(stat.stat_id, str(expected_stat_id))
                    self.assertEqual(stat.stat_type, expeced_stat_type)
                    self.assertEqual(stat.gear_type, expected_gear_type)
                    self.assertEqual(stat.gear_grade, expected_gear_grade)
                    self.assertEqual(stat.gear_level, expected_gear_level)
                    self.assertEqual(stat.rolled, expected_rolled)
                    self.assertEqual(stat.gear_tier, expected_gear_tier)
                    self.assertIn(stat.value, expected_value)
                    
                    
    def test_get_stat_invalid_inputs(self):
        """
        We test some scenarios where we can expect to see invalid results, such as mainstats being modded, 
        rolled values out of bounds, gear level out of bounds, or stat not allowed in pool.
        Case 1: Mainstat and rolled >0
        Case 2: Invalid level
        Case 3: Mod True for mainstat
        Case 4: Invalid rolled value
        Case 5: Invalid mainstat id with gear
        Case 6: Invalid substat id with gear
        """
        input_stat_id = [0, 3, 7, 5, 10, 0]
        input_stat_type = ['mainstat', 'substat', 'mainstat', 'substat', 'mainstat', 'substat']
        input_gear_type = ['weapon', 'ring', 'boots', 'helm', 'necklace', 'armor']
        input_gear_grade = ['heroic', 'rare', 'epic', 'rare', 'heroic', 'epic']
        input_gear_level = [85, 50, 86, 88, 90, 85]
        input_mod = [False, False, True, False, False, True]
        input_rolled = [2, 1, 3, 9, None, 4]
        input_mod_type = ['greater', 'lesser', 'greater', 'lesser', 'greater', 'greater']
        input_show_reforged = [False, False, False, False, False, True]
        
        for i, val in enumerate(input_stat_id):
            with self.subTest(stat_id = val):
                for j in range(1000):
                    with self.assertRaises(ValueError):
                        stat = test_get_stat(input_stat_id[i], input_stat_type[i], input_gear_type[i],
                                             input_gear_grade[i], input_gear_level[i], input_mod[i],
                                             input_rolled[i], input_mod_type[i], input_show_reforged[i])



if __name__ == '__main__':
    unittest.main()