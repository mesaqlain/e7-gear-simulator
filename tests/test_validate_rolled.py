from set_directory_function import set_directory
set_directory()

import unittest
from src.validation_utils import validate_rolled 

class TestValidateRolled(unittest.TestCase):

    def test_valid_rolled(self):
        """Test whether valid int returns the expected results"""
        valid_rolled = [0, 1, 2, 3, 4, 5]
        expected_rolled = [0, 1, 2, 3, 4, 5]
        for i, rolled_val in enumerate(valid_rolled):
            self.assertEqual(validate_rolled(rolled_val), expected_rolled[i], f"Valid rolled value of {rolled_val} should return {expected_rolled[i]}.")
            
            
    def test_valid_rolled_substat(self):
        """Test whether valid int returns the expected results when stat_type is 'substat'"""
        valid_rolled = [0, 1, 2, 3, 4, 5]
        expected_rolled = [0, 1, 2, 3, 4, 5]
        for i, rolled_val in enumerate(valid_rolled):
            self.assertEqual(validate_rolled(rolled_val, 'substat'), expected_rolled[i], f"Valid rolled value of {rolled_val} should return {expected_rolled[i]}.")
            
     
    def test_invalid_rolled_mainstats(self):
        """Test whether valid non-zero int raises ValueError when stat_type is 'mainstat'"""
        invalid_rolled = [1, 2, 3, 4, 5]
        for i in enumerate(invalid_rolled):
            with self.assertRaises(ValueError):
                validate_rolled(i, 'mainstat')        

            
    def test_valid_rolled_none(self):
        """Test whether None returns 0"""
        self.assertEqual(validate_rolled(None), 0, f"Valid rolled value of None should return 0.")
        
    def test_invalid_rolled(self):
        """
        Test whether invalid entries raise ValueError.
        Case 1: Some str
        Case 2: Some negative number
        Case 3: Some large int
        Case 4: An empty list
        """
        valid_rolled = ['1', -1, 200, []]
        for i in valid_rolled:
            with self.assertRaises(ValueError): 
                validate_rolled(i)
        
if __name__ == '__main__':
    unittest.main()
