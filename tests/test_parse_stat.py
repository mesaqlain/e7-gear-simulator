from set_directory_function import set_directory
set_directory()

import unittest
import json
import random
from src.stats import Stat
from src.validation_utils import *
from src.utilities import *

class TestParseStat(unittest.TestCase):
    
    def setUp(self):
        self.stat = Stat()
        stat = self.stat.get_random_stat()
        stat_id = self.stat.stat_id
        stat_key = self.stat.stat_key
        stat_type = self.stat.stat_type
        gear_type = self.stat.gear_type
        # print(f"stat_id: {stat_id}")
        # print(f"stat_key: {stat_key}")
        # print(f"stat_type: {stat_type}")
        # print(f"gear_type: {gear_type}")

        
    def tearDown(self):
        self.stat = None
        
        
    def print_stat_info(self):
        """
        Helper function to print stat information for easier debugging.
        """
        print(f"parsed stat_id: {self.stat.stat_id}")
        print(f"parsed stat_key: {self.stat.stat_key}")
        print(f"parsed stat_type: {self.stat.stat_type}")
        print(f"parsed gear_type: {self.stat.gear_type}")
        print(f"parsed text: {self.stat.text}")
        print(f"parsed gear_grade: {self.stat.gear_grade}")
        print(f"parsed gear_level: {self.stat.gear_level}")
        print(f"parsed gear_tier: {self.stat.gear_tier}")
        print(f"parsed rolled: {self.stat.rolled}")
        print(f"parsed value: {self.stat.value}")
        print(f"parsed value_key: {self.stat.value_key}")
        print(f"parsed reforge_increase: {self.stat.reforge_increase}")
        print("-----------")
        
        
    def test_parse_stat_all_none(self):
        """
        Test parse_stat when everthing is set to None so default values are -
        gear_grade = None (randomly chosen)
        gear_level = None (default 85)
        mod = False (default False)
        rolled = None (default None = False)
        mod_type = 'greater' (default is 'greater')
        
        """
        self.stat.parse_stat()
        #self.print_stat_info()
        
        expected_stat_type = 'mainstat'
        expected_gear_type = None
        expected_gear_grades = list(GRADES.keys())
        expected_gear_level = 85
        expected_gear_tier = 6
        expected_rolled = 0
        #expected_value = 
        expected_value_key = '<A>'
        #expected_reforge_increase = 
        
        self.assertEqual(self.stat.stat_type, expected_stat_type, f"Parsed gear stat type should be {expected_stat_type}")
        self.assertIsNone(self.stat.gear_type, f"Parsed gear type should be None")
        self.assertIn(self.stat.gear_grade, expected_gear_grades, f"Parsed gear should be in {expected_gear_grades}")
        self.assertEqual(self.stat.gear_level, expected_gear_level, f"Parsed gear should be level {expected_gear_level}.")
        self.assertEqual(self.stat.gear_tier, expected_gear_tier, f"Parsed gear should be tier {expected_gear_tier}.")
        self.assertEqual(self.stat.rolled, expected_rolled, f"Parsed gear should have {expected_rolled} roll(s).")
        self.assertEqual(self.stat.value_key, expected_value_key, f"Parsed value_key should be {expected_value_key}.")
        self.assertFalse(self.stat.modded)

        
    def test_parse_stat_all_none_grade_heroic(self):
        """
        Test parse_stat when gear_grade is set to 'heroic' and all others default
        """
        self.stat.parse_stat(gear_grade='heroic')
        #self.print_stat_info()
        
        expected_stat_type = 'mainstat'
        expected_gear_type = None
        expected_gear_grades = 'heroic'
        expected_gear_level = 85
        expected_gear_tier = 6
        expected_rolled = 0
        #expected_value = 
        expected_value_key = '<A>'
        #expected_reforge_increase = 
        
        self.assertEqual(self.stat.stat_type, expected_stat_type, f"Parsed gear stat type should be {expected_stat_type}")
        self.assertIsNone(self.stat.gear_type, f"Parsed gear type should be None")
        self.assertEqual(self.stat.gear_grade, expected_gear_grades, f"Parsed gear should be in {expected_gear_grades}")
        self.assertEqual(self.stat.gear_level, expected_gear_level, f"Parsed gear should be level {expected_gear_level}.")
        self.assertEqual(self.stat.gear_tier, expected_gear_tier, f"Parsed gear should be tier {expected_gear_tier}.")
        self.assertEqual(self.stat.rolled, expected_rolled, f"Parsed gear should have {expected_rolled} roll(s).")
        self.assertEqual(self.stat.value_key, expected_value_key, f"Parsed value_key should be {expected_value_key}.")
        self.assertFalse(self.stat.modded)

        
    def test_parse_stat_3(self):
        """
        Test parse_stat when gear_grade='heroic' and gear_level=88
        """
        self.stat.parse_stat(gear_grade='epic', gear_level=88)
        #self.print_stat_info()
        
        expected_stat_type = 'mainstat'
        expected_gear_type = None
        expected_gear_grades = 'epic'
        expected_gear_level = 88
        expected_gear_tier = 7
        expected_rolled = 0
        #expected_value = 
        expected_value_key = '<A>'
        #expected_reforge_increase = 
        
        self.assertEqual(self.stat.stat_type, expected_stat_type, f"Parsed gear stat type should be {expected_stat_type}")
        self.assertIsNone(self.stat.gear_type, f"Parsed gear type should be None")
        self.assertEqual(self.stat.gear_grade, expected_gear_grades, f"Parsed gear should be in {expected_gear_grades}")
        self.assertEqual(self.stat.gear_level, expected_gear_level, f"Parsed gear should be level {expected_gear_level}.")
        self.assertEqual(self.stat.gear_tier, expected_gear_tier, f"Parsed gear should be tier {expected_gear_tier}.")
        self.assertEqual(self.stat.rolled, expected_rolled, f"Parsed gear should have {expected_rolled} roll(s).")
        self.assertEqual(self.stat.value_key, expected_value_key, f"Parsed value_key should be {expected_value_key}.")
        self.assertFalse(self.stat.modded)
        
        
    def test_parse_stat_4(self):
        """
        Test parse_stat when gear_grade='heroic', gear_level=88, rolled=3
        """
        self.stat.parse_stat(stat_type='substat', gear_grade='rare', gear_level=88, rolled=3)
        #self.print_stat_info()
        
        expected_stat_type = 'substat'
        expected_gear_type = None
        expected_gear_grades = 'rare'
        expected_gear_level = 88
        expected_gear_tier = 7
        expected_rolled = 3
        #expected_value = 
        expected_value_key = '<A>'
        #expected_reforge_increase = 
        
        self.assertEqual(self.stat.stat_type, expected_stat_type, f"Parsed gear stat type should be {expected_stat_type}")
        self.assertIsNone(self.stat.gear_type, f"Parsed gear type should be None")
        self.assertEqual(self.stat.gear_grade, expected_gear_grades, f"Parsed gear should be in {expected_gear_grades}")
        self.assertEqual(self.stat.gear_level, expected_gear_level, f"Parsed gear should be level {expected_gear_level}.")
        self.assertEqual(self.stat.gear_tier, expected_gear_tier, f"Parsed gear should be tier {expected_gear_tier}.")
        self.assertEqual(self.stat.rolled, expected_rolled, f"Parsed gear should have {expected_rolled} roll(s).")
        self.assertEqual(self.stat.value_key, expected_value_key, f"Parsed value_key should be {expected_value_key}.")
        self.assertFalse(self.stat.modded)
        
        
    def test_parse_stat_5(self):
        """
        Test parse_stat when gear_grade='epic', gear_level=70, stat_type='substat'
        """
        self.stat.parse_stat(gear_grade='epic', gear_level=70, stat_type='substat')
        #self.print_stat_info()
        
        expected_stat_type = 'substat'
        expected_gear_type = None
        expected_gear_grades = 'epic'
        expected_gear_level = 70
        expected_gear_tier = 5
        expected_rolled = 0
        #expected_value = 
        expected_value_key = '<A>'
        #expected_reforge_increase = 
        
        self.assertEqual(self.stat.stat_type, expected_stat_type, f"Parsed gear stat type should be {expected_stat_type}")
        self.assertIsNone(self.stat.gear_type, f"Parsed gear type should be None")
        self.assertEqual(self.stat.gear_grade, expected_gear_grades, f"Parsed gear should be in {expected_gear_grades}")
        self.assertEqual(self.stat.gear_level, expected_gear_level, f"Parsed gear should be level {expected_gear_level}.")
        self.assertEqual(self.stat.gear_tier, expected_gear_tier, f"Parsed gear should be tier {expected_gear_tier}.")
        self.assertEqual(self.stat.rolled, expected_rolled, f"Parsed gear should have {expected_rolled} roll(s).")
        self.assertEqual(self.stat.value_key, expected_value_key, f"Parsed value_key should be {expected_value_key}.")
        self.assertFalse(self.stat.modded)

        
    def test_parse_stat_6(self):
        """
        Test parse_stat when gear_grade='heroic', gear_level=88, 
        """
        self.stat.parse_stat(gear_grade='epic', gear_level=70, stat_type='substat', gear_type='boots')
        #self.print_stat_info()
        
        expected_stat_type = 'substat'
        expected_gear_type = 'boots'
        expected_gear_grades = 'epic'
        expected_gear_level = 70
        expected_gear_tier = 5
        expected_rolled = 0
        #expected_value = 
        expected_value_key = '<A>'
        #expected_reforge_increase = 
        
        self.assertEqual(self.stat.stat_type, expected_stat_type, f"Parsed gear stat type should be {expected_stat_type}")
        self.assertEqual(self.stat.gear_type, expected_gear_type, f"Parsed gear type should be None")
        self.assertEqual(self.stat.gear_grade, expected_gear_grades, f"Parsed gear should be in {expected_gear_grades}")
        self.assertEqual(self.stat.gear_level, expected_gear_level, f"Parsed gear should be level {expected_gear_level}.")
        self.assertEqual(self.stat.gear_tier, expected_gear_tier, f"Parsed gear should be tier {expected_gear_tier}.")
        self.assertEqual(self.stat.rolled, expected_rolled, f"Parsed gear should have {expected_rolled} roll(s).")
        self.assertEqual(self.stat.value_key, expected_value_key, f"Parsed value_key should be {expected_value_key}.")
        self.assertFalse(self.stat.modded)

        
    def test_parse_stat_invalid_type_and_roll(self):
        """
        Mainstats cannot have rolled values, so this should raise value error
        """
        with self.assertRaises(ValueError):
            self.stat.parse_stat(stat_type='mainstat', gear_grade='heroic', gear_level=88, rolled=3)
        
        
    def test_parse_stat_invalid_type_and_roll_2(self):
        """
        Mainstats cannot have rolled values, so this should raise value error when stat_type is left None
        """
        with self.assertRaises(ValueError):
            self.stat.parse_stat(gear_grade='heroic', gear_level=88, rolled=2)
            
            

