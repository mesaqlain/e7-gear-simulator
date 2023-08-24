# Add parent directory to path
from set_directory_function import set_directory
set_directory()

# Imports
import unittest
import json
import random
from tests.test_class_gear_v4 import Gear 
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
    
    def setUp(self):
        self.gear = Gear()
        
        
    def tearDown(self):
        self.gear = None
        
        
    def test_initial_attributes(self):
        """
        Tests whether the initial values of the attributes are as we expect
        """
        self.assertIsNone(self.gear.gear_type)
        self.assertIsNone(self.gear.gear_grade)
        self.assertIsNone(self.gear.gear_set)
        self.assertEqual(self.gear.gear_level, 85, "gear level should be 85")
        self.assertEqual(self.gear.gear_tier, 6, "gear tier should be 6")
        self.assertEqual(self.gear.enhance_level, 0, "enhance level should be 0")
        self.assertFalse(self.gear.is_reforged)
        self.assertIsNone(self.gear.mainstat)
        self.assertIsNone(self.gear.substats)
        self.assertIsNone(self.gear.mainstat_id)
        self.assertIsNone(self.gear.substat_ids)

        
        
    def test_create_gear_default(self):
        """
        Tests whether the initial values of the attributes are as we expect when we use 
        create_gear() method. As no args are provided, gear_type, gear_grade mainstat_id, substat_id's should be 
        completely random and we expect to see every gear_type and gear_grade picked at least once.
        """
        expected_gear_types = list(TYPES.keys())
        expected_gear_grades = ['rare', 'heroic', 'epic']
        expected_gear_sets = list(SETS.keys())
        
        for i in range(1000):
            self.gear.create_gear()
            
            gear_grade = self.gear.gear_grade
            gear_type = self.gear.gear_type
            gear_level = self.gear.gear_level
            gear_tier = self.gear.gear_tier
            gear_set = self.gear.gear_set
            substat_ids = self.gear.substat_ids
            mainstat_id = self.gear.mainstat_id
        
            expected_mainstat_id_list = convert_int_to_str(TYPES[gear_type]['mainstat'])
            expected_substat_id_list = convert_int_to_str(TYPES[gear_type]['substat'])
            expected_number_of_subs = GRADES[gear_grade]['starting_substats']
            
            no_of_subs = len(substat_ids)
                        
            self.assertIn(gear_type, expected_gear_types)
            self.assertIn(gear_grade, expected_gear_grades)
            
            self.assertIn(gear_set, expected_gear_sets)
            self.assertEqual(gear_level, 85, "gear level should be 85")
            self.assertEqual(gear_tier, 6, "gear tier should be 6")
            self.assertIsNone(self.gear.mainstat) # TODO in v5
            self.assertIsNone(self.gear.substats) # TODO in v5
            self.assertIn(self.gear.mainstat_id, expected_mainstat_id_list)
            # Check if we got appropriate number of substats based on grade
            self.assertEqual(no_of_subs, expected_number_of_subs)
            # Check that all substat id's are in expected list
            for s in substat_ids:
                self.assertIn(s, expected_substat_id_list)
            # Check that mainstat is not in substat:
            self.assertNotIn(mainstat_id, substat_ids)
            
        
    def test_create_gear_specify_level(self):
        """
        Tests whether the initial values of the attributes are as we expect when we use 
        create_gear() method. As no args are provided, gear_type and gear_grade should be 
        completely random and we expect to see every gear_type and gear_grade picked at least once.
        The mainstat id should also be randomly picked from the available pool given the gear type chosen.
        """
        
        input_level_list = [70, 85, 88, 90, None]
        expected_level_list = [70, 85, 88, 90, 85]
        expected_tier_list = [5, 6, 7, 7, 6]
        expected_gear_types = list(TYPES.keys())
        expected_gear_grades = ['rare', 'heroic', 'epic']
        expected_gear_sets = list(SETS.keys())
        
        for l, lvl in enumerate(input_level_list):
            
            input_level = lvl
            expected_level = expected_level_list[l]
            expected_tier = expected_tier_list[l]
            
            with self.subTest(level=input_level):
                for i in range(100):
                    self.gear.create_gear(gear_level=input_level)

                    gear_grade = self.gear.gear_grade
                    gear_type = self.gear.gear_type
                    gear_level = self.gear.gear_level
                    gear_tier = self.gear.gear_tier
                    gear_set = self.gear.gear_set
                    substat_ids = self.gear.substat_ids
                    mainstat_id = self.gear.mainstat_id

                    expected_mainstat_id_list = convert_int_to_str(TYPES[gear_type]['mainstat'])
                    expected_substat_id_list = convert_int_to_str(TYPES[gear_type]['substat'])
                    expected_number_of_subs = GRADES[gear_grade]['starting_substats']

                    no_of_subs = len(substat_ids)

                    self.assertIn(gear_type, expected_gear_types)
                    self.assertIn(gear_grade, expected_gear_grades)

                    self.assertIn(gear_set, expected_gear_sets)
                    self.assertEqual(gear_level, expected_level, f"gear level should be {expected_level}")
                    self.assertEqual(gear_tier, expected_tier, f"gear tier should be {expected_tier}")
                    self.assertIsNone(self.gear.mainstat) # TODO in v5
                    self.assertIsNone(self.gear.substats) # TODO in v5
                    self.assertIn(self.gear.mainstat_id, expected_mainstat_id_list)
                    # Check if we got appropriate number of substats based on grade
                    self.assertEqual(no_of_subs, expected_number_of_subs)
                    # Check that all substat id's are in expected list
                    for s in substat_ids:
                        self.assertIn(s, expected_substat_id_list)
                    # Check that mainstat is not in substat:
                    self.assertNotIn(mainstat_id, substat_ids)
                    
                    
    def test_create_gear_specify_level_set(self):
        """
        Tests whether the initial values of the attributes are as we expect when we use 
        create_gear() method. As no args are provided, gear_type and gear_grade should be 
        completely random and we expect to see every gear_type and gear_grade picked at least once.
        The mainstat id should also be randomly picked from the available pool given the gear type chosen.
        """
        
        input_set_list = ['health', 'torrent', 'revenge']
        input_level_list = [70, 85, 88, 90, None]
        expected_level_list = [70, 85, 88, 90, 85]
        expected_tier_list = [5, 6, 7, 7, 6]
        expected_gear_types = list(TYPES.keys())
        expected_gear_grades = ['rare', 'heroic', 'epic']
        
        for l, lvl in enumerate(input_level_list):
            for s in input_set_list:
            
                input_level = lvl
                input_set = s
                expected_set = s
                expected_level = expected_level_list[l]
                expected_tier = expected_tier_list[l]

                with self.subTest(level=input_level):
                    for i in range(100):
                        self.gear.create_gear(gear_level=input_level, gear_set=input_set)

                        gear_grade = self.gear.gear_grade
                        gear_type = self.gear.gear_type
                        gear_level = self.gear.gear_level
                        gear_tier = self.gear.gear_tier
                        gear_set = self.gear.gear_set
                        substat_ids = self.gear.substat_ids
                        mainstat_id = self.gear.mainstat_id

                        expected_mainstat_id_list = convert_int_to_str(TYPES[gear_type]['mainstat'])
                        expected_substat_id_list = convert_int_to_str(TYPES[gear_type]['substat'])
                        expected_number_of_subs = GRADES[gear_grade]['starting_substats']

                        no_of_subs = len(substat_ids)

                        self.assertIn(gear_type, expected_gear_types)
                        self.assertIn(gear_grade, expected_gear_grades)

                        self.assertIn(gear_set, expected_set)
                        self.assertEqual(gear_level, expected_level, f"gear level should be {expected_level}")
                        self.assertEqual(gear_tier, expected_tier, f"gear tier should be {expected_tier}")
                        self.assertIsNone(self.gear.mainstat) # TODO in v5
                        self.assertIsNone(self.gear.substats) # TODO in v5
                        self.assertIn(self.gear.mainstat_id, expected_mainstat_id_list)
                        # Check if we got appropriate number of substats based on grade
                        self.assertEqual(no_of_subs, expected_number_of_subs)
                        # Check that all substat id's are in expected list
                        for s in substat_ids:
                            self.assertIn(s, expected_substat_id_list)
                        # Check that mainstat is not in substat:
                        self.assertNotIn(mainstat_id, substat_ids)                    
        
        
    def test_create_gear_specify_level_set_type(self):
        """
        Tests whether the initial values of the attributes are as we expect when we use 
        create_gear() method. As no args are provided, gear_type and gear_grade should be 
        completely random and we expect to see every gear_type and gear_grade picked at least once.
        The mainstat id should also be randomly picked from the available pool given the gear type chosen.
        """
        input_types_list = ['weapon', 'helm', 'armor', 'necklace', 'ring', 'boots']
        input_set_list = ['health', 'torrent', 'revenge']
        input_level_list = [70, 85, 88, 90, None]
        expected_level_list = [70, 85, 88, 90, 85]
        expected_tier_list = [5, 6, 7, 7, 6]
        expected_gear_types = list(TYPES.keys())
        expected_gear_grades = ['rare', 'heroic', 'epic']
        
        for l, lvl in enumerate(input_level_list):
            for t, type_ in enumerate(input_types_list):
                for s in input_set_list:

                    input_type = type_
                    input_level = lvl
                    input_set = s
                    expected_type = type_
                    expected_level = expected_level_list[l]
                    expected_set = s
                    expected_tier = expected_tier_list[l]
                    expected_mainstat_id_list = convert_int_to_str(TYPES[expected_type]['mainstat'])
                    expected_substat_id_list = convert_int_to_str(TYPES[expected_type]['substat'])

                    with self.subTest(level=input_level, type_=input_type):
                        for i in range(100):
                            self.gear.create_gear(gear_level=input_level, gear_set=input_set, gear_type=input_type)

                            gear_grade = self.gear.gear_grade
                            gear_type = self.gear.gear_type
                            gear_level = self.gear.gear_level
                            gear_tier = self.gear.gear_tier
                            gear_set = self.gear.gear_set
                            substat_ids = self.gear.substat_ids
                            mainstat_id = self.gear.mainstat_id

                            expected_number_of_subs = GRADES[gear_grade]['starting_substats']

                            no_of_subs = len(substat_ids)

                            self.assertIn(gear_type, expected_type)
                            self.assertIn(gear_grade, expected_gear_grades)

                            self.assertIn(gear_set, expected_set)
                            self.assertEqual(gear_level, expected_level, f"gear level should be {expected_level}")
                            self.assertEqual(gear_tier, expected_tier, f"gear tier should be {expected_tier}")
                            self.assertIsNone(self.gear.mainstat) # TODO in v5
                            self.assertIsNone(self.gear.substats) # TODO in v5
                            self.assertIn(self.gear.mainstat_id, expected_mainstat_id_list)
                            # Check if we got appropriate number of substats based on grade
                            self.assertEqual(no_of_subs, expected_number_of_subs)
                            # Check that all substat id's are in expected list
                            for s in substat_ids:
                                self.assertIn(s, expected_substat_id_list)
                            # Check that mainstat is not in substat:
                            self.assertNotIn(mainstat_id, substat_ids)            
        
        
    def test_create_gear_specific_values(self):
        """
        Tests whether the initial values of the attributes are as we expect when we use 
        create_gear() method. As no args are provided, gear_type, gear_grade mainstat_id, substat_id's should be 
        completely random and we expect to see every gear_type and gear_grade picked at least once.
        """
        input_substat_ids = [
            [0, 3, 4],
            [10, 4, 0, 3],
            [1, 3, 4],
            [3, 5, 7],
            [2, 0],
            [10, 6]
        ]
        input_mainstat_ids = [10, 6, 8, 2, 7, 9]
        expected_gear_types_list = [
            ['boots'],
            ['necklace'],
            ['ring'],
            ['helm', 'necklace', 'ring', 'boots'],
            ['necklace'],
            ['ring']
        ]
        expected_gear_grades_list = [
            ['heroic', 'epic'],
            ['epic'],
            ['heroic', 'epic'],
            ['heroic', 'epic'],
            ['rare', 'heroic', 'epic'],
            ['rare', 'heroic', 'epic']
        ]
        expected_gear_sets_list = list(SETS.keys())
        
        for j, m_id in enumerate(input_mainstat_ids):
            input_mainstat = m_id
            input_substats = input_substat_ids[j]
            expected_gear_types = expected_gear_types_list[j]
            expected_gear_grades = expected_gear_grades_list[j]
            
            for i in range(1000):
                self.gear.create_gear(substat_ids=input_substats, mainstat_id=input_mainstat)

                gear_grade = self.gear.gear_grade
                gear_type = self.gear.gear_type
                gear_level = self.gear.gear_level
                gear_tier = self.gear.gear_tier
                gear_set = self.gear.gear_set
                substat_ids = self.gear.substat_ids
                mainstat_id = self.gear.mainstat_id

                expected_substat_id_list = convert_int_to_str(TYPES[gear_type]['substat'])
                expected_number_of_subs = GRADES[gear_grade]['starting_substats']
                no_of_subs = len(substat_ids)

                self.assertIn(gear_type, expected_gear_types)
                self.assertIn(gear_grade, expected_gear_grades)

                self.assertIn(gear_set, expected_gear_sets_list)
                self.assertEqual(gear_level, 85, "gear level should be 85")
                self.assertEqual(gear_tier, 6, "gear tier should be 6")
                self.assertIsNone(self.gear.mainstat) # TODO in v5
                self.assertIsNone(self.gear.substats) # TODO in v5
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
        with self.assertRaises(ValueError):
            self.gear.create_gear(gear_type='weapon', gear_set='health', gear_level=90, 
                                  gear_grade='heroic', mainstat_id=3, substat_ids=[1,2,3,4])
            
            
    def test_create_gear_specify_invalid_2(self):
        """
        Tests whether we get ValueError when we there are duplicates in substats
        """
        with self.assertRaises(ValueError):
            self.gear.create_gear(gear_type='weapon', gear_set='health', gear_level=90, 
                                  gear_grade='heroic', mainstat_id=3, substat_ids=[1,2,4,4])
            
            
    def test_create_gear_specify_invalid_3(self):
        """
        Tests whether we get ValueError when we we specify incorrect mainstat with gear_type
        """
        with self.assertRaises(ValueError):
            self.gear.create_gear(gear_type='weapon', gear_set='health', gear_level=90, 
                                  gear_grade='heroic', mainstat_id=3, substat_ids=[1,2,10,9])
            
            
    def test_create_gear_specify_invalid_4(self):
        """
        Tests whether we get ValueError when we we specify incorrect substat with gear_type
        """
        with self.assertRaises(ValueError):
            self.gear.create_gear(gear_type='weapon', gear_set='health', gear_level=90, 
                                  gear_grade='heroic', mainstat_id=0, substat_ids=[1,4,10,9])
            
            
    def test_create_gear_specify_invalid_5(self):
        """
        Tests whether we get ValueError when we we specify incorrect substats number with gear_grade
        e.g. Heroic cannot have 4 substats, if changed to epic, following passes.
        """
        with self.assertRaises(ValueError):
            self.gear.create_gear(gear_type='weapon', gear_set='health', gear_level=90, 
                                  gear_grade='heroic', mainstat_id=0, substat_ids=[6,7,10,9])
            
            
    def test_create_gear_specify_invalid_6(self):
        """
        Tests whether we get ValueError when we we specify too many substats
        """
        with self.assertRaises(ValueError):
            self.gear.create_gear(gear_type='weapon', gear_set='health', gear_level=90, 
                                  mainstat_id=0, substat_ids=[6,7,10,9,10])
            
            
    def test_create_gear_specify_invalid_7(self):
        """
        Tests whether we get ValueError when we we specify incorrect gear_grade and substats no
        e.g. heroic cannot have 4 starting subs
        """
        with self.assertRaises(ValueError):
            self.gear.create_gear(gear_type='weapon', gear_set='health', gear_level=90, gear_grade = 'heroic',
                                  mainstat_id=0, substat_ids=[6, 7, 10, 9])
            
if __name__ == "__main__":
    unittest.main()