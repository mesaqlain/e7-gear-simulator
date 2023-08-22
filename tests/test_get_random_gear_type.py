from set_directory_function import set_directory
set_directory()

import random
import json
import unittest
from src.utilities import get_random_gear_type

TYPES = json.loads(open('data/types.json', 'r').read())

class TestGetRandomGearType(unittest.TestCase):
    
    def test_get_random_gear_type(self):
        """
        Test whether the get_random_set function returns a str that is one of the 
        sets from sets.json.
        """
        # Initialize starting values of 0, which will be incremented when they are chosen
        
        # number of iterations
        iters = 100000
        picked_types = set()
        
        expected_results = set(TYPES.keys())
        
        for i in range(1, iters):
            picked_type = get_random_gear_type()
            picked_types.add(picked_type)
            self.assertIn(picked_type, list(expected_results), f"Set {picked_type} is not in {expected_results}")
                
        missing = expected_results - picked_types
        extra = picked_types - expected_results
        
        self.assertFalse(missing, f"The following types were not selected: {missing}")
        self.assertFalse(extra, f"The following extra types were selected: {extra}")  

if __name__ == '__main__':
    unittest.main()
