from set_directory_function import set_directory
set_directory()

import unittest
import json
import random
from src.validation_utils import *
from src.utilities import *
from tests.test_functions import * 

STATS = json.loads(open('data/stats.json', 'r').read())

class TestGetModValue(unittest.TestCase):
    
    def test_get_mod_value_1(self):
        """
        Test whether we get appropriate mod_values when stat_id=0 and other args default
        """
        parsed_mod_vals = set()

        # Generate 1000 random stats for 'weapon' gear type
        for _ in range(10000):
            mod_val = test_get_mod_value(stat_id = 0)
            parsed_mod_vals.add(mod_val)  

        # Ensure only stat id 0 is selected
        expected_mod_vals = set(range(33, 48))
        missing_mod_vals = expected_mod_vals - parsed_mod_vals
        extra_mod_vals = parsed_mod_vals - expected_mod_vals

        self.assertFalse(missing_mod_vals, f"The following mod values were not selected: {missing_mod_vals}")
        self.assertFalse(extra_mod_vals, f"The following extra mod values were selected: {extra_mod_vals}")

    def test_get_mod_value_2(self):
        """
        Test whether we get appropriate mod_values when stat_id=0 and gear_level=85 and other args default
        """
        parsed_mod_vals = set()

        # Generate 1000 random stats for 'weapon' gear type
        for _ in range(10000):
            mod_val = test_get_mod_value(stat_id = 0, gear_level =85)
            parsed_mod_vals.add(mod_val)  

        # Ensure only stat id 0 is selected
        expected_mod_vals = set(range(33, 48))
        missing_mod_vals = expected_mod_vals - parsed_mod_vals
        extra_mod_vals = parsed_mod_vals - expected_mod_vals

        self.assertFalse(missing_mod_vals, f"The following mod values were not selected: {missing_mod_vals}")
        self.assertFalse(extra_mod_vals, f"The following extra mod values were selected: {extra_mod_vals}")
        
        
    def test_get_mod_value_3(self):
        """
        Test whether we get appropriate mod_values when stat_id=0, gear_level=85, rolled=0 and other args default
        """
        parsed_mod_vals = set()

        # Generate 1000 random stats for 'weapon' gear type
        for _ in range(10000):
            mod_val = test_get_mod_value(stat_id = 0, gear_level =85, rolled=0)
            parsed_mod_vals.add(mod_val)  

        # Ensure only stat id 0 is selected
        expected_mod_vals = set(range(33, 48))
        missing_mod_vals = expected_mod_vals - parsed_mod_vals
        extra_mod_vals = parsed_mod_vals - expected_mod_vals

        self.assertFalse(missing_mod_vals, f"The following mod values were not selected: {missing_mod_vals}")
        self.assertFalse(extra_mod_vals, f"The following extra mod values were selected: {extra_mod_vals}")
        
        
    def test_get_mod_value_4(self):
        """
        Test whether we get appropriate mod_values when stat_id=0, gear_level=85, rolled=0, mod_type='greater'
        """
        parsed_mod_vals = set()

        # Generate 1000 random stats for 'weapon' gear type
        for _ in range(10000):
            mod_val = test_get_mod_value(stat_id = 0, gear_level =85, rolled=0, mod_type='greater')
            parsed_mod_vals.add(mod_val)  

        # Ensure only stat id 0 is selected
        expected_mod_vals = set(range(33, 48))
        missing_mod_vals = expected_mod_vals - parsed_mod_vals
        extra_mod_vals = parsed_mod_vals - expected_mod_vals

        self.assertFalse(missing_mod_vals, f"The following mod values were not selected: {missing_mod_vals}")
        self.assertFalse(extra_mod_vals, f"The following extra mod values were selected: {extra_mod_vals}")
        
        
    def test_get_mod_value_5(self):
        """
        Test whether we get appropriate mod_values when stat_id=0, gear_level=85, rolled=0, mod_type='lesser'
        """
        parsed_mod_vals = set()

        # Generate 1000 random stats for 'weapon' gear type
        for _ in range(10000):
            mod_val = test_get_mod_value(stat_id = 0, gear_level =85, rolled=0, mod_type='lesser')
            parsed_mod_vals.add(mod_val)  

        # Ensure only stat id 0 is selected
        expected_mod_vals = set(range(28, 41))
        missing_mod_vals = expected_mod_vals - parsed_mod_vals
        extra_mod_vals = parsed_mod_vals - expected_mod_vals

        self.assertFalse(missing_mod_vals, f"The following mod values were not selected: {missing_mod_vals}")
        self.assertFalse(extra_mod_vals, f"The following extra mod values were selected: {extra_mod_vals}")
        
        
    def test_get_mod_value_6(self):
        """
        Test whether we get appropriate mod_values when stat_id=7, other args default
        """
        parsed_mod_vals = set()

        # Generate 1000 random stats for 'weapon' gear type
        for _ in range(10000):
            mod_val = test_get_mod_value(stat_id = 7)
            parsed_mod_vals.add(mod_val)  

        # Ensure only stat id 0 is selected
        expected_mod_vals = set(range(4, 8))
        missing_mod_vals = expected_mod_vals - parsed_mod_vals
        extra_mod_vals = parsed_mod_vals - expected_mod_vals

        self.assertFalse(missing_mod_vals, f"The following mod values were not selected: {missing_mod_vals}")
        self.assertFalse(extra_mod_vals, f"The following extra mod values were selected: {extra_mod_vals}")
        
        
    def test_get_mod_value_7(self):
        """
        Test whether we get appropriate mod_values when stat_id=6, rolled=1, others default
        """
        parsed_mod_vals = set()

        # Generate 1000 random stats for 'weapon' gear type
        for _ in range(10000):
            mod_val = test_get_mod_value(stat_id = 6, rolled=1)
            parsed_mod_vals.add(mod_val)  

        # Ensure only stat id 0 is selected
        expected_mod_vals = set(range(3, 7))
        missing_mod_vals = expected_mod_vals - parsed_mod_vals
        extra_mod_vals = parsed_mod_vals - expected_mod_vals

        self.assertFalse(missing_mod_vals, f"The following mod values were not selected: {missing_mod_vals}")
        self.assertFalse(extra_mod_vals, f"The following extra mod values were selected: {extra_mod_vals}")
        
        
    def test_get_mod_value_8(self):
        """
        Test whether we get appropriate mod_values when stat_id=5, rolled=2, mod_type='lesser'
        """
        parsed_mod_vals = set()

        # Generate 1000 random stats for 'weapon' gear type
        for _ in range(10000):
            mod_val = test_get_mod_value(stat_id = 5, rolled=2, mod_type='lesser')
            parsed_mod_vals.add(mod_val)  

        # Ensure only stat id 0 is selected
        expected_mod_vals = set(range(8, 12))
        missing_mod_vals = expected_mod_vals - parsed_mod_vals
        extra_mod_vals = parsed_mod_vals - expected_mod_vals

        self.assertFalse(missing_mod_vals, f"The following mod values were not selected: {missing_mod_vals}")
        self.assertFalse(extra_mod_vals, f"The following extra mod values were selected: {extra_mod_vals}")
        
        
    def test_get_mod_value_9(self):
        """
        Test whether we get appropriate mod_values when stat_id=10, rolled=4, mod_type='greater', gear_level=90
        """
        parsed_mod_vals = set()

        # Generate 1000 random stats for 'weapon' gear type
        for _ in range(10000):
            mod_val = test_get_mod_value(stat_id = 10, rolled=4, gear_level=90, mod_type='greater')
            parsed_mod_vals.add(mod_val)  

        # Ensure only stat id 0 is selected
        expected_mod_vals = set(range(10, 14))
        missing_mod_vals = expected_mod_vals - parsed_mod_vals
        extra_mod_vals = parsed_mod_vals - expected_mod_vals

        self.assertFalse(missing_mod_vals, f"The following mod values were not selected: {missing_mod_vals}")
        self.assertFalse(extra_mod_vals, f"The following extra mod values were selected: {extra_mod_vals}")
        
        
    def test_get_mod_value_10(self):
        """
        Test whether we get appropriate mod_values when stat_id=2, rolled=5, mod_type='lesser', gear_level=88
        """
        parsed_mod_vals = set()

        # Generate 1000 random stats for 'weapon' gear type
        for _ in range(10000):
            mod_val = test_get_mod_value(stat_id=2, rolled=5, gear_level=88, mod_type='lesser')
            parsed_mod_vals.add(mod_val)  

        # Ensure only stat id 0 is selected
        expected_mod_vals = set(range(477, 561))
        missing_mod_vals = expected_mod_vals - parsed_mod_vals
        extra_mod_vals = parsed_mod_vals - expected_mod_vals

        self.assertFalse(missing_mod_vals, f"The following mod values were not selected: {missing_mod_vals}")
        self.assertFalse(extra_mod_vals, f"The following extra mod values were selected: {extra_mod_vals}")
        
        
    def test_get_mod_value_invalid(self):
        """
        Test whether we get ValueErrors for invalid entries
        Case 1: invalid gear level (101)
        Case 2: invalid stat_id (-1)
        Case 3: invalid mod_type (some str)
        Case 4: invalid rolled (6, out of bounds)
        Case 5: invalid rolled (negative)
        """
        invalid_entries = [
            [1, 101, None, None],
            [-1, None, None, None],
            [10, None, None, 'big mod'],
            [5, None, 6, None],
            [5, None, -1, None]
        ]
        for stat_id, gear_level, rolled, mod_type in invalid_entries:
            with self.subTest(stat_id=stat_id, gear_level=gear_level, rolled=rolled, mod_type=mod_type):
                with self.assertRaises(ValueError):
                    test_get_mod_value(stat_id, gear_level, rolled, mod_type)

                    
        
if __name__ == '__main__':
    unittest.main()
