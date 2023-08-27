from set_directory_function import set_directory
set_directory()

# Imports
import unittest
import json
import random
from src.gear import Gear
import copy
from deepdiff import DeepDiff
from unittest.mock import patch

with open('data/stats.json', 'r') as stats_file:
    STATS = json.load(stats_file)
    
class TestReforgeGear(unittest.TestCase):
    """
    Test methods to check if reforge gear works as expected.
    """
    
    def test_reforge_non_lv_85_gear(self):
        """
        Reforge should not work on a gear that is no +15
        """
        input_levels = [70, 75, 80, 88, 90]
        
        for l in input_levels:
            enhance_level = 0
            gear = Gear()
            gear.create_gear(gear_level = l)
            
            # Enhance gear 15 times
            for i in range(15):
                gear.enhance_gear()
                
        gear_before = copy.copy(gear)
        
        with patch('builtins.print') as mock_print:
            
            gear.reforge_gear()

            # Check that the expected output is printed
            mock_print.assert_called_with("Cannot reforge a gear that is not Level 85.")

            # Compare the gear objects using DeepDiff
            diff = DeepDiff(gear, gear_before)
            self.assertTrue(not diff)  # If diff is empty, the objects are the same
            
    def test_reforge_non_fully_enhanced_gear(self):
        """
        Reforge should not work on a gear that has not been fully enhanced
        """
              
        enhance_level = 0
        gear = Gear()
        gear.create_gear()

        enhance_attempts = random.randint(0,14)
        # Enhance gear 15 times
        for i in range(enhance_attempts):
            gear.enhance_gear()
                
        gear_before = copy.copy(gear)
        
        with patch('builtins.print') as mock_print:
            
            gear.reforge_gear()

            # Check that the expected output is printed
            mock_print.assert_called_with("Cannot reforge a gear that has not been enhanced to +15 yet.")

            # Compare the gear objects using DeepDiff
            diff = DeepDiff(gear, gear_before)
            self.assertTrue(not diff)  # If diff is empty, the objects are the same
            
            
    def test_reforge_already_reforged(self):
        """
        Reforging a gear should change its is_reforged status to True and level to 90
        """
        enhance_level = 0
        gear = Gear()
        gear.create_gear()

        # Enhance gear 15 times
        for i in range(15):
            gear.enhance_gear()
            
        # Before reforge
        self.assertFalse(gear.is_reforged)
        self.assertEqual(gear.gear_level, 85)
            
        gear.reforge_gear()
        
        # After reforge
        self.assertTrue(gear.is_reforged)
        self.assertEqual(gear.gear_level, 90)
                

            
    def test_reforge_check_reforge_status(self):
        """
        Test reforge on a mock gear with mainstat=8 (effectiveness) and substats=[1,7,10,9].
        Substats are Atk %, crit damage, Speed, and effect resistance.
        We'll enhance some of the values manually and set fixed values afterwards so that we can expect the reforged value.
        """
        gear = Gear()
        gear.create_gear(mainstat_id=8, substat_ids=[1, 7, 10, 9], gear_type='ring')
        
        # Set mainstat to value at +15
        gear.mainstat.enhance_stat(14)
        
        # Enhance 5 substats, these should change their rolled value and reforge_increase value
        gear.substats[0].enhance_stat()
        gear.substats[0].enhance_stat()
        gear.substats[1].enhance_stat()
        gear.substats[2].enhance_stat()
        gear.substats[2].enhance_stat()
        
        # Manually fix the substats so that we may predict reforged stats
        gear.substats[0].value = 15
        gear.substats[1].value = 10
        gear.substats[2].value = 6
        gear.substats[3].value = 7
        
        # Set enhance_level to +15 so we may reforge
        gear.enhance_level = 15
        
        # Reforge gear
        gear.reforge_gear()

        self.assertEqual(gear.gear_level, 90)
        self.assertTrue(gear.is_reforged)
        self.assertEqual(gear.mainstat.value, 65) # mainstat reforged value for eff
        self.assertEqual(gear.substats[0].value, 19) # 2 rolls so +4 for atk%
        self.assertEqual(gear.substats[1].value, 12) # 1 roll so +2 for cdmg
        self.assertEqual(gear.substats[2].value, 8) # 2 rolls so +2 for spd
        self.assertEqual(gear.substats[3].value, 8) # 0  rolls so +1 for eff_res

    
if __name__ == '__main__':
    unittest.main()
