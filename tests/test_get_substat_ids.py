from set_directory_function import set_directory
set_directory()

import random
import json
import unittest
from tests.test_functions import test_get_substat_ids
from src.utilities import convert_int_to_str

with open('data/types.json', 'r') as types_file:
    TYPES = json.load(types_file)
with open('data/stats.json', 'r') as stats_file:
    STATS = json.load(stats_file)

class TestGetSubstatIDs(unittest.TestCase):
    
    def test_all_none(self):
        """If no args are provided, we should get ValueError"""
        with self.assertRaises(ValueError):
            test_get_substat_ids()
            
    def test_none_2(self):
        """If no gear_type provided, we should get Value Error, even if substat_id is provided."""
        with self.assertRaises(ValueError):
            test_get_substat_ids(substat_ids = 1)
            
    def test_none_3(self):
        """If no gear_type provided, we should get Value Error, even if mainstat_id is provided."""
        with self.assertRaises(ValueError):
            test_get_substat_ids(mainstat_id = 1)
            
    def test_none_4(self):
        """If no gear_type provided, we should get Value Error, even if mainstat_id and substat_ids are provided."""
        with self.assertRaises(ValueError):
            test_get_substat_ids(mainstat_id = 1, substat_ids = [3, 4])
            
    def test_invalid_gear_type(self):
        """If invalid gear_type provided we'll get an error."""
        with self.assertRaises(ValueError):
            test_get_substat_ids('shirt')
            
    def test_invalid_gear_type_main(self):
        """If invalid mainstats given gear_type are provided we'll get an error."""
        valid_inputs = ['weapon', 'helm', 'armor', 'necklace', 'ring', 'boots']
        invalid_mains = [2, 10, 10, 8, 6, 7]
        for i, val in enumerate(valid_inputs):
            with self.assertRaises(ValueError):
                test_get_substat_ids(invalid_mains[i], gear_type=val)
                  
    def test_invalid_gear_type_subs(self):
        """If invalid substats given gear_type are provided we'll get an error."""
        valid_inputs = ['weapon', 'helm', 'armor']
        invalid_subs = [4, 2, 0]
        for i, val in enumerate(valid_inputs):
            with self.assertRaises(ValueError):
                test_get_substat_ids(invalid_subs[i], val)
                
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
                test_get_substat_ids(val, invalid_subs[i])
                
    def test_too_many_subs(self):
        """If too many subs are provided, we'll get an error."""
        with self.assertRaises(ValueError):
            test_get_substat_ids(substat_ids = [1, 2, 3, 4, 5])
            
    def test_too_many_subs(self):
        """If too many subs are provided, we'll get an error."""
        with self.assertRaises(ValueError):
            test_get_substat_ids(gear_type='ring', mainstat_id='8', gear_grade='epic', substat_ids = [1, 2, 3, 4, 5])
            
    def test_gear_grade_subs_nomatch(self):
        """If gear grade doesn't match the number of subs provided."""
        with self.assertRaises(ValueError):
            test_get_substat_ids(mainstat_id=0, gear_type='weapon', substat_ids = [1, 2, 3, 4], gear_grade = 'rare')
            
    def test_gear_grade_subs_nomatch_2(self):
        """If gear grade doesn't match the number of subs provided."""
        with self.assertRaises(ValueError):
            test_get_substat_ids(mainstat_id=0, gear_type='weapon', substat_ids = [1, 2, 3, 4], gear_grade = 'heroic')
            
    def test_gear_grade_subs_nomatch_3(self):
        """mainstat in substat."""
        with self.assertRaises(ValueError):
            test_get_substat_ids(mainstat_id=0, gear_type='weapon', substat_ids = [0, 2, 3, 4], gear_grade = 'epic')
                
                
    def test_all_possible_inputs(self):
        """
       Specify gear_type, gear_grade, and mainstat and test the combination of each.
       Don't specify substat_ids so we expect to get a wider pool of selected id's.
        """
        input_gear_types_list = ['weapon', 'helm', 'armor', 'necklace', 'ring', 'boots']
        input_mainstat_ids_list = [[0, 0], 
                                   [2, 2],
                                   [4, 4],
                                   [0, 1, 2, 3, 4, 5, 6, 7], 
                                   [0, 1, 2, 3, 4, 5, 8, 9], 
                                   [0, 1, 2, 3, 4, 5, 10]]
        input_gear_grades_list = ['normal', 'good', 'rare', 'heroic', 'epic']
        
        
        for t, val in enumerate(input_gear_types_list):
            for g in input_gear_grades_list:
                for m in input_mainstat_ids_list[t]:
                    
                    input_gear_type = val
                    input_gear_grade = g 
                    input_mainstat_id = m
                    
                    with self.subTest(gear_type=input_gear_type, mainstat_id=m, gear_grade=g):
                        for j in range(1000):
                            
                            picked_substat_ids = test_get_substat_ids(
                                mainstat_id=input_mainstat_id, 
                                gear_type=input_gear_type, 
                                gear_grade=input_gear_grade)
                            
                            substat_pool = convert_int_to_str(list(TYPES[input_gear_type]['substat']))
                            expected_substats = list(set(substat_pool) - set([input_mainstat_id]))
                            
                            self.assertTrue(all(s in expected_substats for s in picked_substat_ids))
                            self.assertTrue(m not in picked_substat_ids)
                            self.assertTrue(isinstance(picked_substat_ids, list))
                            
            
    def test_with_some_subs_and_mains(self):
        """
        Specify gear_type, gear_grade, and mainstat and test the combination of each.
        Specify substat_id's to restrict which id's may be picked. Since all of the elements have
        min starting subs of 2, we can include rare.
        """
        input_gear_types_list = ['weapon', 'weapon', 'helm', 'helm', 'armor', 'armor', 
                                 'necklace', 'necklace', 'ring', 'ring', 'boots', 'boots']
        input_substat_ids_list =[
            1, [7, 10], [6, 7], [8, 9], [10, 2], [5, 9],
            [3, 4], [0, 1], [10, 5], [3, 6], [2, 3], [3, 4]
        ]
        input_mainstat_ids_list =[0, 0, 2, 2, 4, 4, 0, 7, 8, 9, 10, 5]
        input_gear_grades_list = ['rare', 'heroic', 'epic']
        
        for t,val in enumerate(input_gear_types_list):
            for g in input_gear_grades_list:
                    
                    input_gear_type = val
                    input_gear_grade = g 
                    input_mainstat_id = input_mainstat_ids_list[t]
                    input_substat_ids = input_substat_ids_list[t]
                    
                    if not isinstance(input_substat_ids, list):
                        input_substat_ids = [input_substat_ids]
                    
                    with self.subTest(gear_type=input_gear_type, mainstat_id=input_mainstat_id, 
                                      substat_ids=input_substat_ids, gear_grade=g):
                        for j in range(1000):
                            
                            picked_substat_ids = test_get_substat_ids(
                                mainstat_id=input_mainstat_id, 
                                substat_ids=input_substat_ids,
                                gear_type=input_gear_type, 
                                gear_grade=input_gear_grade)
                            
                            substat_pool = convert_int_to_str(list(TYPES[input_gear_type]['substat']))
                            expected_substats = list(set(substat_pool) - set([input_mainstat_id]) - set(input_substat_ids))
                            
                            self.assertTrue(all(s in expected_substats for s in picked_substat_ids))
                            self.assertTrue(input_mainstat_id not in picked_substat_ids)
                            self.assertTrue(isinstance(picked_substat_ids, list))
                    
                    
    def test_with_some_subs_and_mains_2(self):
        """
        Specify gear_type, gear_grade, and mainstat and test the combination of each.
        Specify substat_id's to restrict which id's may be picked. Since some of the elements have
        starting subs of 3, we cannot include rare.
        """
        input_gear_types_list = ['weapon', 'weapon', 'helm', 'helm', 'armor', 'armor', 
                                 'necklace', 'necklace', 'ring', 'ring', 'boots', 'boots']
        input_substat_ids_list =[
            [1, 3, 8], [10], [6], [8, 9], [10, 2], [5, 9],
            [3, 4, 1], [0, 1, 10], [10], [6], [2, 3, 1], [4]
        ]
        input_mainstat_ids_list =[0, 0, 2, 2, 4, 4, 
                                  0, 7, 8, 9, 10, 5]
        input_gear_grades_list = ['heroic', 'epic']
        
        for t,val in enumerate(input_gear_types_list):
            for g in input_gear_grades_list:
                    
                    input_gear_type = val
                    input_gear_grade = g 
                    input_mainstat_id = input_mainstat_ids_list[t]
                    input_substat_ids = input_substat_ids_list[t]
                    
                    with self.subTest(gear_type=input_gear_type, mainstat_id=input_mainstat_id, 
                                      substat_ids=input_substat_ids, gear_grade=g):
                        for j in range(1000):
                            
                            picked_substat_ids = test_get_substat_ids(
                                mainstat_id=input_mainstat_id, 
                                substat_ids=input_substat_ids,
                                gear_type=input_gear_type, 
                                gear_grade=input_gear_grade)
                            
                            substat_pool = convert_int_to_str(list(TYPES[input_gear_type]['substat']))
                            expected_substats = list(set(substat_pool) - set([input_mainstat_id]) - set(input_substat_ids))
                            
                            self.assertTrue(all(s in expected_substats for s in picked_substat_ids))
                            self.assertTrue(input_mainstat_id not in picked_substat_ids)
                            self.assertTrue(isinstance(picked_substat_ids, list))          
                                        
             
if __name__ == '__main__':
    unittest.main()