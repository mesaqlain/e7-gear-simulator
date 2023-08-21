from set_directory_function import set_directory
set_directory()

import unittest
import json
import random
from tests.test_functions import * 
from src.validation_utils import *
from src.utilities import *

STATS = json.loads(open('data/stats.json', 'r').read())

class TestGetStatValue(unittest.TestCase):
    
    def test_get_stat_value_1(self):
        """
        Test whether we get appropriate stat_values when stat_id=0 and other args default
        """
        parsed_stat_vals = set()

        # Generate 1000 random stats for 'weapon' gear type
        for _ in range(100):
            stat_val = test_get_stat_value(stat_id = 0)
            parsed_stat_vals.add(stat_val)  

        # Ensure only stat id 0 is selected
        expected_stat_vals = set([100])
        missing_stat_vals = expected_stat_vals - parsed_stat_vals
        extra_stat_vals = parsed_stat_vals - expected_stat_vals

        self.assertFalse(missing_stat_vals, f"The following stat values were not selected: {missing_stat_vals}")
        self.assertFalse(extra_stat_vals, f"The following extra stat values were selected: {extra_stat_vals}")


    def test_get_stat_value_2(self):
        """
        Test whether we get appropriate stat_values when stat_id=0, gear_level=85
        """
        parsed_stat_vals = set()

        # Generate 1000 random stats for 'weapon' gear type
        for _ in range(100):
            stat_val = test_get_stat_value(stat_id = 0, gear_level=85)
            parsed_stat_vals.add(stat_val)  

        # Ensure only stat id 0 is selected
        expected_stat_vals = set([100])
        missing_stat_vals = expected_stat_vals - parsed_stat_vals
        extra_stat_vals = parsed_stat_vals - expected_stat_vals

        self.assertFalse(missing_stat_vals, f"The following stat values were not selected: {missing_stat_vals}")
        self.assertFalse(extra_stat_vals, f"The following extra stat values were selected: {extra_stat_vals}")

        
    def test_get_stat_value_3(self):
        """
        Test whether we get appropriate stat_values when stat_id=0, gear_level=85, stat_type='mainstat'
        """
        parsed_stat_vals = set()

        # Generate 1000 random stats for 'weapon' gear type
        for _ in range(100):
            stat_val = test_get_stat_value(stat_id = 0, stat_type='mainstat', gear_level=85)
            parsed_stat_vals.add(stat_val)  

        # Ensure only stat id 0 is selected
        expected_stat_vals = set([100])
        missing_stat_vals = expected_stat_vals - parsed_stat_vals
        extra_stat_vals = parsed_stat_vals - expected_stat_vals

        self.assertFalse(missing_stat_vals, f"The following stat values were not selected: {missing_stat_vals}")
        self.assertFalse(extra_stat_vals, f"The following extra stat values were selected: {extra_stat_vals}")

        
    def test_get_stat_value_4(self):
        """
        Test whether we get appropriate stat_values when stat_id=0, gear_level=85, stat_type='mainstat', grade='rare'
        """
        parsed_stat_vals = set()

        # Generate 1000 random stats for 'weapon' gear type
        for _ in range(100):
            stat_val = test_get_stat_value(stat_id = 0, stat_type='mainstat', gear_level=85, gear_grade='rare')
            parsed_stat_vals.add(stat_val)  

        # Ensure only stat id 0 is selected
        expected_stat_vals = set([100])
        missing_stat_vals = expected_stat_vals - parsed_stat_vals
        extra_stat_vals = parsed_stat_vals - expected_stat_vals

        self.assertFalse(missing_stat_vals, f"The following stat values were not selected: {missing_stat_vals}")
        self.assertFalse(extra_stat_vals, f"The following extra stat values were selected: {extra_stat_vals}")
        
        
    def test_get_stat_value_5(self):
        """
        Test whether we get appropriate stat_values when stat_id=0, gear_level=90, stat_type='mainstat', grade='rare'
        """
        parsed_stat_vals = set()

        # Generate 1000 random stats for 'weapon' gear type
        for _ in range(100):
            stat_val = test_get_stat_value(stat_id = 0, stat_type='mainstat', gear_level=90, gear_grade='rare')
            parsed_stat_vals.add(stat_val)  

        # Ensure only stat id 0 is selected
        expected_stat_vals = set([103])
        missing_stat_vals = expected_stat_vals - parsed_stat_vals
        extra_stat_vals = parsed_stat_vals - expected_stat_vals

        self.assertFalse(missing_stat_vals, f"The following stat values were not selected: {missing_stat_vals}")
        self.assertFalse(extra_stat_vals, f"The following extra stat values were selected: {extra_stat_vals}")
        
        
    def test_get_stat_value_6(self):
        """
        Test whether we get appropriate stat_values when stat_id=7,
        """
        parsed_stat_vals = set()

        # Generate 1000 random stats for 'weapon' gear type
        for _ in range(100):
            stat_val = test_get_stat_value(stat_id = 7)
            parsed_stat_vals.add(stat_val)  

        # Ensure only stat id 0 is selected
        expected_stat_vals = set([13])
        missing_stat_vals = expected_stat_vals - parsed_stat_vals
        extra_stat_vals = parsed_stat_vals - expected_stat_vals

        self.assertFalse(missing_stat_vals, f"The following stat values were not selected: {missing_stat_vals}")
        self.assertFalse(extra_stat_vals, f"The following extra stat values were selected: {extra_stat_vals}")
        
        
    def test_get_stat_value_7(self):
        """
        Test whether we get appropriate stat_values when stat_id=6, gear_level=88, stat_type='substat', grade='epic'
        """
        parsed_stat_vals = set()

        # Generate 1000 random stats for 'weapon' gear type
        for _ in range(100):
            stat_val = test_get_stat_value(stat_id=6, stat_type='substat', gear_level=88, gear_grade='epic')
            parsed_stat_vals.add(stat_val)  

        # Ensure only stat id 0 is selected
        expected_stat_vals = set([3,4,5,6])
        missing_stat_vals = expected_stat_vals - parsed_stat_vals
        extra_stat_vals = parsed_stat_vals - expected_stat_vals

        self.assertFalse(missing_stat_vals, f"The following stat values were not selected: {missing_stat_vals}")
        self.assertFalse(extra_stat_vals, f"The following extra stat values were selected: {extra_stat_vals}")
        
        
    def test_get_stat_value_8(self):
        """
        Test whether we get appropriate stat_values when stat_id=5, gear_level=70, stat_type='substat', grade='rare'
        """
        parsed_stat_vals = set()

        # Generate 1000 random stats for 'weapon' gear type
        for _ in range(100):
            stat_val = test_get_stat_value(stat_id=5, stat_type='substat', gear_level=70, gear_grade='rare')
            parsed_stat_vals.add(stat_val)  

        # Ensure only stat id 0 is selected
        expected_stat_vals = set([4,5,6])
        missing_stat_vals = expected_stat_vals - parsed_stat_vals
        extra_stat_vals = parsed_stat_vals - expected_stat_vals

        self.assertFalse(missing_stat_vals, f"The following stat values were not selected: {missing_stat_vals}")
        self.assertFalse(extra_stat_vals, f"The following extra stat values were selected: {extra_stat_vals}")
        
        
    def test_get_stat_value_9(self):
        """
        Test whether we get appropriate stat_values when stat_id=10, gear_level=90, stat_type='substat', grade='epic'
        """
        parsed_stat_vals = set()

        # Generate 1000 random stats for 'weapon' gear type
        for _ in range(1000):
            stat_val = test_get_stat_value(stat_id=10, stat_type='substat', gear_level=90, gear_grade='epic')
            parsed_stat_vals.add(stat_val)  

        # Ensure only stat id 0 is selected
        expected_stat_vals = set([3,4,5])
        missing_stat_vals = expected_stat_vals - parsed_stat_vals
        extra_stat_vals = parsed_stat_vals - expected_stat_vals

        self.assertFalse(missing_stat_vals, f"The following stat values were not selected: {missing_stat_vals}")
        self.assertFalse(extra_stat_vals, f"The following extra stat values were selected: {extra_stat_vals}")
        
if __name__ == '__main__':
    unittest.main()
