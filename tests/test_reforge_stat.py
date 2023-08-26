from set_directory_function import set_directory
set_directory()

# Imports
import unittest
import json
import random
from src.stats import Stat

with open('data/stats.json', 'r') as stats_file:
    STATS = json.load(stats_file)

class TestReforgeStat(unittest.TestCase):
    """
    Test the reforge stat function 
    """
    
    def test_reforge_stat_speed(self):
        """
        Test if we get the proper reforge increase if we reforge an unrolled speed substat. 
        Specify grade to be heroic so we know that speed ranges from 1 to 4.
        Since the stat is unenhanced, we expect rolled to be 0 before and after reforge.
        Since rolled is 0, after reforge, the speed value won't increase
        """
        for i in range(100):
            stat = Stat()
            stat.get_stat_by_id(10, stat_type = 'substat', gear_type = 'armor')
            stat.parse_stat(gear_grade='heroic')

            self.assertEqual(stat.rolled, 0)
            self.assertIn(stat.value, [1, 2, 3, 4])

            #Reforge the stat
            stat.reforge_stat()

            self.assertEqual(stat.rolled, 0)
            self.assertIn(stat.value, [1, 2, 3, 4])
            
            
    def test_reforge_stat_speed_main(self):
        """
        Test if we get the proper reforge increase if we reforge an unrolled speed mainstat. 
        Since the stat is unenhanced, we expect rolled to be 0 before and after reforge.
        Value should be 8 before reforge (that's the value at base).
        Value should be 45 after reforge (that's the value for speed mainstat after reforge)
        """
        for i in range(100):
            stat = Stat()
            stat.get_stat_by_id(10, stat_type = 'mainstat')
            stat.parse_stat(gear_grade='heroic')

            self.assertIn(stat.value, [8])

            #Reforge the stat
            stat.reforge_stat()

            self.assertEqual(stat.rolled, 0)
            self.assertIn(stat.value, [45])
        
        
    def test_reforge_stat_mainstat(self):
        """
        Test if we get the proper reforge increase if we reforge a mainstat. 
        We fix the value to some arbitrary number before reforge. Since this is mainstat, our 
        expected value for a given mainstat should always be same.
        Value should be 45 after reforge (that's the value for speed mainstat after reforge)
        """
        input_stat_ids = list(STATS.keys())
        expected_values = [525, 65, 2835, 65, 310, 65, 60, 70, 65, 65, 45]
        
        for s, val in enumerate(input_stat_ids):
            input_id = val
            expected_value = expected_values[s]
        
            for i in range(100):
                stat = Stat()
                stat.get_stat_by_id(input_id, stat_type = 'mainstat')
                stat.parse_stat(gear_grade='heroic')
                # Change value to some arbitrary random number
                stat.value = random.randint(1, 1000)

                #Reforge the stat
                stat.reforge_stat()

                self.assertEqual(stat.rolled, 0)
                self.assertEqual(stat.value, expected_value)
                
                
    def test_reforge_stat_percent(self):
        """
        Test if we get the proper reforge increase if we reforge an rolled attack % substat. 
        Specify grade to be epioc so we know that values range from 4 to 8.
        Enhance stat 3 times and each time make sure that the rolled count is accurate.
        After 3 enhancements, we should have rolled = 3, so  the value should increase by 5
        after reforge.
        """
        for i in range(100):
            stat = Stat()
            stat.get_stat_by_id(3, stat_type = 'substat', gear_type = 'armor')
            stat.parse_stat(gear_grade='epic')

            self.assertEqual(stat.rolled, 0)
            self.assertIn(stat.value, [4, 5, 6, 7, 8])
            
            stat.enhance_stat()
            self.assertEqual(stat.rolled, 1)
            
            stat.enhance_stat()
            self.assertEqual(stat.rolled, 2)

            stat.enhance_stat()
            self.assertEqual(stat.rolled, 3)
            
            value_before_reforge = stat.value
            expected_reforge_increase = 5
            expected_reforge_val = value_before_reforge + expected_reforge_increase

            #Reforge the stat
            stat.reforge_stat()

            self.assertEqual(stat.rolled, 3)
            self.assertEqual(stat.value, expected_reforge_val)

                
if __name__ == '__main__':
    unittest.main()