class TestParseStatCritChance(unittest.TestCase):
    
    def setUp(self):
        """Initialize a stat that has id 6 (crit rate)"""
        self.stat = Stat()
        stat = self.stat.get_stat_by_id(6)
        stat_id = self.stat.stat_id
        stat_key = self.stat.stat_key
        stat_type = self.stat.stat_type
        gear_type = self.stat.gear_type
        # print(f"stat_id: {stat_id}")
        # print(f"stat_key: {stat_key}")
        # print(f"stat_type: {stat_type}")
        # print(f"gear_type: {gear_type}")

        
    def tearDown(self):
        self.stat = None

            
    def print_stat_info(self):
        """
        Helper function to print stat information for easier debugging.
        """
        print(f"parsed stat_id: {self.stat.stat_id}")
        print(f"parsed stat_key: {self.stat.stat_key}")
        print(f"parsed stat_type: {self.stat.stat_type}")
        print(f"parsed gear_type: {self.stat.gear_type}")
        print(f"parsed text: {self.stat.text}")
        print(f"parsed gear_grade: {self.stat.gear_grade}")
        print(f"parsed gear_level: {self.stat.gear_level}")
        print(f"parsed gear_tier: {self.stat.gear_tier}")
        print(f"parsed rolled: {self.stat.rolled}")
        print(f"parsed value: {self.stat.value}")
        print(f"parsed value_key: {self.stat.value_key}")
        print(f"parsed reforge_increase: {self.stat.reforge_increase}")
        print("-----------")
        
        
    def test_parse_stat_crit_all_none(self):
        """
        Test parse_stat when everthing is set to None so default values are -
        gear_grade = None (randomly chosen)
        gear_level = None (default 85)
        mod = False (default False)
        rolled = None (default None = False)
        mod_type = 'greater' (default is 'greater')
        
        """
        self.stat.parse_stat()
        #self.print_stat_info()
        
        expected_stat_id = '6'
        expected_stat_key = 'crit_rate'
        expected_stat_type = 'mainstat'
        expected_gear_type = None
        expected_gear_grades = list(GRADES.keys())
        expected_gear_level = 85
        expected_gear_tier = 6
        expected_rolled = 0
        expected_value = 11
        expected_value_key = '<A>'
        expected_reforge_increase = 60
        
        self.assertEqual(self.stat.stat_id, expected_stat_id, f"Parsed gear stat id should be {expected_stat_id}")
        self.assertEqual(self.stat.stat_key, expected_stat_key, f"Parsed gear stat key should be {expected_stat_key}")
        self.assertEqual(self.stat.stat_type, expected_stat_type, f"Parsed gear stat type should be {expected_stat_type}")
        self.assertIsNone(self.stat.gear_type, f"Parsed gear type should be None")
        self.assertIn(self.stat.gear_grade, expected_gear_grades, f"Parsed gear should be in {expected_gear_grades}")
        self.assertEqual(self.stat.gear_level, expected_gear_level, f"Parsed gear should be level {expected_gear_level}.")
        self.assertEqual(self.stat.gear_tier, expected_gear_tier, f"Parsed gear should be tier {expected_gear_tier}.")
        self.assertEqual(self.stat.rolled, expected_rolled, f"Parsed gear should have {expected_rolled} roll(s).")
        self.assertEqual(self.stat.value, expected_value, f"Parsed value should be {expected_value}.")
        self.assertEqual(self.stat.value_key, expected_value_key, f"Parsed value_key should be {expected_value_key}.")
        self.assertEqual(self.stat.reforge_increase, expected_reforge_increase, f"Parsed reforge_increase should be {expected_reforge_increase}.")
        self.assertFalse(self.stat.modded)

        
    def test_parse_stat_crit_2(self):
        """
        Test parse_stat when stat_type='substat', gear_level=90, gear_grade='rare'        
        """
        parsed_vals = set()
        
        for i in range(100):
            self.stat.parse_stat(stat_type='substat', gear_level=90, gear_grade='rare')
            #self.print_stat_info()
            
            parsed_vals.add(self.stat.value)

            expected_stat_id = '6'
            expected_stat_key = 'crit_rate'
            expected_stat_type = 'substat'
            expected_gear_type = None
            expected_gear_grades = 'rare'
            expected_gear_level = 90
            expected_gear_tier = 7
            expected_rolled = 0
            expected_values = [3, 4, 5]
            expected_value_key = '<A>'
            expected_reforge_increase = 1

            self.assertEqual(self.stat.stat_id, expected_stat_id, f"Parsed gear stat id should be {expected_stat_id}")
            self.assertEqual(self.stat.stat_key, expected_stat_key, f"Parsed gear stat key should be {expected_stat_key}")
            self.assertEqual(self.stat.stat_type, expected_stat_type, f"Parsed gear stat type should be {expected_stat_type}")
            self.assertIsNone(self.stat.gear_type, f"Parsed gear type should be None")
            self.assertIn(self.stat.gear_grade, expected_gear_grades, f"Parsed gear should be in {expected_gear_grades}")
            self.assertEqual(self.stat.gear_level, expected_gear_level, f"Parsed gear should be level {expected_gear_level}.")
            self.assertEqual(self.stat.gear_tier, expected_gear_tier, f"Parsed gear should be tier {expected_gear_tier}.")
            self.assertEqual(self.stat.rolled, expected_rolled, f"Parsed gear should have {expected_rolled} roll(s).")
            self.assertIn(self.stat.value, expected_values, f"Parsed value should be in {expected_values}.")
            self.assertEqual(self.stat.value_key, expected_value_key, f"Parsed value_key should be {expected_value_key}.")
            self.assertEqual(self.stat.reforge_increase, expected_reforge_increase, 
                             f"Parsed reforge_increase should be {expected_reforge_increase}.")  
            self.assertFalse(self.stat.modded)
        
        expected_vals = set([3, 4, 5])
        missing_vals = expected_vals - parsed_vals
        extra_vals = parsed_vals - expected_vals
        
        self.assertFalse(missing_vals, f"The following values were not selected: {missing_vals}")
        self.assertFalse(extra_vals, f"The following extra values were selected: {extra_vals}")

        
    def test_parse_stat_crit_3(self):
        """
        Test parse_stat when stat_type='substat', gear_level=70, gear_grade='epic'        
        """
        parsed_vals = set()
        
        for i in range(100):
            self.stat.parse_stat(stat_type='substat', gear_level=70, gear_grade='epic')
            #self.print_stat_info()
            
            parsed_vals.add(self.stat.value)

            expected_stat_id = '6'
            expected_stat_key = 'crit_rate'
            expected_stat_type = 'substat'
            expected_gear_type = None
            expected_gear_grades = 'epic'
            expected_gear_level = 70
            expected_gear_tier = 5
            expected_rolled = 0
            expected_values = [2, 3, 4]
            expected_value_key = '<A>'
            expected_reforge_increase = 1

            self.assertEqual(self.stat.stat_id, expected_stat_id, f"Parsed gear stat id should be {expected_stat_id}")
            self.assertEqual(self.stat.stat_key, expected_stat_key, f"Parsed gear stat key should be {expected_stat_key}")
            self.assertEqual(self.stat.stat_type, expected_stat_type, f"Parsed gear stat type should be {expected_stat_type}")
            self.assertIsNone(self.stat.gear_type, f"Parsed gear type should be None")
            self.assertIn(self.stat.gear_grade, expected_gear_grades, f"Parsed gear should be in {expected_gear_grades}")
            self.assertEqual(self.stat.gear_level, expected_gear_level, f"Parsed gear should be level {expected_gear_level}.")
            self.assertEqual(self.stat.gear_tier, expected_gear_tier, f"Parsed gear should be tier {expected_gear_tier}.")
            self.assertEqual(self.stat.rolled, expected_rolled, f"Parsed gear should have {expected_rolled} roll(s).")
            self.assertIn(self.stat.value, expected_values, f"Parsed value should be in {expected_values}.")
            self.assertEqual(self.stat.value_key, expected_value_key, f"Parsed value_key should be {expected_value_key}.")
            self.assertEqual(self.stat.reforge_increase, expected_reforge_increase, 
                             f"Parsed reforge_increase should be {expected_reforge_increase}.")        
            self.assertFalse(self.stat.modded)
            
        expected_vals = set([2, 3, 4])
        missing_vals = expected_vals - parsed_vals
        extra_vals = parsed_vals - expected_vals
        
        self.assertFalse(missing_vals, f"The following values were not selected: {missing_vals}")
        self.assertFalse(extra_vals, f"The following extra values were selected: {extra_vals}")  
        
        
