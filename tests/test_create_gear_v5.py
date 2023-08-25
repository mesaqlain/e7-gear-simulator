# Add parent directory to path
from set_directory_function import set_directory
set_directory()

# Imports
import unittest
import json
import random
from tests.test_class_gear_v5 import Gear 
from src.stats import Stat
from src.validation_utils import *
from src.utilities import get_random_gear_type, convert_int_to_str

# Data
with open('data/types.json', 'r') as types_file:
    TYPES = json.load(types_file)
with open('data/sets.json', 'r') as sets_file:
    SETS = json.load(sets_file)
with open('data/grades.json', 'r') as grades_file:
    GRADES = json.load(grades_file)

class TestGetGearType(unittest.TestCase):
    """
    Test the test version of Gear() class from tests/test_class_gear_v5.py
    """
            
    def test_initial_attributes(self):
        """
        Tests whether the initial values of the attributes are as we expect
        """
        self.gear = Gear()
        
        self.assertIsNone(self.gear.gear_type)
        self.assertIsNone(self.gear.gear_grade)
        self.assertIsNone(self.gear.gear_set)
        self.assertEqual(self.gear.gear_level, 85, "gear level should be 85")
        self.assertEqual(self.gear.gear_tier, 6, "gear tier should be 6")
        self.assertEqual(self.gear.enhance_level, 0, "enhance level should be 0")
        self.assertFalse(self.gear.is_reforged)
        self.assertIsNone(self.gear.mainstat)
        self.assertEqual(self.gear.substats, [])
        self.assertIsNone(self.gear.mainstat_id)
        self.assertIsNone(self.gear.substat_ids)

        
    def assert_stat_values(self, stat, expected):
        
        stat_id = stat.stat_id
        stat_type = stat.stat_type
        stat_value = stat.value
        stat_rolled = stat.rolled
        stat_modded = stat.modded
        
        self.assertIn(stat_id, expected[0])
        self.assertEqual(stat_type, expected[1])
        self.assertIn(stat_value, expected[2])
        self.assertEqual(stat_rolled, expected[3])
        if expected[4]:
            self.assertTrue(stat_modded)
        else:
            self.assertFalse(stat_modded)
        
        
        
    def test_create_gear_default(self):
        """
        Tests whether the initial values of the attributes are as we expect when we use 
        create_gear() method. As no args are provided, gear_type, gear_grade mainstat_id, substat_id's should be 
        completely random and we expect to see every gear_type and gear_grade picked at least once. The mainstat and substat attributes should 
        also hold some parsed stat info and we need to test those.
        """
        expected_gear_types = list(TYPES.keys())
        expected_gear_grades = ['rare', 'heroic', 'epic']
        expected_gear_sets = list(SETS.keys())
        
        for i in range(1000):
            self.gear = Gear()
            self.gear.create_gear()
            
            gear_grade = self.gear.gear_grade
            gear_type = self.gear.gear_type
            gear_level = self.gear.gear_level
            gear_tier = self.gear.gear_tier
            gear_set = self.gear.gear_set
            substat_ids = self.gear.substat_ids
            mainstat_id = self.gear.mainstat_id
            mainstat = self.gear.mainstat
            substats = self.gear.substats
            no_of_parsed_subs = len(substats)
        
            expected_mainstat_id_list = convert_int_to_str(TYPES[gear_type]['mainstat'])
            expected_substat_id_list = convert_int_to_str(TYPES[gear_type]['substat'])
            expected_number_of_subs = GRADES[gear_grade]['starting_substats']
                      
            no_of_subs = len(substat_ids)

                        
            self.assertIn(gear_type, expected_gear_types)
            self.assertIn(gear_grade, expected_gear_grades)
            
            self.assertIn(gear_set, expected_gear_sets)
            self.assertEqual(gear_level, 85, "gear level should be 85")
            self.assertEqual(gear_tier, 6, "gear tier should be 6")
            self.assertIsNotNone(self.gear.mainstat) 
            self.assertIsNotNone(self.gear.substats) 
            # Check if we parsed appropriate number of subs
            self.assertEqual(no_of_parsed_subs, expected_number_of_subs)
            self.assertIn(self.gear.mainstat_id, expected_mainstat_id_list)
            self.assertIn(self.gear.mainstat.stat_id, expected_mainstat_id_list)
            self.assertIsInstance(self.gear.mainstat, Stat)
            for k in self.gear.substats:
                self.assertIsInstance(k, Stat)
            # Check if we got appropriate number of substats based on grade
            self.assertEqual(no_of_subs, expected_number_of_subs)
            # Check that all substat id's are in expected list
            for s in substat_ids:
                self.assertIn(s, expected_substat_id_list)
            # Check that mainstat is not in substat:
            self.assertNotIn(mainstat_id, substat_ids)
            
        
    def test_create_gear_specific_values(self):
        """
        Tests whether the values of the attributes are as we expect when we use 
        create_gear() method. We provide specific values and see if we get proper parsed values.
        """
        
        expected_tier = [6, 5, 7, 7, 7, 6]
        input_substat_ids = [
            [0, 3, 4],
            [10, 4, 0, 3],
            [1, 3, 4],
            [3, 5, 7]
        ]
        expected_substat_values_list = [
            [list(range(27,41)), list(range(4,8)), list(range(22,31))],
            [[2,3,4,5], list(range(28,36)), list(range(33, 47)), [4,5,6,7,8]],
            [[5,6,7,8,9], [5,6,7,8,9], list(range(30,41))],
            [[5,6,7,8,9], [5,6,7,8,9], [4,5,6,7,8]]
        ]
        input_gear_level_list = [70, 85, 88, 90]
        expected_tier = [5, 6, 7, 7]
        input_mainstat_ids = [10, 6, 8, 2]
        expected_mainstat_values_list = [8, 11, 13, 553]
        expected_gear_types_list = [
            ['boots'],
            ['necklace'],
            ['ring'],
            ['helm', 'necklace', 'ring', 'boots']
        ]
        expected_gear_grades_list = [
            ['heroic', 'epic'],
            ['epic'],
            ['heroic', 'epic'],
            ['heroic', 'epic']
        ]
        expected_gear_sets_list = list(SETS.keys())
        
        for j, m_id in enumerate(input_mainstat_ids):
            input_mainstat = m_id
            input_substats = input_substat_ids[j]
            input_gear_level = input_gear_level_list[j]
            expected_gear_types = expected_gear_types_list[j]
            expected_gear_grades = expected_gear_grades_list[j]
            expected_gear_level = input_gear_level
            expected_gear_tier = expected_tier[j]
            
            expected_mainstat_values = expected_mainstat_values_list[j]
            expected_substat_values = expected_substat_values_list[j]
            
            for i in range(1000):
                self.gear = Gear()
                self.gear.create_gear(substat_ids=input_substats, mainstat_id=input_mainstat, gear_level=input_gear_level)

                gear_grade = self.gear.gear_grade
                gear_type = self.gear.gear_type
                gear_level = self.gear.gear_level
                gear_tier = self.gear.gear_tier
                gear_set = self.gear.gear_set
                substat_ids = self.gear.substat_ids
                mainstat_id = self.gear.mainstat_id
                maintat_info = self.gear.mainstat
                substats_info = self.gear.substats
                
                # Check mainstat info
                expect_mainstat_info = [[str(input_mainstat)], 'mainstat', [expected_mainstat_values], 0, False]
                self.assert_stat_values(maintat_info, expect_mainstat_info)
                
                # Check each substat info from the ones that were input
                for s,val in enumerate(input_substats):
                    expected_substat_info = [[str(val)], 'substat', expected_substat_values[s], 0, False]
                    substat = substats_info[s]
                    self.assert_stat_values(substat, expected_substat_info)

                expected_substat_id_list = convert_int_to_str(TYPES[gear_type]['substat'])
                expected_number_of_subs = GRADES[gear_grade]['starting_substats']
                no_of_subs = len(substat_ids)

                self.assertIn(gear_type, expected_gear_types)
                self.assertIn(gear_grade, expected_gear_grades)

                self.assertIn(gear_set, expected_gear_sets_list)
                self.assertEqual(gear_level, expected_gear_level, f"gear level should be {expected_gear_level}")
                self.assertEqual(gear_tier, expected_gear_tier, f"gear tier should be {expected_gear_tier}")
                self.assertIsInstance(self.gear.mainstat, Stat)
                for k in self.gear.substats:
                    self.assertIsInstance(k, Stat)
                    
                self.assertEqual(maintat_info.stat_id, str(input_mainstat))

                # self.assertIsNone(self.gear.substats) 
                self.assertEqual(self.gear.mainstat_id, str(input_mainstat))
                # Check if we got appropriate number of substats based on grade
                self.assertEqual(no_of_subs, expected_number_of_subs)
                # Check that all substat id's are in expected list
                for s in substat_ids:
                    self.assertIn(s, expected_substat_id_list)
                # Check that mainstat is not in substat:
                self.assertNotIn(mainstat_id, substat_ids)
                    
        
    def test_create_gear_specify_invalid_1(self):
        """
        Tests whether we get ValueError when we mainstat is in substat
        """
        self.gear = Gear()
        with self.assertRaises(ValueError):
            self.gear.create_gear(gear_type='weapon', gear_set='health', gear_level=90, 
                                  gear_grade='heroic', mainstat_id=3, substat_ids=[1,2,3,4])
            
            
    def test_create_gear_specify_invalid_2(self):
        """
        Tests whether we get ValueError when we there are duplicates in substats
        """
        self.gear = Gear()
        with self.assertRaises(ValueError):
            self.gear.create_gear(gear_type='weapon', gear_set='health', gear_level=90, 
                                  gear_grade='heroic', mainstat_id=3, substat_ids=[1,2,4,4])
            
            
    def test_create_gear_specify_invalid_3(self):
        """
        Tests whether we get ValueError when we we specify incorrect mainstat with gear_type
        """
        self.gear = Gear()
        with self.assertRaises(ValueError):
            self.gear.create_gear(gear_type='weapon', gear_set='health', gear_level=90, 
                                  gear_grade='heroic', mainstat_id=3, substat_ids=[1,2,10,9])
            
            
    def test_create_gear_specify_invalid_4(self):
        """
        Tests whether we get ValueError when we we specify incorrect substat with gear_type
        """
        self.gear = Gear()
        with self.assertRaises(ValueError):
            self.gear.create_gear(gear_type='weapon', gear_set='health', gear_level=90, 
                                  gear_grade='heroic', mainstat_id=0, substat_ids=[1,4,10,9])
            
            
    def test_create_gear_specify_invalid_5(self):
        """
        Tests whether we get ValueError when we we specify incorrect substats number with gear_grade
        e.g. Heroic cannot have 4 substats, if changed to epic, following passes.
        """
        self.gear = Gear()
        with self.assertRaises(ValueError):
            self.gear.create_gear(gear_type='weapon', gear_set='health', gear_level=90, 
                                  gear_grade='heroic', mainstat_id=0, substat_ids=[6,7,10,9])
            
            
    def test_create_gear_specify_invalid_6(self):
        """
        Tests whether we get ValueError when we we specify too many substats
        """
        self.gear = Gear()
        with self.assertRaises(ValueError):
            self.gear.create_gear(gear_type='weapon', gear_set='health', gear_level=90, 
                                  mainstat_id=0, substat_ids=[6,7,10,9,10])
            
            
    def test_create_gear_specify_invalid_7(self):
        """
        Tests whether we get ValueError when we we specify incorrect gear_grade and substats no
        e.g. heroic cannot have 4 starting subs
        """
        self.gear = Gear()
        with self.assertRaises(ValueError):
            self.gear.create_gear(gear_type='weapon', gear_set='health', gear_level=90, gear_grade = 'heroic',
                                  mainstat_id=0, substat_ids=[6, 7, 10, 9])
            
if __name__ == "__main__":
    unittest.main()