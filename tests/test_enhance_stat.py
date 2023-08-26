from set_directory_function import set_directory
set_directory()

# Imports
import unittest
import json
import random
from src.stats import Stat

class TestEnhanceStat(unittest.TestCase):
    """
    Test the enhance stat function 
    """
    
    def test_enhance_stat_mainstat_attack(self):
        """
        Test whether the mainstat goes up appropriately when an attack stat has been enhanced
        from +0 to +1
        """
        stat = Stat()
        stat.get_stat_by_id(0, stat_type='mainstat')
        stat.parse_stat(stat_type='mainstat', gear_type='weapon', gear_grade='heroic', 
                   gear_level=85)
        stat.format_stat()
        
        input_enhance_level = 0
        self.assertEqual(stat.value, 100)
        stat.enhance_stat(enhance_level=input_enhance_level)
        expected_value = 120
        self.assertEqual(stat.value, expected_value)
        self.assertEqual(stat.text_formatted, '120 Attack')
        
        
    def test_enhance_stat_mainstat_crit_chance(self):
        """
        Test whether the mainstat goes up appropriately when a crit chance stat has been enhanced
        from +1 to +2
        """
        stat = Stat()
        stat.get_stat_by_id(6, stat_type='mainstat')
        stat.parse_stat(stat_type='mainstat', gear_type='necklace', gear_grade='epic', 
                   gear_level=88)
        stat.format_stat()
        stat.value = 14
        input_enhance_level = 1
        self.assertEqual(stat.value, 14)
        stat.enhance_stat(enhance_level=input_enhance_level)
        expected_value = 17
        self.assertEqual(stat.value, expected_value)
        self.assertEqual(stat.text_formatted, '17% Crit Chance')        
        
        
    def test_enhance_stat_mainstat_speed(self):
        """
        Test whether the mainstat goes up appropriately when a crit chance stat has been enhanced
        from +14 to +15
        """
        stat = Stat()
        stat.get_stat_by_id(10, stat_type='mainstat')
        stat.parse_stat(stat_type='mainstat', gear_type='boots', gear_grade='epic', 
                   gear_level=85)
        stat.format_stat()
        
        stat.value = 34
        input_enhance_level = 14
        self.assertEqual(stat.value, 34)
        stat.enhance_stat(enhance_level=input_enhance_level)
        expected_value = 40
        self.assertEqual(stat.value, expected_value)
        self.assertEqual(stat.text_formatted, '40 Speed')
        
    def test_enhance_stat_mainstat_eff(self):
        """
        Test whether the mainstat goes up appropriately when an Effectiveness % stat has been enhanced
        from +0 to +15
        """
        # Initialize enhance level
        enhance_level = 0
        stat = Stat()
        # Get stat value 8 (effectiveness)
        stat.get_stat_by_id(8, stat_type='mainstat', gear_type='ring')
        stat.parse_stat(stat.stat_type, gear_type=stat.gear_type, gear_grade='epic', 
                   gear_level=85)
        stat.format_stat()
        expected_values = [14, 17, 19, 22, 24, 26, 29, 31, 34, 36, 40, 43, 47, 51, 60]
        
        for i in range(15):
            stat.enhance_stat(enhance_level=enhance_level)
            expected_value = expected_values[i]
            self.assertEqual(stat.value, expected_value)
            enhance_level += 1

        
        
    def test_enhance_stat_substat_speed(self):
        """
        Test whether a speed substat goes up appropriately when rolled count is 0
        """
        for i in range(1000):
            stat = Stat()
            stat.get_stat_by_id(10, stat_type='substat')
            stat.parse_stat(stat_type=stat.stat_type, gear_type='boots', gear_grade='epic', 
                       gear_level=85)
            stat.format_stat()

            # Check if rolled is 0 as expected
            self.assertEqual(stat.rolled, 0)
            stat.enhance_stat()

            expected_values = [4, 5, 6, 7, 8, 9, 10]
            expected_text_fromatted = ['4 Speed', '5 Speed', '6 Speed', '7 Speed', '8 Speed', '9 Speed', '10 Speed']

            self.assertIn(stat.value, expected_values, f"{stat.value} not in {expected_values}")
            self.assertIn(stat.text_formatted, expected_text_fromatted)
            self.assertEqual(stat.reforge_increase, 1)
            self.assertEqual(stat.rolled, 1)
            
            
    def test_enhance_stat_substat_attack(self):
        """
        Test whether an attack % substat goes up appropriately when rolled count is 3
        """
        for i in range(1000):
            stat = Stat()
            stat.get_stat_by_id(1, stat_type='substat')
            stat.parse_stat(stat_type=stat.stat_type, gear_type='ring', gear_grade='heroic', 
                       gear_level=85)
            stat.format_stat()
            
            # Set a new rolled value
            stat.rolled = 3

            # Check if rolled is 0 as expected
            self.assertEqual(stat.rolled, 3)
            # Check if we got appropriate attack % value
            self.assertIn(stat.value, [4, 5, 6, 7, 8])
            
            # Change to new value
            stat.value = 20
            
            # Enhance the stat (expect value to go up by 4-8)
            stat.enhance_stat()

            expected_values = [24, 25, 26, 27, 28]
            expected_text_fromatted = ['24% Attack', '25% Attack', '26% Attack', '27% Attack', '28% Attack']

            self.assertIn(stat.value, expected_values, f"{stat.value} not in {expected_values}")
            self.assertIn(stat.text_formatted, expected_text_fromatted)
            self.assertEqual(stat.reforge_increase, 7)
            self.assertEqual(stat.rolled, 4)

        

if __name__ == '__main__':
    unittest.main()
        