class TestParseStatModTrueInvalid(unittest.TestCase):
    
    def setUp(self):
        """Initialize a stat that has id 10 (speed), stat_type=''gear_type='weapon'"""
        self.stat = Stat()
        
        
    def tearDown(self):
        self.stat = None       
        
        
    def test_parse_stat_speed_invalid_1(self):
        """
        Test parse_stat when everthing mod=True and others default.
        Should get value error as mainstats cannot have mod
        
        """
        self.stat.get_stat_by_id(10)
        with self.assertRaises(ValueError):
            self.stat.parse_stat(mod=True)
    
        
    def test_parse_stat_invalid_2(self):
        """
        Test parse_stat when everthing mod=True and others default.
        Should get value error as mainstats cannot have mod
        get_stat_by_id()
        """
        self.stat.get_stat_by_id(5, stat_type='mainstat')
        with self.assertRaises(ValueError):
            self.stat.parse_stat(mod=True)
        
        
    def test_parse_stat_invalid_3(self):
        """
        Test parse_stat when everthing mod=True and others default.
        Should get value error as mainstats cannot have mod
        get_random_stat()
        """
        self.stat.get_random_stat()
        with self.assertRaises(ValueError):
            self.stat.parse_stat(mod=True)
            
            
    def test_parse_stat_invalid_4(self):
        """
        Test parse_stat when everthing mod=True and others default.
        Should get value error as mainstats cannot have mod
        get_non_overlapping_stat()
        """
        self.stat.get_non_overlapping_stat([1, 2, 3], 'mainstat')
        with self.assertRaises(ValueError):
            self.stat.parse_stat(mod=True)
        
        
