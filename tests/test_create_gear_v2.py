# Add parent directory to path
from set_directory_function import set_directory
set_directory()

# Imports
import unittest
import json
import random
from tests.test_class_gear_v2 import Gear 
from src.validation_utils import *
from src.utilities import get_random_gear_type, convert_int_to_str

# Data
with open('data/types.json', 'r') as types_file:
    TYPES = json.load(types_file)
with open('data/sets.json', 'r') as sets_file:
    SETS = json.load(sets_file)


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
        create_gear() method. As no args are provided, gear_type and gear_grade should be 
        completely random and we expect to see every gear_type and gear_grade picked at least once.
        """
        expected_gear_types_list = set(list(TYPES.keys()))
        expected_gear_grades_list = set(['rare', 'heroic', 'epic'])
        
        picked_gear_types = set()
        picked_gear_grades = set()

        for i in range(1000):
            self.gear.create_gear()
            
            gear_type = self.gear.gear_type
            gear_grade = self.gear.gear_grade
            
            picked_gear_types.add(gear_type)
            picked_gear_grades.add(gear_grade)
            
            expected_gear_types = list(expected_gear_types_list)
            expected_gear_grades = list(expected_gear_grades_list)
            
            self.assertIn(gear_type, expected_gear_types)
            self.assertIn(gear_grade, expected_gear_grades)
            
            self.assertIn(self.gear.gear_set, list(SETS.keys()))
            self.assertEqual(self.gear.gear_level, 85, "gear level should be 85")
            self.assertEqual(self.gear.gear_tier, 6, "gear tier should be 6")
            self.assertIsNone(self.gear.mainstat)
            self.assertIsNone(self.gear.substats)
            self.assertIsNone(self.gear.mainstat_id)
            self.assertEqual(self.gear.substat_ids, [])

            
        missing_types = expected_gear_types_list - picked_gear_types 
        extra_types = picked_gear_types - expected_gear_types_list
        
        self.assertFalse(missing_types, f"The following values were not selected: {missing_types}")
        self.assertFalse(extra_types, f"The following extra values were selected: {extra_types}")
        
        missing_grades = expected_gear_grades_list - picked_gear_grades 
        extra_grades = picked_gear_grades - expected_gear_grades_list
        
        self.assertFalse(missing_grades, f"The following values were not selected: {missing_grades}")
        self.assertFalse(extra_grades, f"The following extra values were selected: {extra_grades}")
        

        
    def test_create_gear_specify_1(self):
        """
        Tests whether the initial values of the attributes are as we expect when we use 
        create_gear() method with specified gear_type. We should get same gear_type back
        and one of the random gear_grades.
        """
        input_gear_types_list = list(TYPES.keys())
        
        for j in list(input_gear_types_list):
            
            input_gear_type = j
            
            expected_gear_types_set = set([input_gear_type])
            expected_gear_grades_set = set(['rare', 'heroic', 'epic'])
            
            picked_gear_types = set()
            picked_gear_grades = set()
            
            for i in range(1000):
                
                self.gear.create_gear(gear_type=input_gear_type)

                gear_type = self.gear.gear_type
                gear_grade = self.gear.gear_grade

                picked_gear_types.add(gear_type)
                picked_gear_grades.add(gear_grade)
                
                expected_gear_types = list(expected_gear_types_set)
                expected_gear_grades = list(expected_gear_grades_set)

                self.assertIn(gear_type, expected_gear_types)
                self.assertIn(gear_grade, expected_gear_grades)
                
                self.assertIn(self.gear.gear_set, list(SETS.keys()))
                self.assertEqual(self.gear.gear_level, 85, "gear level should be 85")
                self.assertEqual(self.gear.gear_tier, 6, "gear tier should be 6")
                self.assertIsNone(self.gear.mainstat)
                self.assertIsNone(self.gear.substats)
                self.assertIsNone(self.gear.mainstat_id)
                self.assertEqual(self.gear.substat_ids, [])
                
            missing_types = expected_gear_types_set - picked_gear_types 
            extra_types = picked_gear_types - expected_gear_types_set

            self.assertFalse(missing_types, f"The following values were not selected: {missing_types}")
            self.assertFalse(extra_types, f"The following extra values were selected: {extra_types}")

            missing_grades = expected_gear_grades_set - picked_gear_grades 
            extra_grades = picked_gear_grades - expected_gear_grades_set

            self.assertFalse(missing_grades, f"The following values were not selected: {missing_grades}")
            self.assertFalse(extra_grades, f"The following extra values were selected: {extra_grades}")
        
        
    def test_create_gear_specify_2(self):
        """
        Tests whether the initial values of the attributes are as we expect when we use 
        create_gear() method with specified gear_type and gear_set. We should get same gear_type and gear_set
        back and one of the random gear_grades.
        """
        input_gear_types_list = list(TYPES.keys())
        input_gear_sets_list = list(SETS.keys())
        
        for j in input_gear_types_list:
            for s in input_gear_sets_list:
            
                input_gear_type = j
                input_gear_set = s

                expected_gear_types_set = set([input_gear_type])
                expected_gear_grades_set = set(['rare', 'heroic', 'epic'])
                expected_gear_sets_set = set([input_gear_set])

                picked_gear_types = set()
                picked_gear_grades = set()
                picked_gear_sets = set()

                for i in range(1000):

                    self.gear.create_gear(gear_type=input_gear_type, gear_set=input_gear_set)

                    gear_type = self.gear.gear_type
                    gear_grade = self.gear.gear_grade
                    gear_set = self.gear.gear_set

                    picked_gear_types.add(gear_type)
                    picked_gear_grades.add(gear_grade)
                    picked_gear_sets.add(gear_set)

                    expected_gear_types = list(expected_gear_types_set)
                    expected_gear_grades = list(expected_gear_grades_set)
                    expected_gear_sets = list(expected_gear_sets_set)

                    self.assertIn(gear_type, expected_gear_types)
                    self.assertIn(gear_grade, expected_gear_grades)
                    self.assertIn(gear_set, expected_gear_sets)
                    
                    self.assertEqual(self.gear.gear_level, 85, "gear level should be 85")
                    self.assertEqual(self.gear.gear_tier, 6, "gear tier should be 6")
                    self.assertIsNone(self.gear.mainstat)
                    self.assertIsNone(self.gear.substats)
                    self.assertIsNone(self.gear.mainstat_id)
                    self.assertEqual(self.gear.substat_ids, [])

                missing_types = expected_gear_types_set - picked_gear_types 
                extra_types = picked_gear_types - expected_gear_types_set
                self.assertFalse(missing_types, f"The following values were not selected: {missing_types}")
                self.assertFalse(extra_types, f"The following extra values were selected: {extra_types}")

                missing_grades = expected_gear_grades_set - picked_gear_grades 
                extra_grades = picked_gear_grades - expected_gear_grades_set
                self.assertFalse(missing_grades, f"The following values were not selected: {missing_grades}")
                self.assertFalse(extra_grades, f"The following extra values were selected: {extra_grades}")
                
                missing_sets = expected_gear_sets_set - picked_gear_sets
                extra_gsets = picked_gear_sets - expected_gear_sets_set
                self.assertFalse(missing_sets, f"The following values were not selected: {missing_sets}")
                self.assertFalse(extra_gsets, f"The following extra values were selected: {extra_gsets}")        

        
    def test_create_gear_specify_3(self):
        """
        Tests whether the initial values of the attributes are as we expect when we use 
        create_gear() method with specified gear_type, gear_set, gear_level. We should get same gear_type, gear_set, 
        gear_level (along with appropriate tier) and one of the random gear_grades as output.
        """
        input_gear_types_list = list(TYPES.keys())
        input_gear_sets_list = ['speed', 'health', 'critical', 'immunity']
        input_gear_level_list = [70, None, 85, 88, 90]
        
        expected_gear_level_list = [70, 85, 85, 88, 90]
        exepected_gear_tier_list = [5, 6, 6, 7, 7]
        
        for j in input_gear_types_list:
            for s in input_gear_sets_list:
                for l, val in enumerate(input_gear_level_list):
            
                    input_gear_type = j
                    input_gear_set = s
                    input_gear_level = val

                    expected_gear_types_set = set([input_gear_type])
                    expected_gear_grades_set = set(['rare', 'heroic', 'epic'])

                    picked_gear_types = set()
                    picked_gear_grades = set()

                    for i in range(1000):

                        self.gear.create_gear(gear_type=input_gear_type, gear_set=input_gear_set, gear_level=input_gear_level)

                        gear_type = self.gear.gear_type
                        gear_grade = self.gear.gear_grade
                        gear_set = self.gear.gear_set
                        gear_level = self.gear.gear_level
                        gear_tier = self.gear.gear_tier

                        picked_gear_types.add(gear_type)
                        picked_gear_grades.add(gear_grade)

                        expected_gear_types = list(expected_gear_types_set)
                        expected_gear_grades = list(expected_gear_grades_set)
                        expected_gear_set = input_gear_set
                        expected_gear_level = expected_gear_level_list[l]
                        expected_gear_tier = exepected_gear_tier_list[l]

                        self.assertIn(gear_type, expected_gear_types)
                        self.assertIn(gear_grade, expected_gear_grades)
                        self.assertEqual(gear_set, expected_gear_set)
                        self.assertEqual(gear_level, expected_gear_level)
                        self.assertEqual(gear_tier, expected_gear_tier)
                        
                        self.assertIsNone(self.gear.mainstat)
                        self.assertIsNone(self.gear.substats)
                        self.assertIsNone(self.gear.mainstat_id)
                        self.assertEqual(self.gear.substat_ids, [])

                    missing_types = expected_gear_types_set - picked_gear_types 
                    extra_types = picked_gear_types - expected_gear_types_set
                    self.assertFalse(missing_types, f"The following values were not selected: {missing_types}")
                    self.assertFalse(extra_types, f"The following extra values were selected: {extra_types}")

                    missing_grades = expected_gear_grades_set - picked_gear_grades 
                    extra_grades = picked_gear_grades - expected_gear_grades_set
                    self.assertFalse(missing_grades, f"The following values were not selected: {missing_grades}")
                    self.assertFalse(extra_grades, f"The following extra values were selected: {extra_grades}")

                    
    def test_create_gear_specify_4(self):
        """
        Tests whether the initial values of the attributes are as we expect when we use 
        create_gear() method with specified gear_type, gear_set, gear_level, gear_grade. 
        We should get same gear_type, gear_set, gear_level (along with appropriate tier) 
        and gear_grade as output.
        """
        input_gear_types_list = list(TYPES.keys())
        input_gear_sets_list = ['speed', 'health', 'critical', 'immunity']
        input_gear_grades_list = ['rare', 'heroic', 'epic']
        input_gear_level_list = [70, None, 85, 88, 90]
        
        expected_gear_level_list = [70, 85, 85, 88, 90]
        exepected_gear_tier_list = [5, 6, 6, 7, 7]
        
        for j in input_gear_types_list:
            for s in input_gear_sets_list:
                for l, val in enumerate(input_gear_level_list):
                    for g in input_gear_grades_list:
            
                        input_gear_type = j
                        input_gear_set = s
                        input_gear_level = val
                        input_gear_grade = g

                        expected_gear_types_set = set([input_gear_type])

                        picked_gear_types = set()

                        for i in range(1000):

                            self.gear.create_gear(gear_type=input_gear_type, 
                                                  gear_set=input_gear_set, 
                                                  gear_level=input_gear_level,
                                                  gear_grade=input_gear_grade)

                            gear_type = self.gear.gear_type
                            gear_grade = self.gear.gear_grade
                            gear_set = self.gear.gear_set
                            gear_level = self.gear.gear_level
                            gear_tier = self.gear.gear_tier

                            picked_gear_types.add(gear_type)

                            expected_gear_types = list(expected_gear_types_set)
                            expected_gear_grade = input_gear_grade
                            expected_gear_set = input_gear_set
                            expected_gear_level = expected_gear_level_list[l]
                            expected_gear_tier = exepected_gear_tier_list[l]

                            self.assertIn(gear_type, expected_gear_types)
                            self.assertEqual(gear_grade, expected_gear_grade)
                            self.assertEqual(gear_set, expected_gear_set)
                            self.assertEqual(gear_level, expected_gear_level)
                            self.assertEqual(gear_tier, expected_gear_tier)

                            self.assertIsNone(self.gear.mainstat)
                            self.assertIsNone(self.gear.substats)
                            self.assertIsNone(self.gear.mainstat_id)
                            self.assertEqual(self.gear.substat_ids, [])

                        missing_types = expected_gear_types_set - picked_gear_types 
                        extra_types = picked_gear_types - expected_gear_types_set
                        self.assertFalse(missing_types, f"The following values were not selected: {missing_types}")
                        self.assertFalse(extra_types, f"The following extra values were selected: {extra_types}")

                        
    def test_create_gear_specify_mainstat(self):
        """
        Tests whether the initial values of the attributes are as we expect when we use 
        create_gear() method with specified mainstat_id, gear_set, gear_level, and gear_grade.
        We should get a random gear based on the mainstat provided.
        """
        mainstat_id_list = [0, 2, 4, 10, 6, 7, 8, 9, 1, 3, 5]
        expect_gear_types_list = [
            ['weapon', 'necklace', 'ring', 'boots'],
            ['helm', 'necklace', 'ring', 'boots'],
            ['armor', 'necklace', 'ring', 'boots'],
            ['boots'],
            ['necklace'],
            ['necklace'],
            ['ring'],
            ['ring'],
            ['necklace', 'ring', 'boots'],
            ['necklace', 'ring', 'boots'],
            ['necklace', 'ring', 'boots']
            ]                
        input_gear_sets_list = ['speed', 'health', 'destruction']
        input_gear_level_list = [70, 85, None, 86, 90]
        expected_gear_level_list = [70, 85, 85, 86, 90]
        expected_gear_tier_list = [5, 6, 6, 7, 7]
        input_gear_grade_list = ['rare', 'heroic', 'epic']
        
        for ind_m, j in enumerate(mainstat_id_list):
            for s in input_gear_sets_list:
                for ind, lvl in enumerate(input_gear_level_list):
                    for g in input_gear_grade_list:
                        
                        input_lvl = lvl
                        expected_lvl = expected_gear_level_list[ind]
                        expected_tier = expected_gear_tier_list[ind]
                        input_gear_set = s
                        input_gear_grade = g

                        expected_gear_types_set = set(expect_gear_types_list[ind_m])
                        picked_gear_types = set()


                        for i in range(100):
                            self.gear.create_gear(gear_set=s, gear_level=input_lvl, gear_grade=g, mainstat_id=j)

                            gear_type = self.gear.gear_type
                            picked_gear_types.add(gear_type)
                            expected_gear_types = list(expected_gear_types_set)
                            self.assertIn(gear_type, expected_gear_types)

                            self.assertEqual(self.gear.gear_set, s)
                            self.assertEqual(self.gear.gear_level, expected_lvl, f"gear level should be {expected_lvl}")
                            self.assertEqual(self.gear.gear_tier, expected_tier, f"gear tier should be {expected_tier}")
                            self.assertEqual(self.gear.gear_grade, g, f"gear grade should be {g}")
                            self.assertIsNone(self.gear.mainstat)
                            self.assertIsNone(self.gear.substats)
                            self.assertEqual(self.gear.mainstat_id, str(j))
                            self.assertEqual(self.gear.substat_ids, [])

                        missing = expected_gear_types_set - picked_gear_types 
                        extra = picked_gear_types - expected_gear_types_set

                        self.assertFalse(missing, f"The following values were not selected: {missing}")
                        self.assertFalse(extra, f"The following extra values were selected: {extra}")  
                        
                        
    def test_create_gear_specify_values(self):
        """
        Tests whether the initial values of the attributes are as we expect when we use 
        create_gear() method with specified mainstat_id, substat_id, gear_set, gear_level.
        We should get an appropriate random gear based on the mainstat and substats provided.
        The gear_grade should reflect the number of substats provided.
        """
        expected_gear_types_list = [['boots'], 
                                    ['ring'],
                                    ['necklace'], 
                                    ['helm', 'ring', 'necklace', 'boots'],
                                    ['ring', 'necklace', 'boots'],
                                    ['ring', 'necklace', 'boots']
                                    ]
        expected_gear_grades_list = [
            ['rare', 'heroic', 'epic'],
            ['rare', 'heroic', 'epic'],
            ['epic'],
            ['epic'],
            ['rare', 'heroic', 'epic'],
            ['heroic', 'epic'],
        ]
        mainstat_id_list = [10, 8, 6, 2, 3, 1]
        substat_id_list = [0, 
                           [0], 
                           [10, 3, 4, 1], 
                           [10, 0, 7, 8], 
                           [1, 2], 
                           [0, 3, 5]
                          ]
        input_gear_sets_list = ['speed', 'health', 'destruction']
        input_gear_level_list = [70, 85, None, 86, 90]
        expected_gear_level_list = [70, 85, 85, 86, 90]
        expected_gear_tier_list = [5, 6, 6, 7, 7]
        
        for ind_m, j in enumerate(mainstat_id_list):
            for s in input_gear_sets_list:
                for ind, lvl in enumerate(input_gear_level_list):
                        
                    input_lvl = lvl
                    expected_lvl = expected_gear_level_list[ind]
                    expected_tier = expected_gear_tier_list[ind]
                    expected_grade = expected_gear_grades_list[ind_m]
                    input_gear_set = s
                    input_substat_ids = convert_int_to_str(substat_id_list[ind_m])

                    expected_gear_types_set = set(expected_gear_types_list[ind_m])
                    picked_gear_types = set()
                    
                    with self.subTest(set_=s, lvl_=input_lvl, main_=j, sub_=input_substat_ids):
                        for i in range(100):
                            self.gear.create_gear(gear_set=s, gear_level=input_lvl, 
                                                  mainstat_id=j, substat_ids=input_substat_ids)

                            gear_type = self.gear.gear_type
                            picked_gear_types.add(gear_type)
                            expected_gear_types = list(expected_gear_types_set)
                            self.assertIn(gear_type, expected_gear_types)
                            self.assertEqual(self.gear.gear_set, s)
                            self.assertEqual(self.gear.gear_level, expected_lvl, f"gear level should be {expected_lvl}")
                            self.assertEqual(self.gear.gear_tier, expected_tier, f"gear tier should be {expected_tier}")
                            self.assertIn(self.gear.gear_grade, expected_grade, f"gear grade should be in  {expected_grade}")
                            self.assertIsNone(self.gear.mainstat)
                            self.assertIsNone(self.gear.substats)
                            self.assertEqual(self.gear.mainstat_id, str(j))
                            self.assertEqual(self.gear.substat_ids, input_substat_ids)

                        missing = expected_gear_types_set - picked_gear_types 
                        extra = picked_gear_types - expected_gear_types_set

                        self.assertFalse(missing, f"The following values were not selected: {missing}")
                        self.assertFalse(extra, f"The following extra values were selected: {extra}")  
                        
                        
    def test_create_gear_specify_values_subs_no_main(self):
        """
        Tests whether the attributes are as we expect when we use 
        create_gear() method with specified substat_id, gear_set, gear_level.
        We should get an appropriate random gear type based on the substats provided.
        The gear_grade should reflect the number of substats provided.
        """
        expected_gear_types_list = [['boots', 'necklace', 'ring', 'helm'], 
                                    ['boots', 'necklace', 'ring', 'helm'],
                                    ['necklace', 'helm', 'ring', 'boots'],
                                    ['helm', 'ring', 'necklace', 'boots'],
                                    ['weapon', 'ring', 'necklace', 'boots'],
                                    ['helm', 'ring', 'necklace', 'boots']
                                    ]
        expected_gear_grades_list = [
            ['rare', 'heroic', 'epic'],
            ['rare', 'heroic', 'epic'],
            ['epic'],
            ['epic'],
            ['rare', 'heroic', 'epic'],
            ['heroic', 'epic'],
        ]
        substat_id_list = [0, 
                           [0], 
                           [10, 3, 4, 1], 
                           [10, 0, 7, 8], 
                           [1, 2], 
                           [0, 3, 5]
                          ]
        input_gear_sets_list = ['speed', 'health', 'destruction']
        input_gear_level_list = [70, 85, None, 86, 90]
        expected_gear_level_list = [70, 85, 85, 86, 90]
        expected_gear_tier_list = [5, 6, 6, 7, 7]
        
        for ind_m, j in enumerate(substat_id_list):
            for s in input_gear_sets_list:
                for ind, lvl in enumerate(input_gear_level_list):
                        
                    input_lvl = lvl
                    expected_lvl = expected_gear_level_list[ind]
                    expected_tier = expected_gear_tier_list[ind]
                    expected_grade = expected_gear_grades_list[ind_m]
                    input_gear_set = s
                    input_substat_ids = convert_int_to_str(substat_id_list[ind_m])

                    expected_gear_types_set = set(expected_gear_types_list[ind_m])
                    picked_gear_types = set()
                    
                    with self.subTest(set_=s, lvl_=input_lvl, main_=j, sub_=input_substat_ids):
                        for i in range(100):
                            self.gear.create_gear(gear_set=s, gear_level=input_lvl, 
                                                  substat_ids=input_substat_ids)

                            gear_type = self.gear.gear_type
                            picked_gear_types.add(gear_type)
                            expected_gear_types = list(expected_gear_types_set)
                            self.assertIn(gear_type, expected_gear_types)
                            self.assertEqual(self.gear.gear_set, s)
                            self.assertEqual(self.gear.gear_level, expected_lvl, f"gear level should be {expected_lvl}")
                            self.assertEqual(self.gear.gear_tier, expected_tier, f"gear tier should be {expected_tier}")
                            self.assertIn(self.gear.gear_grade, expected_grade, f"gear grade should be in  {expected_grade}")
                            self.assertIsNone(self.gear.mainstat)
                            self.assertIsNone(self.gear.substats)
                            self.assertIsNone(self.gear.mainstat_id)
                            self.assertEqual(self.gear.substat_ids, input_substat_ids)

                        missing = expected_gear_types_set - picked_gear_types 
                        extra = picked_gear_types - expected_gear_types_set

                        self.assertFalse(missing, f"The following values were not selected: {missing}")
                        self.assertFalse(extra, f"The following extra values were selected: {extra}") 
                        
                        
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
            
if __name__ == "__main__":
    unittest.main()