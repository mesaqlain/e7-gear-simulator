from set_directory_function import set_directory
set_directory()

# Imports
import unittest
import json
import random
import copy
from deepdiff import DeepDiff
from src.gear import Gear
from src.stats import Stat
from src.utilities import convert_int_to_str
from unittest.mock import patch


class TestEnhanceGear(unittest.TestCase):
    """
    Test the enhance_gear method in the Gear() class
    """
    
    def test_rare_gear(self):
        """
        Test a rare gear
        """
        gear = Gear()
        gear.create_gear(gear_grade='rare', gear_type='weapon', substat_ids=[10, 6])
        enhance_level = 0
        expected_mainstat_values = [120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 330, 360, 390, 425, 500]
        
        # Ensure mainstat value
        self.assertEqual(gear.mainstat.value, 100)
        
        # Track substats rolled before and after enhancement
        prev_rolled = [s.rolled for s in gear.substats]
        prev_values = [s.value for s in gear.substats]
        
        speed_expected_increase = [1, 2, 3, 4]
        crit_expected_increase = [3, 4, 5]

        for i in range(15):
            gear.enhance_gear()
            
            # Test gear enhancement level
            self.assertEqual(gear.enhance_level, i+1)
            # Test mainstat value
            self.assertEqual(gear.mainstat.value, expected_mainstat_values[i])
            # Check that there are 2 substats before +9
            if i < 8:
                self.assertEqual(len(gear.substats), 2)
            # Check that there are 2 substats before +12
            elif i < 11:
                self.assertEqual(len(gear.substats), 3)
            # Check that there are 4 substats after +12
            else:
                self.assertEqual(len(gear.substats), 4)
                
            if i == 2:
                enhanced_substat_idx = None
                new_rolled = [s.rolled for s in gear.substats]
                new_values = [s.value for s in gear.substats]
                for idx, (prev_val, new_val) in enumerate(zip(prev_rolled, new_rolled)):
                    if prev_val != new_val:
                        enhanced_substat_idx = idx
                        break
                        
                # Ensure that substat at enhanced_substat_idx increased by 1
                self.assertEqual(gear.substats[enhanced_substat_idx].rolled, prev_rolled[enhanced_substat_idx] + 1)
                # If speed was enhanced, check that we have an enhanced value
                if gear.substats[enhanced_substat_idx].stat_id == 10:
                    expected_values = [prev_values[enhanced_substat_idx] + increase for increase in speed_expected_increase]
                    self.assertIn(gear.substats[enhanced_substat_idx].value, expected_values)
                # If crit was enhance, check that we have an enhanced value
                if gear.substats[enhanced_substat_idx].stat_id == 6:
                    expected_values = [prev_values[enhanced_substat_idx] + increase for increase in crit_expected_increase]
                    self.assertIn(gear.substats[enhanced_substat_idx].value, expected_values)
                
            elif i == 5:
                enhanced_substat_idx = None
                new_rolled = [s.rolled for s in gear.substats]
                for idx, (prev_val, new_val) in enumerate(zip(prev_rolled, new_rolled)):
                    if prev_val != new_val:
                        enhanced_substat_idx = idx
                        break
                        
                # Ensure that substat at enhanced_substat_idx increased by 1
                self.assertEqual(gear.substats[enhanced_substat_idx].rolled, prev_rolled[enhanced_substat_idx] + 1)
                # If speed was enhanced, check that we have an enhanced value
                if gear.substats[enhanced_substat_idx].stat_id == 10:
                    expected_values = [prev_values[enhanced_substat_idx] + increase for increase in speed_expected_increase]
                    self.assertIn(gear.substats[enhanced_substat_idx].value, expected_values)
                # If crit was enhance, check that we have an enhanced value
                if gear.substats[enhanced_substat_idx].stat_id == 6:
                    expected_values = [prev_values[enhanced_substat_idx] + increase for increase in crit_expected_increase]
                    self.assertIn(gear.substats[enhanced_substat_idx].value, expected_values)
                
            elif i == 14:
                enhanced_substat_idx = None
                new_rolled = [s.rolled for s in gear.substats]
                for idx, (prev_val, new_val) in enumerate(zip(prev_rolled, new_rolled)):
                    if prev_val != new_val:
                        enhanced_substat_idx = idx
                        break

            # Update prev_substats for the next iteration
            prev_rolled = [s.rolled for s in gear.substats]
            prev_values = [s.value for s in gear.substats]

            
    def test_heroic_gear(self):
        """
        Test a heroic gear
        """
        gear = Gear()
        gear.create_gear(gear_grade='heroic', gear_type='boots', substat_ids=[10, 6, 1], mainstat_id=0)
        enhance_level = 0
        expected_mainstat_values = [120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 330, 360, 390, 425, 500]
        
        # Ensure mainstat value
        self.assertEqual(gear.mainstat.value, 100)
        
        # Track substats rolled before and after enhancement
        prev_rolled = [s.rolled for s in gear.substats]
        prev_values = [s.value for s in gear.substats]
        
        speed_expected_increase = [1, 2, 3, 4]
        crit_expected_increase = [3, 4, 5]
        attack_expected_increase = [4, 5, 6, 7, 8]

        for i in range(15):
            gear.enhance_gear()
            
            # Test gear enhancement level
            self.assertEqual(gear.enhance_level, i+1)
            # Test mainstat value
            self.assertEqual(gear.mainstat.value, expected_mainstat_values[i])
            # Check that there are 2 substats before +9
            if i < 8:
                self.assertEqual(len(gear.substats), 3)
            # Check that there are 2 substats before +12
            elif i < 11:
                self.assertEqual(len(gear.substats), 3)
            # Check that there are 4 substats after +12
            else:
                self.assertEqual(len(gear.substats), 4)
                
            if i == 2:
                enhanced_substat_idx = None
                new_rolled = [s.rolled for s in gear.substats]
                new_values = [s.value for s in gear.substats]
                for idx, (prev_val, new_val) in enumerate(zip(prev_rolled, new_rolled)):
                    if prev_val != new_val:
                        enhanced_substat_idx = idx
                        break
                        
                # Ensure that substat at enhanced_substat_idx increased by 1
                self.assertEqual(gear.substats[enhanced_substat_idx].rolled, prev_rolled[enhanced_substat_idx] + 1)
                # If speed was enhanced, check that we have an enhanced value
                if gear.substats[enhanced_substat_idx].stat_id == 10:
                    expected_values = [prev_values[enhanced_substat_idx] + increase for increase in speed_expected_increase]
                    self.assertIn(gear.substats[enhanced_substat_idx].value, expected_values)
                # If crit was enhance, check that we have an enhanced value
                if gear.substats[enhanced_substat_idx].stat_id == 6:
                    expected_values = [prev_values[enhanced_substat_idx] + increase for increase in crit_expected_increase]
                    self.assertIn(gear.substats[enhanced_substat_idx].value, expected_values)
                # If attack % was enhance, check that we have an enhanced value
                if gear.substats[enhanced_substat_idx].stat_id == 1:
                    expected_values = [prev_values[enhanced_substat_idx] + increase for increase in attack_expected_increase]
                    self.assertIn(gear.substats[enhanced_substat_idx].value, expected_values)
                                    
                
            elif i == 5:
                enhanced_substat_idx = None
                new_rolled = [s.rolled for s in gear.substats]
                for idx, (prev_val, new_val) in enumerate(zip(prev_rolled, new_rolled)):
                    if prev_val != new_val:
                        enhanced_substat_idx = idx
                        break
                        
                # Ensure that substat at enhanced_substat_idx increased by 1
                self.assertEqual(gear.substats[enhanced_substat_idx].rolled, prev_rolled[enhanced_substat_idx] + 1)
                # If speed was enhanced, check that we have an enhanced value
                if gear.substats[enhanced_substat_idx].stat_id == 10:
                    expected_values = [prev_values[enhanced_substat_idx] + increase for increase in speed_expected_increase]
                    self.assertIn(gear.substats[enhanced_substat_idx].value, expected_values)
                # If crit was enhance, check that we have an enhanced value
                if gear.substats[enhanced_substat_idx].stat_id == 6:
                    expected_values = [prev_values[enhanced_substat_idx] + increase for increase in crit_expected_increase]
                    self.assertIn(gear.substats[enhanced_substat_idx].value, expected_values)
                # If attack % was enhance, check that we have an enhanced value
                if gear.substats[enhanced_substat_idx].stat_id == 1:
                    expected_values = [prev_values[enhanced_substat_idx] + increase for increase in attack_expected_increase]
                    self.assertIn(gear.substats[enhanced_substat_idx].value, expected_values)                   
                                    
            elif i == 8:
                enhanced_substat_idx = None
                new_rolled = [s.rolled for s in gear.substats]
                for idx, (prev_val, new_val) in enumerate(zip(prev_rolled, new_rolled)):
                    if prev_val != new_val:
                        enhanced_substat_idx = idx
                        break
                        
                # Ensure that substat at enhanced_substat_idx increased by 1
                self.assertEqual(gear.substats[enhanced_substat_idx].rolled, prev_rolled[enhanced_substat_idx] + 1)
                # If speed was enhanced, check that we have an enhanced value
                if gear.substats[enhanced_substat_idx].stat_id == 10:
                    expected_values = [prev_values[enhanced_substat_idx] + increase for increase in speed_expected_increase]
                    self.assertIn(gear.substats[enhanced_substat_idx].value, expected_values)
                # If crit was enhance, check that we have an enhanced value
                if gear.substats[enhanced_substat_idx].stat_id == 6:
                    expected_values = [prev_values[enhanced_substat_idx] + increase for increase in crit_expected_increase]
                    self.assertIn(gear.substats[enhanced_substat_idx].value, expected_values)
                # If attack % was enhance, check that we have an enhanced value
                if gear.substats[enhanced_substat_idx].stat_id == 1:
                    expected_values = [prev_values[enhanced_substat_idx] + increase for increase in attack_expected_increase]
                    self.assertIn(gear.substats[enhanced_substat_idx].value, expected_values)
                
            elif i == 14:
                enhanced_substat_idx = None
                new_rolled = [s.rolled for s in gear.substats]
                for idx, (prev_val, new_val) in enumerate(zip(prev_rolled, new_rolled)):
                    if prev_val != new_val:
                        enhanced_substat_idx = idx
                        break

            # Update prev_substats for the next iteration
            prev_rolled = [s.rolled for s in gear.substats]
            prev_values = [s.value for s in gear.substats]            

            
    def test_epic_gear(self):
        """
        Test a epic gear
        """
        gear = Gear()
        gear.create_gear(gear_grade='epic', gear_type='ring', substat_ids=[10, 6, 1, 3], mainstat_id=0)
        enhance_level = 0
        expected_mainstat_values = [120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 330, 360, 390, 425, 500]
        
        # Ensure mainstat value
        self.assertEqual(gear.mainstat.value, 100)
        
        # Track substats rolled before and after enhancement
        prev_rolled = [s.rolled for s in gear.substats]
        prev_values = [s.value for s in gear.substats]
        
        speed_expected_increase = [1, 2, 3, 4]
        crit_expected_increase = [3, 4, 5]
        attack_expected_increase = [4, 5, 6, 7, 8]
        health_expected_increase = attack_expected_increase

        for i in range(15):
            gear.enhance_gear()
            
            # Test gear enhancement level
            self.assertEqual(gear.enhance_level, i+1)
            # Test mainstat value
            self.assertEqual(gear.mainstat.value, expected_mainstat_values[i])
            self.assertEqual(len(gear.substats), 4)
                
            if i == 2:
                enhanced_substat_idx = None
                new_rolled = [s.rolled for s in gear.substats]
                new_values = [s.value for s in gear.substats]
                for idx, (prev_val, new_val) in enumerate(zip(prev_rolled, new_rolled)):
                    if prev_val != new_val:
                        enhanced_substat_idx = idx
                        break
                        
                # Ensure that substat at enhanced_substat_idx increased by 1
                self.assertEqual(gear.substats[enhanced_substat_idx].rolled, prev_rolled[enhanced_substat_idx] + 1)
                # If speed was enhanced, check that we have an enhanced value
                if gear.substats[enhanced_substat_idx].stat_id == 10:
                    expected_values = [prev_values[enhanced_substat_idx] + increase for increase in speed_expected_increase]
                    self.assertIn(gear.substats[enhanced_substat_idx].value, expected_values)
                # If crit was enhance, check that we have an enhanced value
                if gear.substats[enhanced_substat_idx].stat_id == 6:
                    expected_values = [prev_values[enhanced_substat_idx] + increase for increase in crit_expected_increase]
                    self.assertIn(gear.substats[enhanced_substat_idx].value, expected_values)
                # If attack % was enhance, check that we have an enhanced value
                if gear.substats[enhanced_substat_idx].stat_id == 1:
                    expected_values = [prev_values[enhanced_substat_idx] + increase for increase in attack_expected_increase]
                    self.assertIn(gear.substats[enhanced_substat_idx].value, expected_values)
                # If attack % was enhance, check that we have an enhanced value
                if gear.substats[enhanced_substat_idx].stat_id == 3:
                    expected_values = [prev_values[enhanced_substat_idx] + increase for increase in health_expected_increase]
                    self.assertIn(gear.substats[enhanced_substat_idx].value, expected_values)
                                    
                
            elif i == 5:
                enhanced_substat_idx = None
                new_rolled = [s.rolled for s in gear.substats]
                for idx, (prev_val, new_val) in enumerate(zip(prev_rolled, new_rolled)):
                    if prev_val != new_val:
                        enhanced_substat_idx = idx
                        break
                        
                # Ensure that substat at enhanced_substat_idx increased by 1
                self.assertEqual(gear.substats[enhanced_substat_idx].rolled, prev_rolled[enhanced_substat_idx] + 1)
                # If speed was enhanced, check that we have an enhanced value
                if gear.substats[enhanced_substat_idx].stat_id == 10:
                    expected_values = [prev_values[enhanced_substat_idx] + increase for increase in speed_expected_increase]
                    self.assertIn(gear.substats[enhanced_substat_idx].value, expected_values)
                # If crit was enhance, check that we have an enhanced value
                if gear.substats[enhanced_substat_idx].stat_id == 6:
                    expected_values = [prev_values[enhanced_substat_idx] + increase for increase in crit_expected_increase]
                    self.assertIn(gear.substats[enhanced_substat_idx].value, expected_values)
                # If attack % was enhance, check that we have an enhanced value
                if gear.substats[enhanced_substat_idx].stat_id == 1:
                    expected_values = [prev_values[enhanced_substat_idx] + increase for increase in attack_expected_increase]
                    self.assertIn(gear.substats[enhanced_substat_idx].value, expected_values)  
                # If attack % was enhance, check that we have an enhanced value
                if gear.substats[enhanced_substat_idx].stat_id == 3:
                    expected_values = [prev_values[enhanced_substat_idx] + increase for increase in health_expected_increase]
                    self.assertIn(gear.substats[enhanced_substat_idx].value, expected_values)
                                    
            elif i == 8:
                enhanced_substat_idx = None
                new_rolled = [s.rolled for s in gear.substats]
                for idx, (prev_val, new_val) in enumerate(zip(prev_rolled, new_rolled)):
                    if prev_val != new_val:
                        enhanced_substat_idx = idx
                        break
                        
                # Ensure that substat at enhanced_substat_idx increased by 1
                self.assertEqual(gear.substats[enhanced_substat_idx].rolled, prev_rolled[enhanced_substat_idx] + 1)
                # If speed was enhanced, check that we have an enhanced value
                if gear.substats[enhanced_substat_idx].stat_id == 10:
                    expected_values = [prev_values[enhanced_substat_idx] + increase for increase in speed_expected_increase]
                    self.assertIn(gear.substats[enhanced_substat_idx].value, expected_values)
                # If crit was enhance, check that we have an enhanced value
                if gear.substats[enhanced_substat_idx].stat_id == 6:
                    expected_values = [prev_values[enhanced_substat_idx] + increase for increase in crit_expected_increase]
                    self.assertIn(gear.substats[enhanced_substat_idx].value, expected_values)
                # If attack % was enhance, check that we have an enhanced value
                if gear.substats[enhanced_substat_idx].stat_id == 1:
                    expected_values = [prev_values[enhanced_substat_idx] + increase for increase in attack_expected_increase]
                    self.assertIn(gear.substats[enhanced_substat_idx].value, expected_values)
                # If attack % was enhance, check that we have an enhanced value
                if gear.substats[enhanced_substat_idx].stat_id == 3:
                    expected_values = [prev_values[enhanced_substat_idx] + increase for increase in health_expected_increase]
                    self.assertIn(gear.substats[enhanced_substat_idx].value, expected_values)
                
            elif i == 11:
                enhanced_substat_idx = None
                new_rolled = [s.rolled for s in gear.substats]
                for idx, (prev_val, new_val) in enumerate(zip(prev_rolled, new_rolled)):
                    if prev_val != new_val:
                        enhanced_substat_idx = idx
                        break
                        
                # Ensure that substat at enhanced_substat_idx increased by 1
                self.assertEqual(gear.substats[enhanced_substat_idx].rolled, prev_rolled[enhanced_substat_idx] + 1)
                # If speed was enhanced, check that we have an enhanced value
                if gear.substats[enhanced_substat_idx].stat_id == 10:
                    expected_values = [prev_values[enhanced_substat_idx] + increase for increase in speed_expected_increase]
                    self.assertIn(gear.substats[enhanced_substat_idx].value, expected_values)
                # If crit was enhance, check that we have an enhanced value
                if gear.substats[enhanced_substat_idx].stat_id == 6:
                    expected_values = [prev_values[enhanced_substat_idx] + increase for increase in crit_expected_increase]
                    self.assertIn(gear.substats[enhanced_substat_idx].value, expected_values)
                # If attack % was enhance, check that we have an enhanced value
                if gear.substats[enhanced_substat_idx].stat_id == 1:
                    expected_values = [prev_values[enhanced_substat_idx] + increase for increase in attack_expected_increase]
                    self.assertIn(gear.substats[enhanced_substat_idx].value, expected_values)
                # If attack % was enhance, check that we have an enhanced value
                if gear.substats[enhanced_substat_idx].stat_id == 3:
                    expected_values = [prev_values[enhanced_substat_idx] + increase for increase in health_expected_increase]
                    self.assertIn(gear.substats[enhanced_substat_idx].value, expected_values)

            elif i == 14:
                enhanced_substat_idx = None
                new_rolled = [s.rolled for s in gear.substats]
                for idx, (prev_val, new_val) in enumerate(zip(prev_rolled, new_rolled)):
                    if prev_val != new_val:
                        enhanced_substat_idx = idx
                        break
                        
                # Ensure that substat at enhanced_substat_idx increased by 1
                self.assertEqual(gear.substats[enhanced_substat_idx].rolled, prev_rolled[enhanced_substat_idx] + 1)
                # If speed was enhanced, check that we have an enhanced value
                if gear.substats[enhanced_substat_idx].stat_id == 10:
                    expected_values = [prev_values[enhanced_substat_idx] + increase for increase in speed_expected_increase]
                    self.assertIn(gear.substats[enhanced_substat_idx].value, expected_values)
                # If crit was enhance, check that we have an enhanced value
                if gear.substats[enhanced_substat_idx].stat_id == 6:
                    expected_values = [prev_values[enhanced_substat_idx] + increase for increase in crit_expected_increase]
                    self.assertIn(gear.substats[enhanced_substat_idx].value, expected_values)
                # If attack % was enhance, check that we have an enhanced value
                if gear.substats[enhanced_substat_idx].stat_id == 1:
                    expected_values = [prev_values[enhanced_substat_idx] + increase for increase in attack_expected_increase]
                    self.assertIn(gear.substats[enhanced_substat_idx].value, expected_values)
                # If attack % was enhance, check that we have an enhanced value
                if gear.substats[enhanced_substat_idx].stat_id == 3:
                    expected_values = [prev_values[enhanced_substat_idx] + increase for increase in health_expected_increase]
                    self.assertIn(gear.substats[enhanced_substat_idx].value, expected_values)
                    
                    
            # Update prev_substats for the next iteration
            prev_rolled = [s.rolled for s in gear.substats]
            prev_values = [s.value for s in gear.substats]            
            
            
    def test_max_gear(self):
        """
        Test a epic gear
        """
        gear = Gear()
        gear.create_gear(gear_grade='epic', gear_type='ring', substat_ids=[10, 6, 1, 3], mainstat_id=0)
        gear.enhance_level = 15
                    
        gear_before = copy.copy(gear)
        
        with patch('builtins.print') as mock_print:
            gear.enhance_gear()
            
            # Check that the expected output is printed
            mock_print.assert_called_with("Gear is already at maximum enhancement level!")
            
            # Compare the gear objects using DeepDiff
            diff = DeepDiff(gear, gear_before)
            self.assertTrue(not diff)  # If diff is empty, the objects are the same
            
            
if __name__ == '__main__':
    unittest.main()