class TestParseStatModTrueSpeed(unittest.TestCase):
    
    def setUp(self):
        """Initialize a stat that has id 10 (speed), stat_type=''gear_type='weapon'"""
        self.stat = Stat()
        stat = self.stat.get_stat_by_id(10)
        
        
    def tearDown(self):
        self.stat = None       
        
        
    def test_parse_stat_speed_valid(self):
        """
        Test parse_stat when stat_id=10, stat_type='substat', mod=True        
        """
        
        parsed_vals = set()

        for i in range(100):
            self.stat.parse_stat(stat_type='substat', gear_level=70, gear_grade='heroic', mod=True)
            #self.print_stat_info()
            
            parsed_vals.add(self.stat.value)

            expected_stat_id = '10'
            expected_stat_key = 'speed_flat'
            expected_stat_type = 'substat'
            expected_gear_type = None
            expected_gear_grades = 'heroic'
            expected_gear_level = 70
            expected_gear_tier = 5
            expected_rolled = 0
            expected_values = [2, 3, 4]
            expected_value_key = '<A>'
            expected_reforge_increase = 0

            self.assertEqual(self.stat.stat_id, expected_stat_id, f"Parsed gear stat id should be {expected_stat_id}")
            self.assertEqual(self.stat.stat_key, expected_stat_key, f"Parsed gear stat key should be {expected_stat_key}")
            self.assertEqual(self.stat.stat_type, expected_stat_type, f"Parsed gear stat type should be {expected_stat_type}")
            self.assertIsNone(self.stat.gear_type, f"Parsed gear type should be None")
            self.assertIn(self.stat.gear_grade, expected_gear_grades, f"Parsed gear should be in {expected_gear_grades}")
            self.assertEqual(self.stat.gear_level, expected_gear_level, f"Parsed gear should be level {expected_gear_level}.")
            self.assertEqual(self.stat.gear_tier, expected_gear_tier, f"Parsed gear should be tier {expected_gear_tier}.")
            self.assertEqual(self.stat.rolled, expected_rolled, f"Parsed gear should have {expected_rolled} roll(s).")
            self.assertIn(self.stat.value, expected_values, f"Parsed value should be in {expected_values}.")
            self.assertEqual(self.stat.value_key, expected_value_key, f"Parsed value_key should be {expected_value_key}.")
            self.assertEqual(self.stat.reforge_increase, expected_reforge_increase, 
                             f"Parsed reforge_increase should be {expected_reforge_increase}.")  
            self.assertTrue(self.stat.modded)
        
        expected_vals = set([2, 3, 4])
        missing_vals = expected_vals - parsed_vals
        extra_vals = parsed_vals - expected_vals
        
        self.assertFalse(missing_vals, f"The following values were not selected: {missing_vals}")
        self.assertFalse(extra_vals, f"The following extra values were selected: {extra_vals}")    
        

    def test_parse_stat_speed_valid_2(self):
        """
        Test parse_stat when stat_id=10, stat_type='substat', mod=True, 
        gear_level=90, gear_grade='epic', rolled=4
        """
        
        parsed_vals = set()

        for i in range(100):
            self.stat.parse_stat(stat_type='substat', gear_level=90, gear_grade='epic', mod=True, rolled=4)
            #self.print_stat_info()
            
            parsed_vals.add(self.stat.value)

            expected_stat_id = '10'
            expected_stat_key = 'speed_flat'
            expected_stat_type = 'substat'
            expected_gear_type = None
            expected_gear_grades = 'epic'
            expected_gear_level = 90
            expected_gear_tier = 7
            expected_rolled = 4
            expected_values = [10, 11, 12, 13]
            expected_value_key = '<A>'
            expected_reforge_increase = 4

            self.assertEqual(self.stat.stat_id, expected_stat_id, f"Parsed gear stat id should be {expected_stat_id}")
            self.assertEqual(self.stat.stat_key, expected_stat_key, f"Parsed gear stat key should be {expected_stat_key}")
            self.assertEqual(self.stat.stat_type, expected_stat_type, f"Parsed gear stat type should be {expected_stat_type}")
            self.assertIsNone(self.stat.gear_type, f"Parsed gear type should be None")
            self.assertIn(self.stat.gear_grade, expected_gear_grades, f"Parsed gear should be in {expected_gear_grades}")
            self.assertEqual(self.stat.gear_level, expected_gear_level, f"Parsed gear should be level {expected_gear_level}.")
            self.assertEqual(self.stat.gear_tier, expected_gear_tier, f"Parsed gear should be tier {expected_gear_tier}.")
            self.assertEqual(self.stat.rolled, expected_rolled, f"Parsed gear should have {expected_rolled} roll(s).")
            self.assertIn(self.stat.value, expected_values, f"Parsed value should be in {expected_values}.")
            self.assertEqual(self.stat.value_key, expected_value_key, f"Parsed value_key should be {expected_value_key}.")
            self.assertEqual(self.stat.reforge_increase, expected_reforge_increase, 
                             f"Parsed reforge_increase should be {expected_reforge_increase}.")  
            self.assertTrue(self.stat.modded)
        
        expected_vals = set([10, 11, 12, 13])
        missing_vals = expected_vals - parsed_vals
        extra_vals = parsed_vals - expected_vals
        
        self.assertFalse(missing_vals, f"The following values were not selected: {missing_vals}")
        self.assertFalse(extra_vals, f"The following extra values were selected: {extra_vals}")    
        
        
    def test_parse_stat_speed_valid_3(self):
        """
        Test parse_stat when stat_id=10, stat_type='substat', mod=True, 
        gear_level=85, gear_grade='heroic', rolled=2, mod_type='lesser'
        """
        
        parsed_vals = set()

        for i in range(100):
            self.stat.parse_stat(stat_type='substat', gear_level=85, gear_grade='heroic', mod=True, rolled=2, mod_type='lesser')
            #self.print_stat_info()
            
            parsed_vals.add(self.stat.value)

            expected_stat_id = '10'
            expected_stat_key = 'speed_flat'
            expected_stat_type = 'substat'
            expected_gear_type = None
            expected_gear_grades = 'heroic'
            expected_gear_level = 85
            expected_gear_tier = 6
            expected_rolled = 2
            expected_values = [3, 4, 5]
            expected_value_key = '<A>'
            expected_reforge_increase = 2

            self.assertEqual(self.stat.stat_id, expected_stat_id, f"Parsed gear stat id should be {expected_stat_id}")
            self.assertEqual(self.stat.stat_key, expected_stat_key, f"Parsed gear stat key should be {expected_stat_key}")
            self.assertEqual(self.stat.stat_type, expected_stat_type, f"Parsed gear stat type should be {expected_stat_type}")
            self.assertIsNone(self.stat.gear_type, f"Parsed gear type should be None")
            self.assertIn(self.stat.gear_grade, expected_gear_grades, f"Parsed gear should be in {expected_gear_grades}")
            self.assertEqual(self.stat.gear_level, expected_gear_level, f"Parsed gear should be level {expected_gear_level}.")
            self.assertEqual(self.stat.gear_tier, expected_gear_tier, f"Parsed gear should be tier {expected_gear_tier}.")
            self.assertEqual(self.stat.rolled, expected_rolled, f"Parsed gear should have {expected_rolled} roll(s).")
            self.assertIn(self.stat.value, expected_values, f"Parsed value should be in {expected_values}.")
            self.assertEqual(self.stat.value_key, expected_value_key, f"Parsed value_key should be {expected_value_key}.")
            self.assertEqual(self.stat.reforge_increase, expected_reforge_increase, 
                             f"Parsed reforge_increase should be {expected_reforge_increase}.")  
            self.assertTrue(self.stat.modded)
        
        expected_vals = set([3, 4, 5])
        missing_vals = expected_vals - parsed_vals
        extra_vals = parsed_vals - expected_vals
        
        self.assertFalse(missing_vals, f"The following values were not selected: {missing_vals}")
        self.assertFalse(extra_vals, f"The following extra values were selected: {extra_vals}")    

        
