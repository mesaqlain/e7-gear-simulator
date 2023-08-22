from set_directory_function import set_directory
set_directory()

import random
import json
import unittest
from tests.test_functions import test_get_gear_type
from src.utilities import get_random_gear_type

with open('data/types.json', 'r') as types_file:
    TYPES = json.load(types_file)


class TestGetGearType(unittest.TestCase):
    
    def test_get_gear_type_default(self):
        """
        Test whether we get a completely random gear if no args are provided.
        """
        expect_gear_types = set(TYPES.keys())
        picked_gear_types = set()
        
        for i in range(10000):
            gear_type = test_get_gear_type()
            picked_gear_types.add(gear_type)
            self.assertIn(gear_type, list(expect_gear_types), f"{gear_type} is not in expect_gear_types")
        
        missing = expect_gear_types - picked_gear_types 
        extra = picked_gear_types - expect_gear_types
        
        self.assertFalse(missing, f"The following values were not selected: {missing}")
        self.assertFalse(extra, f"The following extra values were selected: {extra}")

        
    def test_get_gear_type_input_mainstat(self):
        """
        Test whether we get an appropriate random gear if no args are provided.
        """
        mainstat_id_list = [0, 2, 4, 10, 6, 7, 8, 9, 1, 3, 5]
        expect_gear_types = [
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
        
        for i, val in enumerate(mainstat_id_list):
            with self.subTest(mainstat_id=val, gear_type=expect_gear_types[i]):
                picked_gear_types = set()
                expected_gear_types = set(expect_gear_types[i])

                for j in range(10000):
                    input_mainstat_id = val
                    gear_type = test_get_gear_type(mainstat_id=input_mainstat_id)
                    picked_gear_types.add(gear_type)
                    self.assertIn(gear_type, expected_gear_types, f"{gear_type} is not in {expected_gear_types}")

                missing = expected_gear_types - picked_gear_types 
                extra = picked_gear_types - expected_gear_types

                self.assertFalse(missing, f"The following values were not selected: {missing}")
                self.assertFalse(extra, f"The following extra values were selected: {extra}")
        
        
    def test_get_gear_type_input_gear_type(self):
        """
        Test whether we get the same gear type back if gear_type is provided but
        mainstat and substat ids are not.
        """
        expect_gear_types = set(TYPES.keys())
        picked_gear_types = set()
        
        for i in range(10000):
            input_gear = get_random_gear_type()
            gear_type = test_get_gear_type(gear_type=input_gear)
            picked_gear_types.add(gear_type)
            self.assertEqual(gear_type, input_gear, f"{gear_type} does not match input {input_gear}")
        
        missing = expect_gear_types - picked_gear_types 
        extra = picked_gear_types - expect_gear_types
        
        self.assertFalse(missing, f"The following values were not selected: {missing}")
        self.assertFalse(extra, f"The following extra values were selected: {extra}")
        
        
    def test_get_gear_type_input_mainstat_type(self):
        """
        Test whether we get an appropriate random gear if gear_type and correct mainstat are provided.
        """
        gear_type_list = ['ring', 'helm', 'boots', 'boots', 'necklace', 'necklace',
                         'ring', 'ring', 'boots', 'necklace', 'ring']
        mainstat_id_list = [0, 2, 4, 10, 6, 7, 8, 9, 1, 3, 5]
        expect_gear_types_list = gear_type_list
        
        for i, val in enumerate(mainstat_id_list):
            with self.subTest(mainstat_id=val, gear_type=expect_gear_types_list[i]):
                for j in range(10000):
                    input_mainstat_id = val
                    gear_type = test_get_gear_type(gear_type=gear_type_list[i], mainstat_id=input_mainstat_id)
                    expected_gear_type = expect_gear_types_list[i]
                    self.assertEqual(gear_type, expected_gear_type, f"{gear_type} is not in {expected_gear_type}")
                    
                    
    def test_get_gear_type_input_substats_type(self):
        """
        Test whether we get an appropriate random gear if gear_type and correct substats are provided.
        """
        gear_type_list = ['ring', 'helm', 'boots', 'boots', 'necklace', 'necklace',
                         'ring', 'ring', 'boots', 'necklace', 'ring']
        substat_id_list = [0, 
                           [0], 
                           [10, 3, 4, 1], 
                           [10, 1, 0, 4], 
                           [1, 2], 
                           [0, 3, 5], 
                           [1, 2, 3], 
                           [5, 6, 7, 8], 
                           [10, 1, 3], 
                           [2, 0, 5], 
                           5]
        expect_gear_types_list = gear_type_list
        
        for i, val in enumerate(substat_id_list):
            with self.subTest(substat_ids=val, gear_type=expect_gear_types_list[i]):
                for j in range(100):
                    input_substat_ids = val
                    gear_type = test_get_gear_type(gear_type=gear_type_list[i], substat_ids=input_substat_ids)
                    expected_gear_type = expect_gear_types_list[i]
                    self.assertEqual(gear_type, expected_gear_type, f"{gear_type} is not in {expected_gear_type}")
        
        
    def test_get_gear_type_invalid_mainstats(self):
        """
        Test whether we get a Value Error when we pick incorrect gear_type with mainstats.
        """
        gear_type_list = ['weapon', 'weapon', 'weapon', 
                          'helm', 'helm', 'helm',
                          'armor', 'armor', 'armor',
                          'necklace', 'necklace', 'necklace',
                          'ring', 'ring', 'ring',
                          'boots', 'boots', 'boots', 'boots']
        mainstat_id_list = [1, 5, 6,
                           5, 8, 10,
                           0, 1, 9,
                           8, 9, 10,
                           6, 7, 10,
                           6, 7, 8, 9]
        
        for i, val in enumerate(gear_type_list):
            with self.subTest(gear_type = val):
                with self.assertRaises(ValueError):
                    test_get_gear_type(gear_type=val, mainstat_id=mainstat_id_list[i])
        
        
    def test_get_gear_type_invalid_mainstats_2(self):
        """
        Test whether we get a Value Error when we pick incorrect gear_type with mainstats,
        even if the substats are correct.
        """
        gear_type_list = ['weapon', 'weapon', 'weapon', 
                          'helm', 'helm', 'helm',
                          'armor', 'armor', 'armor',
                          'necklace', 'necklace', 'necklace',
                          'ring', 'ring', 'ring',
                          'boots', 'boots', 'boots', 'boots']
        mainstat_id_list = [1, 5, 6,
                           5, 8, 10,
                           0, 1, 9,
                           8, 9, 10,
                           6, 7, 10,
                           6, 7, 8, 9]
        substat_id_list = [1, [5], [10, 2],
                           [5], [8, 9, 10], [6, 7, 8, 10],
                           [5, 6, 8], [3, 5], [3, 5, 10, 9],
                           [8, 5, 10], [3, 5, 10], 10,
                           [6, 3, 2, 0], [7, 3, 4, 1], [10, 2],
                           6, 7, 8, 9]
        
        for i, val in enumerate(gear_type_list):
            with self.subTest(gear_type = val):
                with self.assertRaises(ValueError):
                    test_get_gear_type(gear_type=val, mainstat_id=mainstat_id_list[i])

                    
    def test_get_gear_type_invalid_substats(self):
        """
        Test whether we get a Value Error when we pick incorrect gear_type with substats
        """
        gear_type_list = ['weapon', 'weapon', 'weapon', 'weapon',
                          'helm', 'helm', 'helm',
                          'armor', 'armor', 'armor']
        substat_id_list = [0, [0, 4, 5], [10, 4, 9, 8], [10, 0, 5, 6],
                           [2], [2, 3, 5, 10], [1, 7, 8, 2],
                           [0, 1, 4], [10, 0, 3], [6, 7, 3, 4]]    
        mainstat_id_list = [0, 0, 0, 0,
                           2, 2, 2,
                           4, 4, 4]
        for i, val in enumerate(gear_type_list):
            with self.subTest(gear_type = val, mainstat=mainstat_id_list[i], substats=substat_id_list[i]):
                with self.assertRaises(ValueError):
                    test_get_gear_type(gear_type=val, mainstat_id=mainstat_id_list[i], substat_ids=substat_id_list[i])
                    
             
    def test_get_gear_type_invalid_substats_2(self):
        """
        Test whether we get a Value Error when we pick incorrect gear_type with substats,
        even if the mainstats are correct.
        """
        gear_type_list = ['weapon', 'weapon', 'weapon', 'weapon',
                          'helm', 'helm', 'helm',
                          'armor', 'armor', 'armor']
        substat_id_list = [0, [0, 4, 5], [10, 4, 9, 8], [10, 0, 5, 6],
                           [2], [2, 3, 5, 10], [1, 7, 8, 2],
                           [0, 1, 4], [10, 0, 3], [6, 7, 3, 4]]        
        for i, val in enumerate(gear_type_list):
            with self.subTest(gear_type = val, substats=substat_id_list[i]):
                with self.assertRaises(ValueError):
                    test_get_gear_type(gear_type=val, substat_ids=substat_id_list[i])

                    
    def test_get_gear_type_invalid_duplicate_subs(self):
        """
        Test whether we get a Value Error when we pick duplicate subs
        """
        substat_id_list = [[0, 0], 
                           [0, 4, 4], 
                           [10, 4, 10, 4], 
                           [10, 0, 0, 0],
                           [3, 3, 1, 6],
                           [5, 5, 5]]
        for i, val in enumerate(substat_id_list):
            with self.subTest(substat_ids = val):
                with self.assertRaises(ValueError):
                    test_get_gear_type(substat_ids=val)
                    
                    
    def test_get_gear_type_invalid_duplicate_subs_2(self):
        """
        Test whether we get a Value Error when we pick duplicate subs 
        even if gear_type are correct:
        """
        gear_type_list = ['ring', 'boots', 'weapon', 'helm', 'necklace', 'weapon']
        substat_id_list = [[0, 0], 
                           [0, 4, 4], 
                           [10, 4, 10, 4], 
                           [10, 0, 0, 0],
                           [3, 3, 1, 6],
                           [5, 5, 5]]
        for i, val in enumerate(substat_id_list):
            with self.subTest(substat_ids = val):
                with self.assertRaises(ValueError):
                    test_get_gear_type(gear_type=gear_type_list[i], substat_ids=val)
                    
                    
    def test_get_gear_type_invalid_duplicate_subs_3(self):
        """
        Test whether we get a Value Error when we pick duplicate subs 
        even if gear_type and mainstatsare correct:
        """
        gear_type_list = ['ring', 'boots', 'weapon', 'helm', 'necklace', 'weapon']
        mainstat_id_list = [5, 10, 0, 2, 7, 0]
        substat_id_list = [[0, 0], 
                           [0, 4, 4], 
                           [10, 4, 10, 4], 
                           [10, 0, 0, 0],
                           [3, 3, 1, 6],
                           [5, 5, 5]]
        for i, val in enumerate(substat_id_list):
            with self.subTest(substat_ids = val):
                with self.assertRaises(ValueError):
                    test_get_gear_type(gear_type=gear_type_list[i], mainstat_id=mainstat_id_list[i], substat_ids=val)

    def test_get_gear_type_invalid_main_sub_clash(self):
        """
        Test whether we get a Value Error when we pick a sub 
        that is already in mainstat:
        """
        mainstat_id_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        substat_id_list = [[0, 0], 
                           [0, 4, 4], 
                           [10, 4, 10, 4], 
                           [10, 0, 0, 0],
                           [3, 3, 1, 6],
                           [5, 5, 5]]
        for i, val in enumerate(substat_id_list):
            with self.subTest(substat_ids = val):
                with self.assertRaises(ValueError):
                    test_get_gear_type(mainstat_id=mainstat_id_list[i], substat_ids=val)
                    
                    
    def test_get_gear_type_invalid_main_sub_clash_2(self):
        """
        Test whether we get a Value Error when we pick a sub 
        that is already in mainstat and gear_type is correct:
        """
        gear_type_list = ['weapon', 'ring', 'helm', 'necklace', 'armor', 'boots', 'necklace', 'necklace', 'ring', 'ring', 'boots']
        mainstat_id_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        substat_id_list = [[0, 0], 
                           [0, 4, 4], 
                           [10, 4, 10, 4], 
                           [10, 0, 0, 0],
                           [3, 3, 1, 6],
                           [5, 5, 5]]
        for i, val in enumerate(substat_id_list):
            with self.subTest(substat_ids = val):
                with self.assertRaises(ValueError):
                    test_get_gear_type(mainstat_id=mainstat_id_list[i], substat_ids=val)
                    
                    
                    
                    
if __name__ == "__main__":
    unittest.main()