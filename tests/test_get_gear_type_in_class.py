# Add parent directory to path
from set_directory_function import set_directory
set_directory()

# Imports
import unittest
import json
import random
from tests.test_class_gear_v1 import Gear 
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
        create_gear() method. As no args are provided, gear_type should be completely random 
        and we expect to see every gear_type picked at least once.
        """
        expected_gear_types_list = set(list(TYPES.keys()))
        picked_gear_types = set()
        
        for i in range(1000):
            self.gear.create_gear()
            
            gear_type = self.gear.gear_type
            picked_gear_types.add(gear_type)
            expected_gear_types = list(expected_gear_types_list)
            self.assertIn(gear_type, expected_gear_types)
            
            self.assertIn(self.gear.gear_set, list(SETS.keys()))
            self.assertEqual(self.gear.gear_level, 85, "gear level should be 85")
            self.assertEqual(self.gear.gear_tier, 6, "gear tier should be 6")
            self.assertIsNone(self.gear.gear_grade)
            self.assertIsNone(self.gear.mainstat)
            self.assertIsNone(self.gear.substats)
            self.assertIsNone(self.gear.mainstat_id)
            self.assertIsNone(self.gear.substat_ids)

            
        missing = expected_gear_types_list - picked_gear_types 
        extra = picked_gear_types - expected_gear_types_list
        
        self.assertFalse(missing, f"The following values were not selected: {missing}")
        self.assertFalse(extra, f"The following extra values were selected: {extra}")

        
    def test_create_gear_specify_1(self):
        """
        Tests whether the initial values of the attributes are as we expect when we use 
        create_gear() method with specified gear_type
        """
        input_gear_types_list = list(TYPES.keys())
        
        for j in input_gear_types_list:
            
            expected_gear_types_list = set([j])
            picked_gear_types = set()

            for i in range(1000):
                self.gear.create_gear(gear_type=j)

                gear_type = self.gear.gear_type
                picked_gear_types.add(gear_type)
                expected_gear_types = list(expected_gear_types_list)
                self.assertIn(gear_type, expected_gear_types)

                self.assertIn(self.gear.gear_set, list(SETS.keys()))
                self.assertEqual(self.gear.gear_level, 85, "gear level should be 85")
                self.assertEqual(self.gear.gear_tier, 6, "gear tier should be 6")
                self.assertIsNone(self.gear.gear_grade)
                self.assertIsNone(self.gear.mainstat)
                self.assertIsNone(self.gear.substats)
                self.assertIsNone(self.gear.mainstat_id)
                self.assertIsNone(self.gear.substat_ids)
                
            missing = expected_gear_types_list - picked_gear_types 
            extra = picked_gear_types - expected_gear_types_list

            self.assertFalse(missing, f"The following values were not selected: {missing}")
            self.assertFalse(extra, f"The following extra values were selected: {extra}")
        
        
    def test_create_gear_specify_2(self):
        """
        Tests whether the initial values of the attributes are as we expect when we use 
        create_gear() method with specified gear_type and gear_set
        """
        input_gear_types_list = list(TYPES.keys())
        input_gear_sets_list = ['speed', 'health', 'destruction']
        
        for j in input_gear_types_list:
            for s in input_gear_sets_list:
                expected_gear_types_list = set([j])
                picked_gear_types = set()
                input_gear_set = s

                for i in range(100):
                    self.gear.create_gear(gear_type=j, gear_set=s)

                    gear_type = self.gear.gear_type
                    picked_gear_types.add(gear_type)
                    expected_gear_types = list(expected_gear_types_list)
                    self.assertIn(gear_type, expected_gear_types)

                    self.assertEqual(self.gear.gear_set, s)
                    self.assertEqual(self.gear.gear_level, 85, "gear level should be 85")
                    self.assertEqual(self.gear.gear_tier, 6, "gear tier should be 6")
                    self.assertIsNone(self.gear.gear_grade)
                    self.assertIsNone(self.gear.mainstat)
                    self.assertIsNone(self.gear.substats)
                    self.assertIsNone(self.gear.mainstat_id)
                    self.assertIsNone(self.gear.substat_ids)

                missing = expected_gear_types_list - picked_gear_types 
                extra = picked_gear_types - expected_gear_types_list

                self.assertFalse(missing, f"The following values were not selected: {missing}")
                self.assertFalse(extra, f"The following extra values were selected: {extra}")     
            
            
    def test_create_gear_specify_3(self):
        """
        Tests whether the initial values of the attributes are as we expect when we use 
        create_gear() method with specified gear_type, gear_set, and gear_level
        """
        input_gear_types_list = list(TYPES.keys())
        input_gear_sets_list = ['speed', 'health', 'destruction']
        input_gear_level_list = [70, 85, None, 86, 90]
        expected_gear_level_list = [70, 85, 85, 86, 90]
        expected_gear_tier_list = [5, 6, 6, 7, 7]
        
        for j in input_gear_types_list:
            for s in input_gear_sets_list:
                for ind, lvl in enumerate(input_gear_level_list):
                    
                    input_lvl = lvl
                    expected_lvl = expected_gear_level_list[ind]
                    expected_tier = expected_gear_tier_list[ind]
                    input_gear_set = s
                    
                    expected_gear_types_list = set([j])
                    picked_gear_types = set()
                    

                    for i in range(100):
                        self.gear.create_gear(gear_type=j, gear_set=s, gear_level=input_lvl)

                        gear_type = self.gear.gear_type
                        picked_gear_types.add(gear_type)
                        expected_gear_types = list(expected_gear_types_list)
                        self.assertIn(gear_type, expected_gear_types)

                        self.assertEqual(self.gear.gear_set, s)
                        self.assertEqual(self.gear.gear_level, expected_lvl, f"gear level should be {expected_lvl}")
                        self.assertEqual(self.gear.gear_tier, expected_tier, f"gear tier should be {expected_tier}")
                        self.assertIsNone(self.gear.gear_grade)
                        self.assertIsNone(self.gear.mainstat)
                        self.assertIsNone(self.gear.substats)
                        self.assertIsNone(self.gear.mainstat_id)
                        self.assertIsNone(self.gear.substat_ids)

                    missing = expected_gear_types_list - picked_gear_types 
                    extra = picked_gear_types - expected_gear_types_list

                    self.assertFalse(missing, f"The following values were not selected: {missing}")
                    self.assertFalse(extra, f"The following extra values were selected: {extra}")     
            
            
    def test_create_gear_specify_4(self):
        """
        Tests whether the initial values of the attributes are as we expect when we use 
        create_gear() method with specified gear_type, gear_set, gear_level, and gear_grade
        """
        input_gear_types_list = list(TYPES.keys())
        input_gear_sets_list = ['speed', 'health', 'destruction']
        input_gear_level_list = [70, 85, None, 86, 90]
        expected_gear_level_list = [70, 85, 85, 86, 90]
        expected_gear_tier_list = [5, 6, 6, 7, 7]
        input_gear_grade_list = ['rare', 'heroic', 'epic']
        
        for j in input_gear_types_list:
            for s in input_gear_sets_list:
                for ind, lvl in enumerate(input_gear_level_list):
                    for g in input_gear_grade_list:
                        
                        input_lvl = lvl
                        expected_lvl = expected_gear_level_list[ind]
                        expected_tier = expected_gear_tier_list[ind]
                        input_gear_set = s
                        input_gear_grade = g

                        expected_gear_types_list = set([j])
                        picked_gear_types = set()


                        for i in range(100):
                            self.gear.create_gear(gear_type=j, gear_set=s, gear_level=input_lvl, gear_grade=g)

                            gear_type = self.gear.gear_type
                            picked_gear_types.add(gear_type)
                            expected_gear_types = list(expected_gear_types_list)
                            self.assertIn(gear_type, expected_gear_types)

                            self.assertEqual(self.gear.gear_set, s)
                            self.assertEqual(self.gear.gear_level, expected_lvl, f"gear level should be {expected_lvl}")
                            self.assertEqual(self.gear.gear_tier, expected_tier, f"gear tier should be {expected_tier}")
                            self.assertEqual(self.gear.gear_grade, g, f"gear grade should be {g}")
                            self.assertIsNone(self.gear.mainstat)
                            self.assertIsNone(self.gear.substats)
                            self.assertIsNone(self.gear.mainstat_id)
                            self.assertIsNone(self.gear.substat_ids)

                        missing = expected_gear_types_list - picked_gear_types 
                        extra = picked_gear_types - expected_gear_types_list

                        self.assertFalse(missing, f"The following values were not selected: {missing}")
                        self.assertFalse(extra, f"The following extra values were selected: {extra}")  
                        
                        
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
                            self.assertIsNone(self.gear.substat_ids)

                        missing = expected_gear_types_set - picked_gear_types 
                        extra = picked_gear_types - expected_gear_types_set

                        self.assertFalse(missing, f"The following values were not selected: {missing}")
                        self.assertFalse(extra, f"The following extra values were selected: {extra}")  
                        
                        
    def test_create_gear_specify_values(self):
        """
        Tests whether the initial values of the attributes are as we expect when we use 
        create_gear() method with specified mainstat_id, substat_id, gear_set, gear_level, and gear_grade.
        We should get an appropriate random gear based on the mainstat and substats provided.
        """
        expected_gear_types_list = [['boots'], 
                                    ['ring'],
                                    ['necklace'], 
                                    ['helm', 'ring', 'necklace', 'boots'],
                                    ['ring', 'necklace', 'boots'],
                                    ['ring', 'necklace', 'boots']
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
                        input_substat_ids = convert_int_to_str(substat_id_list[ind_m])

                        expected_gear_types_set = set(expected_gear_types_list[ind_m])
                        picked_gear_types = set()


                        for i in range(100):
                            self.gear.create_gear(gear_set=s, gear_level=input_lvl, gear_grade=g, 
                                                  mainstat_id=j, substat_ids=input_substat_ids)

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
        Tests whether we get ValueError when we there aer duplicates in substats
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
            
            
if __name__ == "__main__":
    unittest.main()