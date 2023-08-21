from set_directory_function import set_directory
set_directory()

import unittest
import json
import random
from src.stats import Stat
from src.validation_utils import *
from src.utilities import *

class TestFormatMainStat(unittest.TestCase):

    def setUp(self):
        self.stat = Stat()
        
        
    def tearDown(self):
        self.stat = None

        
    def test_format_stat_main_1(self):
        """
        Test using Attack% as our mainstat, gear_grade='epic'
        gear_level = default 85, so we expect value of 12
        """
        
        self.stat.get_stat_by_id(1, stat_type='mainstat')
        self.stat.parse_stat(gear_grade='epic')
        formatted_text = self.stat.format_stat()
        expected_text = '12% Attack'
        
        self.assertEqual(formatted_text, expected_text, f"Was expecting: {expected_text}, but received {formatted_text}.")
        
        
    def test_format_stat_main_2(self):
        """
        Test using Speed as our mainstat, gear_grade='epic'
        gear_level = 90, so we expect value of 9 as base and 45 as reforged
        """
        
        self.stat.get_stat_by_id(10, stat_type='mainstat')
        self.stat.parse_stat(gear_grade='heroic', gear_level=90)
        formatted_text = self.stat.format_stat(show_reforged=True)
        expected_text = '9 (45) Speed'
        
        self.assertEqual(formatted_text, expected_text, f"Was expecting: {expected_text}, but received {formatted_text}.")
        
        
    def test_format_stat_sub_1(self):
        """
        Test using Defense% as our substat, gear_grade='heroic'
        gear_level = 70, so we expect value of 4,5,6 or 7
        Repeat this test 1000 times.
        """
        parsed_text_list = set()
        expected_text_list = set(['4% Defense', '5% Defense', '6% Defense', '7% Defense'])
        
        for i in range(1000):
            
            self.stat.get_stat_by_id(5, stat_type='substat')
            self.stat.parse_stat(gear_grade='heroic', gear_level=70)
            formatted_text = self.stat.format_stat()
            parsed_text_list.add(formatted_text)
            expected_texts = list(expected_text_list)

            self.assertIn(formatted_text, expected_texts, f"{formatted_text} was no expected.")
            
        missing_vals = expected_text_list - parsed_text_list
        extra_vals = parsed_text_list - expected_text_list
        
        self.assertFalse(missing_vals, f"The following values were not selected: {missing_vals}")
        self.assertFalse(extra_vals, f"The following extra values were selected: {extra_vals}")  

        
    def test_format_stat_sub_2(self):
        """
        Test using Health% as our substat, gear_grade='epic'
        gear_level = 85, so we expect value of 4,5,6 or 7
        Repeat this test 1000 times.
        """
        parsed_text_list = set()
        expected_text_list = set(['4% Health (modded)' , '5% Health (modded)', '6% Health (modded)', 
                                  '7% Health (modded)', '8% Health (modded)'])
        
        for i in range(1000):
            
            self.stat.get_stat_by_id(3, stat_type='substat')
            self.stat.parse_stat(gear_grade='epic', gear_level=85, mod=True)
            formatted_text = self.stat.format_stat()
            parsed_text_list.add(formatted_text)
            expected_texts = list(expected_text_list)

            self.assertIn(formatted_text, expected_texts, f"{formatted_text} was no expected.")
            
        missing_vals = expected_text_list - parsed_text_list
        extra_vals = parsed_text_list - expected_text_list
        
        self.assertFalse(missing_vals, f"The following values were not selected: {missing_vals}")
        self.assertFalse(extra_vals, f"The following extra values were selected: {extra_vals}")
        
        
    def test_format_stat_sub_3(self):
        """
        Test using Crit Chance% as our substat, gear_grade='epic'
        gear_level = 90, so we expect value of 4,5,6 or 7
        show_reforge = True and mod = True (default rolled = 0, so reforge_increase should be 1)
        so we expect values (2, 3, 4) and reforged values (3, 4, 5)
        Repeat this test 1000 times.
        """
        parsed_text_list = set()
        expected_text_list = set(['2% (3%) Crit Chance (modded)', '3% (4%) Crit Chance (modded)', 
                                 '4% (5%) Crit Chance (modded)'])
        
        for i in range(1000):
            
            self.stat.get_stat_by_id(6, stat_type='substat')
            self.stat.parse_stat(gear_grade='epic', gear_level=85, mod=True)
            formatted_text = self.stat.format_stat(show_reforged=True)
            parsed_text_list.add(formatted_text)
            expected_texts = list(expected_text_list)

            self.assertIn(formatted_text, expected_texts, f"{formatted_text} was no expected.")
            
        missing_vals = expected_text_list - parsed_text_list
        extra_vals = parsed_text_list - expected_text_list
        
        self.assertFalse(missing_vals, f"The following values were not selected: {missing_vals}")
        self.assertFalse(extra_vals, f"The following extra values were selected: {extra_vals}")  

        
    def test_format_stat_sub_4(self):
        """
        Test using Crit Chance% as our substat, gear_grade='epic', gear_level = 85
        show_reforge = True and mod = True rolled = 3, mod_type='lesser' so reforge_increase should be 4.
        We expect values (4, 5, 6, 7) and reforged values (8, 9, 10, 11)
        Repeat this test 1000 times.
        """
        parsed_text_list = set()
        expected_text_list = set(['4% (8%) Crit Chance (modded)', '5% (9%) Crit Chance (modded)', 
                                 '6% (10%) Crit Chance (modded)', '7% (11%) Crit Chance (modded)'])
        
        for i in range(1000):
            
            self.stat.get_stat_by_id(6, stat_type='substat')
            self.stat.parse_stat(gear_grade='epic', gear_level=85, mod=True, rolled=3, mod_type='lesser')
            formatted_text = self.stat.format_stat(show_reforged=True)
            parsed_text_list.add(formatted_text)
            expected_texts = list(expected_text_list)

            self.assertIn(formatted_text, expected_texts, f"{formatted_text} was no expected.")
            
        missing_vals = expected_text_list - parsed_text_list
        extra_vals = parsed_text_list - expected_text_list
        
        self.assertFalse(missing_vals, f"The following values were not selected: {missing_vals}")
        self.assertFalse(extra_vals, f"The following extra values were selected: {extra_vals}")  
        
        
    def test_format_stat_sub_5(self):
        """
        Test using Speed as our substat, gear_grade='rare', gear_level = 90
        show_reforge = False and mod = False
        We expect values (2, 3, 4) 
        Repeat this test 1000 times.
        """
        parsed_text_list = set()
        expected_text_list = set(['2 Speed', '3 Speed', '4 Speed'])
        
        for i in range(1000):
            
            self.stat.get_stat_by_id(10, stat_type='substat')
            self.stat.parse_stat(gear_grade='rare', gear_level=90, mod=False, rolled=0, mod_type='lesser')
            formatted_text = self.stat.format_stat(show_reforged=False)
            parsed_text_list.add(formatted_text)
            expected_texts = list(expected_text_list)

            self.assertIn(formatted_text, expected_texts, f"{formatted_text} was no expected.")
            
        missing_vals = expected_text_list - parsed_text_list
        extra_vals = parsed_text_list - expected_text_list
        
        self.assertFalse(missing_vals, f"The following values were not selected: {missing_vals}")
        self.assertFalse(extra_vals, f"The following extra values were selected: {extra_vals}")
        
        
    def test_format_stat_sub_6(self):
        """
        Test using Speed as our substat, gear_grade='rare', gear_level = 90
        show_reforge = True, rolled = 2 (so reforge_increase should be 2),  and mod = False
        We expect values (2, 3, 4) 
        Repeat this test 1000 times.
        """
        parsed_text_list = set()
        expected_text_list = set(['2 (4) Speed', '3 (5) Speed', '4 (6) Speed'])
        
        for i in range(1000):
            
            self.stat.get_stat_by_id(10, stat_type='substat')
            self.stat.parse_stat(gear_grade='rare', gear_level=90, mod=False, rolled=2, mod_type='lesser')
            formatted_text = self.stat.format_stat(show_reforged=True)
            parsed_text_list.add(formatted_text)
            expected_texts = list(expected_text_list)

            self.assertIn(formatted_text, expected_texts, f"{formatted_text} was no expected.")
            
        missing_vals = expected_text_list - parsed_text_list
        extra_vals = parsed_text_list - expected_text_list
        
        self.assertFalse(missing_vals, f"The following values were not selected: {missing_vals}")
        self.assertFalse(extra_vals, f"The following extra values were selected: {extra_vals}")  

        
    def test_format_stat_sub_7(self):
        """
        Test using Speed as our substat, gear_grade='epic', gear_level = 88
        show_reforge = True, rolled = 2 (so reforge_increase should be 2), and mod = True
        We expect base values (4, 5, 6) and reforged values (6, 7, 8)
        Repeat this test 1000 times.
        """
        parsed_text_list = set()
        expected_text_list = set(['4 (6) Speed (modded)', '5 (7) Speed (modded)', '6 (8) Speed (modded)'])
        
        for i in range(1000):
            
            self.stat.get_stat_by_id(10, stat_type='substat')
            self.stat.parse_stat(gear_grade='epic', gear_level=88, mod=True, rolled=2, mod_type='greater')
            formatted_text = self.stat.format_stat(show_reforged=True)
            parsed_text_list.add(formatted_text)
            expected_texts = list(expected_text_list)

            self.assertIn(formatted_text, expected_texts, f"{formatted_text} was no expected.")
            
        missing_vals = expected_text_list - parsed_text_list
        extra_vals = parsed_text_list - expected_text_list
        
        self.assertFalse(missing_vals, f"The following values were not selected: {missing_vals}")
        self.assertFalse(extra_vals, f"The following extra values were selected: {extra_vals}")  
        
if __name__ == '__main__':
    unittest.main()