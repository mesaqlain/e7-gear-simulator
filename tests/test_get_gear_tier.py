from set_directory_function import set_directory
set_directory()

import unittest
import json
from src.utilities import get_gear_tier

TIERS = json.loads(open('data/tiers.json', 'r').read())

class TestGetGearTier(unittest.TestCase):
    
    
    def test_get_gear_tier_5(self):
        """
        Test whether any int between 58 and 71 yields 'tier 5' or int 5 output
        """
        
        inputs_ = range(58, 72)
        expected_output = 5
        
        for i in inputs_:
            with self.subTest(gear_level=i):
                gear_tier = get_gear_tier(i)
                self.assertEqual(gear_tier, expected_output)

                
    def test_get_gear_tier_6(self):
        """
        Test whether any int between 72 and 85 yields 'tier 6' or int 6 output
        """
        
        inputs_ = range(72, 85)
        expected_output = 6
        
        for i in inputs_:
            with self.subTest(gear_level=i):
                gear_tier = get_gear_tier(i)
                self.assertEqual(gear_tier, expected_output)
              
            
    def test_get_gear_tier_7(self):
        """
        Test whether any int between 72 and 85 yields 'tier 6' or int 6 output
        """
        
        inputs_ = range(86, 100)
        expected_output = 7
        
        for i in inputs_:
            with self.subTest(gear_level=i):
                gear_tier = get_gear_tier(i)
                self.assertEqual(gear_tier, expected_output)

                
    def test_get_gear_tier_invalid_inputs(self):
        """
        Test whether we get ValueError for invalid inputs
        """
        
        invalid_inputs = [56, 57, 101, 102, 0, -1, '70', 'eighty', [], {}]
        
        for i in invalid_inputs:
            with self.subTest(gear_level=i):
                with self.assertRaises(ValueError):
                    get_gear_tier(i)  
                    
                    
    def test_get_gear_tier_non(self):
        """
        Test whether we get tier 6 if we input None
        """
        self.assertEqual(get_gear_tier(None), 6)
         
            
if __name__ == '__main__':
    unittest.main()
            
