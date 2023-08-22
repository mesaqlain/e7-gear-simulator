from set_directory_function import set_directory
set_directory()

import random
import json
import unittest
from src.utilities import get_random_set

SETS = json.loads(open('data/sets.json', 'r').read())

class TestGetRandomSet(unittest.TestCase):
    
    def test_get_random_set(self):
        """
        Test whether the get_random_set function returns a str that is one of the 
        sets from sets.json.
        """
        # Initialize starting values of 0, which will be incremented when they are chosen
        
        # number of iterations
        iters = 100000
        picked_sets = set()
        
        expected_results = set(SETS.keys())
        
        for i in range(1, iters):
            picked_set = get_random_set()
            picked_sets.add(picked_set)
            self.assertIn(picked_set, list(expected_results), f"Set {picked_set} is not in {expected_results}")
                
        missing = expected_results - picked_sets
        extra = picked_sets - expected_results
        
        self.assertFalse(missing, f"The following sets were not selected: {missing}")
        self.assertFalse(extra, f"The following extra sets were selected: {extra}")  

if __name__ == '__main__':
    unittest.main()
