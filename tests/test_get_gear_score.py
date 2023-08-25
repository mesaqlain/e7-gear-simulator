# Add parent directory to path
from set_directory_function import set_directory
set_directory()

# Imports
import unittest
import json
import random
from src.gear import Gear 
from src.stats import Stat

class TestGetGearScore(unittest.TestCase):
    """
    Test the get_gear_score method in Gear() class and see if we get expected results
    """
    
    def test_get_gear_score_rare(self):
        """
        Check if we get expected gear score for a rare gear
        """
        test_gear = Gear()
        test_gear.create_gear(gear_grade='rare', substat_ids=[1, 7])
        
        # Set values
        test_gear.substats[0].value = 8 
        test_gear.substats[1].value = 7
        
        gear_score = test_gear.get_gear_score()
        expected_gear_score = [16, 18]
        
        self.assertEqual(gear_score, expected_gear_score)


    def test_get_gear_score_heroic(self):
        """
        Check if we get expected gear score for a heroic gear
        """
        test_gear = Gear()
        test_gear.create_gear(gear_grade='heroic', substat_ids=[1, 7, 10])
        
        # Set values
        test_gear.substats[0].value = 8 
        test_gear.substats[1].value = 7
        test_gear.substats[2].value = 3

        
        gear_score = test_gear.get_gear_score()
        expected_gear_score = [22, 24]
        
        self.assertEqual(gear_score, expected_gear_score)
        

    def test_get_gear_score_epic(self):
        """
        Check if we get expected gear score for a epic gear
        """
        test_gear = Gear()
        test_gear.create_gear(gear_grade='epic', substat_ids=[1, 7, 10, 8])
        
        # Set values
        test_gear.substats[0].value = 8 
        test_gear.substats[1].value = 7
        test_gear.substats[2].value = 3
        test_gear.substats[3].value = 4        
        
        gear_score = test_gear.get_gear_score()
        expected_gear_score = [26, 29]
        
        self.assertEqual(gear_score, expected_gear_score)
        
        
if __name__ == '__main__':
    unittest.main()
    