class TestParseStatModTrueNonOverlapping(unittest.TestCase):
    
    def setUp(self):
        """Initialize a stat that has id 10 (speed), stat_type=''gear_type='weapon'"""
        self.stat = Stat()
        
        
    def tearDown(self):
        self.stat = None       
        
        
    def test_parse_stat_non_overlapping_1(self):
        """
        Test parse_stat when using get_non_overlapping_stat(), stat_type='substat', gear_type='ring'
        mod=True, rolled=2, mod_type='lesser'        
        """
        
        chosen_ids = set()
        expected_ids = set(['4', '5', '6', '7', '8', '9', '10'])

        for i in range(1000):
            self.stat.get_non_overlapping_stat([0,1,2,3], stat_type='substat', gear_type='ring')
            self.stat.parse_stat(mod=True, rolled=2, mod_type='lesser')
            #self.print_stat_info()
            
            chosen_ids.add(self.stat.stat_id)

            expected_stat_ids = list(expected_ids)
            expected_stat_type = 'substat'
            expected_gear_type = 'ring'
            expected_gear_grades = list(GRADES.keys())
            expected_gear_level = 85
            expected_gear_tier = 6
            expected_rolled = 2

            self.assertEqual(self.stat.stat_type, expected_stat_type, f"Parsed gear stat type should be {expected_stat_type}")
            self.assertEqual(self.stat.gear_type, expected_gear_type, f"Parsed gear stat type should be {expected_gear_type}")
            self.assertIn(self.stat.gear_grade, expected_gear_grades, f"Parsed gear should be in {expected_gear_grades}")
            self.assertEqual(self.stat.gear_level, expected_gear_level, f"Parsed gear should be level {expected_gear_level}.")
            self.assertEqual(self.stat.gear_tier, expected_gear_tier, f"Parsed gear should be tier {expected_gear_tier}.")
            self.assertEqual(self.stat.rolled, expected_rolled, f"Parsed gear should have {expected_rolled} roll(s).")
            self.assertTrue(self.stat.modded)
        
        missing = expected_ids - chosen_ids
        extra = chosen_ids - expected_ids
        
        self.assertFalse(missing, f"The following ids were not selected: {missing}")
        self.assertFalse(extra, f"The following extra ids were selected: {extra}")    
        

        
    def test_parse_stat_non_overlapping_2(self):
        """
        Test parse_stat when using get_non_overlapping_stat(), stat_type='substat', gear_type='ring'
        mod=True, rolled=2, mod_type='lesser'        
        """
        
        chosen_ids = set()
        expected_ids = set(['2', '3', '5', '10'])

        for i in range(1000):
            self.stat.get_non_overlapping_stat([6,7,8,9], stat_type='substat', gear_type='armor')
            self.stat.parse_stat(gear_level=88, mod=True, rolled=5, mod_type='greater')
            #self.print_stat_info()
            
            chosen_ids.add(self.stat.stat_id)

            expected_stat_ids = list(expected_ids)
            expected_stat_type = 'substat'
            expected_gear_type = 'armor'
            expected_gear_grades = list(GRADES.keys())
            expected_gear_level = 88
            expected_gear_tier = 7
            expected_rolled = 2

            self.assertEqual(self.stat.stat_type, expected_stat_type, f"Parsed gear stat type should be {expected_stat_type}")
            self.assertEqual(self.stat.gear_type, expected_gear_type, f"Parsed gear stat type should be {expected_gear_type}")
            self.assertIn(self.stat.gear_grade, expected_gear_grades, f"Parsed gear should be in {expected_gear_grades}")
            self.assertEqual(self.stat.gear_level, expected_gear_level, f"Parsed gear should be level {expected_gear_level}.")
            self.assertEqual(self.stat.gear_tier, expected_gear_tier, f"Parsed gear should be tier {expected_gear_tier}.")
            self.assertEqual(self.stat.rolled, expected_rolled, f"Parsed gear should have {expected_rolled} roll(s).")
            self.assertTrue(self.stat.modded)
        
        missing = expected_ids - chosen_ids
        extra = chosen_ids - expected_ids
        
        self.assertFalse(missing, f"The following ids were not selected: {missing}")
        self.assertFalse(extra, f"The following extra ids were selected: {extra}")    
        
        
if __name__ == '__main__':
    unittest.main()
